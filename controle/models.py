from datetime import date, datetime
from django.conf.urls import url
from django.contrib.admin.sites import DefaultAdminSite
from django.db import models
from django.db.models.deletion import CASCADE, PROTECT
from django.db.models.fields import CharField, DecimalField
from django.db.models.fields.related import ForeignKey
from django.http import request
from django.utils.regex_helper import Group
from django.utils import timezone
from django.utils.tree import Node
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.conf import settings
from producao.models import *
from bens.models import *
#from caixa.models import Filial

class Aplicacao(models.Model):
    aplicacao = models.CharField(max_length=50)
    def __str__(self):
        return self.aplicacao
    class Meta:
        verbose_name = 'Aplicaçao'
        verbose_name_plural = 'Aplicaçao'

  

class Movimentacao(models.Model):    
    data = models.DateField()
    veiculo = models.ForeignKey(Veiculo, on_delete=PROTECT)
    origem = models.CharField(max_length=100, null=True, blank=True)
    destino = models.CharField(max_length=100, null=True, blank=True)
    hora_saida = models.TimeField(null=True, blank=True)
    hora_chegada = models.TimeField(null=True, blank=True)
    leitura_inicial = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    leitura_final = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    missao = models.CharField(max_length=200, null=True, blank=True)    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, editable = False)

    def __str__(self):
        return str(self.data)
    class Meta:
        verbose_name = 'Movimentacao de Veículos'
        verbose_name_plural = 'Movimentacao de Veículos'

    def save(self, *args, **kwargs): 
           
        self.total = self.leitura_final - self.leitura_inicial       
        super(Movimentacao, self).save(*args, **kwargs)

    

