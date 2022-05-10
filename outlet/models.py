from django.db import models
from estoque.models import *
from producao.models import *

# Create your models here.
class Produto_de_Venda(models.Model):
    material = models.ForeignKey(Material, on_delete=PROTECT)
    tipo = models.ForeignKey(Tipo_Produto, on_delete=PROTECT)
    acabamento = models.ForeignKey(Acabamento, on_delete=PROTECT)
    qualidade = models.CharField(max_length=10, null=True, blank=True)
    observacao = models.CharField(max_length=100, null=True, blank=True)
    identificacao = models.CharField(max_length=50, null=True, blank=True)
    localizacao = models.CharField(max_length=50, null=True, blank=True)
    quantidade = models.FloatField(default=1)
    vendido = models.FloatField(default=0)    
    unidade = models.ForeignKey(Un, on_delete=PROTECT)
    comprimento = DecimalField(max_digits=6, decimal_places=3)
    altura_espessura = DecimalField(max_digits=6, decimal_places=3)
    largura = DecimalField(max_digits=6, decimal_places=3)
    preco = models.FloatField() 
    exportacao = models.BooleanField(default=False)   
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, editable = False)
