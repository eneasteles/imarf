from datetime import date, datetime
from django.conf.urls import url
from django.contrib.admin.sites import DefaultAdminSite, site
from django.db import models
from django.db.models.deletion import CASCADE, PROTECT
from django.db.models.fields import CharField, DecimalField
from django.db.models.fields.related import ForeignKey
from django.utils.regex_helper import Group
from django.utils import timezone
from django.utils.tree import Node
from django.contrib.auth.models import User
from serraria.models import *
from producao.models import *
from django.contrib.admin import admin

#from django_pgviews import view as pg

MES_CHOICES = (
        (1,'JANEIRO'),
        (2,'FEVEREIRO'),
        (3,'MARÇO'),
        (4,'ABRIL'),
        (5,'MAIO'),
        (6,'JUNHO'),
        (7,'JULHO'),
        (8,'AGOSTO'),
        (9,'SETEMBRO'),
        (10,'OUTUBRO'),
        (11,'NOVEMBRO'),
        (12,'DEZEMBRO')
    )

class StatusBloco(models.Model):
    status = models.CharField(max_length=15)

    def __str__(self):
        return self.status

class Blocos(models.Model):
    TIPO_CHOICES = (
        ('A','PRIMEIRA'),
        ('B','SEGUNDA LINHA')
    )
    bloco = models.CharField(max_length=15)
    material = models.ForeignKey(Material, on_delete=models.PROTECT) 
    tipo = models.CharField(max_length=1, default='A', choices=TIPO_CHOICES)   
    comprimento = models.DecimalField(max_digits=6, decimal_places=3, default=0) 
    altura = models.DecimalField(max_digits=6, decimal_places=3, default=0) 
    largura = models.DecimalField(max_digits=6, decimal_places=3, default=0) 
    status = models.ForeignKey(Status_bloco, on_delete=models.PROTECT) 
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, default=3, on_delete=PROTECT)



    def __str__(self):
        return self.bloco

class BlocosItems(models.Model):
    bloco = models.ForeignKey(Bloco, on_delete=PROTECT)
    produto = models.ForeignKey(Produto, on_delete=PROTECT)
    unidade = models.ForeignKey(Unidade, on_delete=PROTECT)
    quantidade = models.FloatField()
    valor = models.FloatField()
    descricao = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)