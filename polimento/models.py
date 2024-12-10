from django.db import models
from producao.models import *
from polimento.models import *
from chapa.models import Chapa
from smart_selects.db_fields import ChainedForeignKey

# Create your models here.
TIPO_DE_ABRASIVOS = (
        ('DIAMANTADO','DIAMANTADO'),('COMUM', 'COMUM'),
    )


LINHA_CHOICES = (
        ('1', 'MESAS'),
        ('2', 'AUTOMÁTICA'),
        ('3', 'AUTOMÁTICA C/30 BANDEIJAS')
    )
class Tipo_Polimento(models.Model):
    tipo_polimento = models.CharField(max_length=50)
    class Meta:
        verbose_name = 'Tipo de Polimento'
        verbose_name_plural = 'Tipos de Polimentos'
    def __str__(self):
        return self.tipo_polimento

class Abrasivo(models.Model):
    fornecedor = models.ForeignKey(Pessoa, on_delete=models.PROTECT, default=1)
    grao = models.IntegerField(default=0)
    descricao = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)  
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_alteracao = models.DateTimeField(auto_now=True)
    usuario_cadastrou = models.ForeignKey(User, on_delete=PROTECT)

    def __str__(self):
        return self.descricao


class Qualidade(models.Model):
    qualidade = models.CharField(max_length=100, primary_key=True)
    def __str__(self):
        return self.qualidade



class Polimento(models.Model):
    data = models.DateField(default=timezone.now)
    turno = models.PositiveIntegerField(default=1)
    #Operador = models.ForeignKey(Operador, on_delete=models.CASCADE)
    operador = models.ForeignKey(Operador, on_delete=models.CASCADE, default=3)
    maquina = models.ForeignKey(Maquina, on_delete=models.CASCADE)
    horimetro_inicial = models.FloatField(default=0)
    horimetro_final = models.FloatField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'Chapas Polidas'
        verbose_name_plural = 'Chapas Polidas'

    def __str__(self):
        return self.data.strftime('%d/%m/%Y')

class Chapas_Polidas(models.Model):
    polimento = models.ForeignKey(Polimento, on_delete=models.CASCADE)
    mudanca_numero = models.BigIntegerField(default=0, verbose_name="Mudança/Set")
    bloco = models.ForeignKey(Bloco, on_delete=models.PROTECT)
    qtde_chapas = models.PositiveIntegerField(default=0)
    acabamento = models.ForeignKey(Acabamento, on_delete=models.PROTECT, default=2)
    chapas_quebradas = models.PositiveIntegerField(default=0)
    velocidade = models.PositiveIntegerField(default=0)
    frequencia = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return str(self.id)
    
class Parada_Politriz(models.Model):
    polimento_id = models.ForeignKey(Polimento, on_delete=models.PROTECT, default=12)
    data_inicial = models.DateTimeField(default=timezone.now)
    data_final = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

"""
class Jogo_de_Abrasivos(models.Model):
    id =  models.AutoField(primary_key=True)
    abrasivo = models.ForeignKey(Abrasivo, on_delete=models.PROTECT, default=1)
    quantidade = models.PositiveIntegerField(default=6)
    valor_abrasivo = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    finalizado = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Jogo de Abrasivo'
        verbose_name_plural = 'Jogo de Abrasivos'

    def __str__(self):
        return str(self.id)

class Set_de_Abrasivos(models.Model):
    maquina = models.ForeignKey(Maquina, on_delete=models.PROTECT)
    set_de_abrasivos = models.ManyToManyField(Jogo_de_Abrasivos, limit_choices_to={'finalizado': False})
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)    
    class Meta:
        verbose_name = 'Set de Abrasivo'
        verbose_name_plural = 'Set de Abrasivos'    
    def __str__(self):
        return str(self.id)
"""

"""
class Chp_Pol_por_Jogo_de_Abr(models.Model):
    data = models.DateField(default=timezone.now)
    maquina = models.ForeignKey(Maquina, on_delete=models.CASCADE)
    jogo_de_abrasivos = models.ForeignKey(Jogo_de_Abrasivos, on_delete=models.PROTECT, default=1)
    bloco = models.ForeignKey(Bloco, on_delete=models.PROTECT)
    cabeca = models.PositiveIntegerField(default=0)
    quantidade = models.PositiveIntegerField(default=0)
    tipo_polimento = models.ForeignKey(Tipo_Polimento, on_delete=models.PROTECT, default=1)
    velocidade = models.PositiveIntegerField(default=0)
    frequencia = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)


class Chapas_Ini_Fin(models.Model):
    polimento = models.ForeignKey(Polimento, on_delete=models.CASCADE)
    bloco = models.ForeignKey(Bloco, on_delete=models.CASCADE, default=2)
    #chapa = models.ForeignKey(Chapa, on_delete=models.CASCADE, blank=True, null=True)
    chapa = ChainedForeignKey(Chapa, on_delete=models.PROTECT,
        chained_field="bloco",
        chained_model_field="bloco",
        show_all=False,
        auto_choose=True        
        )
    chapa_inicial = models.PositiveIntegerField(default=0)
    chapa_final = models.PositiveIntegerField(default=0)
    set_de_abrasivos = models.ForeignKey(Set_de_Abrasivos, on_delete=models.PROTECT, default=1)

    # Model temporária de gastos com abrasivos
class Consumo_de_Abrasivos(models.Model):
    data = models.DateField(default=timezone.now)
    abrasivo = models.ForeignKey(Abrasivo, on_delete=models.PROTECT, default=1)
    quantidade = models.DecimalField(max_digits=10, decimal_places=3)
    unidade = models.ForeignKey(Unidade, on_delete=CASCADE)
    preco = models.DecimalField(max_digits=10, default = 0,decimal_places=2)    
    valor = models.DecimalField(max_digits=10, decimal_places=2, default=0, editable=False)

    class Meta:
        verbose_name = 'Consumo de Abrasivo'
        verbose_name_plural = 'Consumo de Abrasivos'
    def save(self, *args, **kwargs):           
        self.valor = self.quantidade * self.preco 
        self.abrasivo.valor += self.valor
        self.abrasivo.save()
        super(Consumo_de_Abrasivos, self).save(*args, **kwargs)
"""  

        
class Troca_de_jogo_de_abrasivos(models.Model):
    maquina = models.ForeignKey(Maquina, on_delete=models.PROTECT)
    cabeca = models.PositiveIntegerField(default=0, verbose_name="Cabeça")
    jogo = models.PositiveBigIntegerField(default=0)
    tipo_de_abrasivo = models.ForeignKey(Abrasivo, on_delete=models.PROTECT, default=1, verbose_name="Abrasivo")
    grao = models.PositiveIntegerField(default=0)
    mudanca_numero = models.PositiveIntegerField('Mudança/Set',default=0)
    finalizado = models.BooleanField(default=False, verbose_name="Finalizado")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'Troca de Jogo de Abrasivo'
        verbose_name_plural = 'Troca de Jogos de Abrasivos'
    
    def __str__(self):
        return str(self.id)
