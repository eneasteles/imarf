from django.contrib.auth.models import User
from django.db import models
from datetime import date, datetime, timezone
from producao.models import *

# Create your models here.
from django.db import models
#from caixa.models import Filial

# Create your models here.

class Veiculo(models.Model):
    veiculo = models.CharField(max_length=100)
    placa = models.CharField(max_length=7)  
    ano = models.IntegerField()
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    cor = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50,default='.')
    #filial = models.ForeignKey(Filial, on_delete=PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, editable = False)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.veiculo + ' - ' + self.placa
    class Meta:
        verbose_name = 'Veículo'
        verbose_name_plural = 'Veículos'

class Bem(models.Model):
    bem = models.CharField(max_length=100)    
    marca = models.CharField(max_length=50, blank=True, null=True)
    modelo = models.CharField(max_length=50, blank=True, null=True)
    ano = models.IntegerField(blank=True, null=True)
    serial = models.CharField(max_length=100, blank=True, null=True)
    descricao = models.TextField()
    #Filial = models.ForeignKey(Filial, on_delete=models.CASCADE, blank=True, null=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, blank=True, null=True)
    garantia = models.DateField(auto_now=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.bem
