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
"""
class Qualidade_Polimento(models.Model):
    qualidade = models.CharField(max_length=100)
    def __str__(self):
        return self.qualidade
"""


class Polimento(models.Model):
    data = models.DateField(default=timezone.now)
    turno = models.PositiveIntegerField(default=1)
    #Operador = models.ForeignKey(Operador, on_delete=models.CASCADE)
    operador = models.ForeignKey(Operador, on_delete=models.CASCADE, default=3)
    maquina = models.ForeignKey(Maquina, on_delete=models.CASCADE)
    horimetro_inicial = models.FloatField(default=0)
    horimetro_final = models.FloatField(default=0)
    #############################################
    bloco = models.ForeignKey(Bloco, on_delete=models.CASCADE)
    # morreu --quantidade = models.PositiveIntegerField(default=0)
    acabamento = models.ForeignKey(Acabamento, on_delete=models.PROTECT, default=2)
    # substituído --tipo_polimento = models.ForeignKey(Tipo_Polimento, on_delete=models.PROTECT, default=1, verbose_name="Acabamento")
    chapas_quebradas = models.PositiveIntegerField(default=0)
    chapas_trincadas = models.PositiveIntegerField(default=0)
    velocidade = models.PositiveIntegerField(default=0)
    qualidade = models.ForeignKey(Qualidade, on_delete=models.PROTECT)    
    frequencia = models.PositiveIntegerField(default=1)
    finalizado = models.BooleanField(default=False)
    #################################################
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.data.strftime('%d/%m/%Y')
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
class Chapas_Polidas(models.Model):
    polimento_id = models.ForeignKey(Polimento, on_delete=models.CASCADE,default=1)
    bloco = models.ForeignKey(Bloco, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=0)
    acabamento = models.ForeignKey(Acabamento, on_delete=models.PROTECT, default=1)
    tipo_polimento = models.ForeignKey(Tipo_Polimento, on_delete=models.PROTECT, default=1, verbose_name="Acabamento")
    chapas_quebradas = models.PositiveIntegerField(default=0)
    chapas_trincadas = models.PositiveIntegerField(default=0)
    velocidade = models.PositiveIntegerField(default=0)
    qualidade = models.ForeignKey(Qualidade_Polimento, on_delete=models.PROTECT)    
    frequencia = models.PositiveIntegerField(default=1)
    finalizado = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
"""





class Jogo_de_Abrasivos(models.Model):
    #polimento_id = models.ForeignKey(Polimento, on_delete=models.PROTECT,default=1)
    abrasivo = models.ForeignKey(Abrasivo, on_delete=models.PROTECT, default=1)
    quantidade = models.PositiveIntegerField(default=6)
    #cabeca = models.PositiveIntegerField(default=0)
    #pausado = models.BooleanField(default=False)
    valor_abrasivo = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    #data = models.DateField(default=timezone.now)
    finalizado = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

class Chp_Pol_por_Jogo_de_Abr(models.Model):
    data = models.DateField(default=timezone.now)
    maquina = models.ForeignKey(Maquina, on_delete=models.CASCADE)
    jogo_de_abrasivos = models.ForeignKey(Jogo_de_Abrasivos, on_delete=models.PROTECT, default=1)
    bloco = models.ForeignKey(Bloco, on_delete=models.PROTECT)
    cabeca = models.PositiveIntegerField(default=0)
    quantidade = models.PositiveIntegerField(default=0)
    #acabamento = models.ForeignKey(Acabamento, default=2 ,on_delete=PROTECT)
    tipo_polimento = models.ForeignKey(Tipo_Polimento, on_delete=models.PROTECT, default=1)
    velocidade = models.PositiveIntegerField(default=0)
    #qualidade = models.ForeignKey(Qualidade_Polimento, on_delete=models.PROTECT)
    frequencia = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)


################################
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
    jogo_abrasivos = models.ManyToManyField(Jogo_de_Abrasivos, limit_choices_to={'finalizado': False})
##########################    
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
