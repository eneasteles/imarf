from django.db import models
from producao.models import *
from polimento.models import *

# Create your models here.

class Chapa(models.Model):
    bloco = models.ForeignKey(Bloco, on_delete=models.PROTECT)
    chapa_numero = models.IntegerField(default=0)
    comprimento_bruto = models.DecimalField(max_digits=6, decimal_places=2)
    altura_bruto = models.DecimalField(max_digits=6, decimal_places=2)
    espessura = models.DecimalField(max_digits=6, decimal_places=2)
    comprimento_liquido = models.DecimalField(max_digits=6, decimal_places=2)
    altura_liquida = models.DecimalField(max_digits=6, decimal_places=2)
    polimento_id = models.BigIntegerField(default=0)
    acabamento = models.ForeignKey(Acabamento, on_delete=models.PROTECT)
    qualidade = models.CharField(max_length=50, null=True, blank=True)
    cavalete = models.CharField(max_length=50, null=True, blank=True)
    packing_list = models.BigIntegerField(default=0)
    localizacao = models.CharField(max_length=50, null=True, blank=True)
    valor_m2 = models.DecimalField(max_digits=10, decimal_places=2)
    observacao = models.TextField(max_length=300, null=True, blank=True)
    exportacao = models.BooleanField(default=False)
    status_chapa = models.ForeignKey(Status_chapa, on_delete=models.PROTECT, default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['bloco', 'chapa_numero',]

    def __str__(self):
        return  str(self.chapa_numero) + ' Bloco ' + str(self.bloco.bloco)
