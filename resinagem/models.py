from django.db import models
from django.utils import timezone
from django.db.models.fields import CharField
from producao.models import Operador, Bloco, Acabamento, Resina, Unidade_de_Medida, Unidade
from django.db.models.deletion import PROTECT
from almoxarifado.models import Item_de_Almoxarifado

# Create your models here.
# substituindo  resina pelo item de estoque
# substituindo  Valor_resina pelo item de estoque 

class Linha_Resinagem(models.Model):
    linha = CharField(max_length=15)
    def __str__(self):
        return str(self.linha)

class Resinagem(models.Model):
    linha = models.ForeignKey(Linha_Resinagem, on_delete=PROTECT)
    data = models.DateField(default=timezone.now)
    operador = models.ForeignKey(Operador, on_delete=PROTECT)
    bloco = models.ForeignKey(Bloco, on_delete=PROTECT, default=2)
    quantidade_de_chapas = models.PositiveIntegerField(default=0)
    acabamento = models.ForeignKey(Acabamento, default=2 ,on_delete=PROTECT)    
    observacao = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.id) +" -- " +str(self.data)

class Insumo(models.Model):
    resina = models.ForeignKey(Item_de_Almoxarifado, on_delete=PROTECT)
    unidade = models.ForeignKey(Unidade_de_Medida, on_delete=PROTECT)
    quantidade = models.FloatField()
    valor = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

class Chapas_resinadas(models.Model):
    resinagem = models.ForeignKey(Resinagem, on_delete=PROTECT, verbose_name="Chapa número") 
    chapa_inicial= models.IntegerField()
    chapa_final = models.IntegerField()

class Resinagem_item(models.Model):
    resinagem = models.ForeignKey(Resinagem, on_delete=PROTECT, verbose_name="Insumo")
    resina = models.ForeignKey(Item_de_Almoxarifado, on_delete=PROTECT)
    #quantidade_de_chapas = models.FloatField()
    quantidade = models.FloatField(default=0)
    preco = models.FloatField(default=0)
    unidade = models.ForeignKey(Unidade_de_Medida, on_delete=PROTECT, default=1)
    frequencia = models.PositiveIntegerField(default=1) 
    #observacao = models.CharField(max_length=200, blank=True)
 #   usuario = models.ForeignKey(User, on_delete=PROTECT)
    def __str__(self):
        return f'{self.resina}'

class Resinagem_tela_chapa(models.Model):
    resinagem = models.ForeignKey(Resinagem, on_delete=PROTECT, verbose_name="Chapa número")
    chapa_inicial= models.IntegerField()
    chapa_final = models.IntegerField()
    resina = models.ForeignKey(Item_de_Almoxarifado, on_delete=PROTECT, default=3, verbose_name="Tela")
    quantidade_insumo = models.FloatField(default=0)
    unidade = models.ForeignKey(Unidade, on_delete=PROTECT, default='M')

    def __str__(self):
        return f'{self.resinagem}'


