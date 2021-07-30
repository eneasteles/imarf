from django.db import models
from producao.models import *

# Create your models here.
class Item_de_Producao(models.Model):
    id = models.AutoField(primary_key=True)
    item_de_producao = models.CharField(max_length=100)
    def __str__(self):
        return self.item_de_producao

class Custos_Gerais(models.Model):
    id = models.AutoField(primary_key=True)    
    ano = models.IntegerField(default=timezone.now().year)
    mes = models.IntegerField(choices=MES_CHOICES)
    producao_m2 = models.FloatField()    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.ano) + ' - ' + str(self.mes)

class Custos_Gerais_Itens(models.Model):
    custos_gerais = models.ForeignKey(Custos_Gerais, on_delete=PROTECT)
    item_de_producao = models.ForeignKey(Material, on_delete=PROTECT)
    valor = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
