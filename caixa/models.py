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
from django.conf import settings
from producao.models import *
from estoque.models import *

class Aplicacao(models.Model):
    aplicacao = models.CharField(max_length=50)
    def __str__(self):
        return self.aplicacao

class Filial(models.Model):
    filial = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    responsavel = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.filial
    
NATUREZA_CHOICES = (
        ('E', 'ENTRADA'),
        ('S', 'SAIDA'),
    )
class Caixa(models.Model):    
    data = models.DateField(default=timezone.now)
    empresa = models.ForeignKey(Empresa, on_delete=PROTECT)
    filial = models.ForeignKey(Filial, on_delete=PROTECT)    
    natureza = models.CharField(max_length=1, default='S', choices=NATUREZA_CHOICES)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.CharField(max_length=100, blank=True, null=True) 
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User,  on_delete=PROTECT)

    def __str__(self):
        return str(self.data)

class Caixa_Item(models.Model):
    caixa = models.ForeignKey(Caixa, on_delete=CASCADE)
    item = models.ForeignKey(Item, on_delete=CASCADE)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    unidade = models.ForeignKey(Unidade, on_delete=CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    aplicacao = models.ForeignKey(Aplicacao, default=1, on_delete=PROTECT)
    