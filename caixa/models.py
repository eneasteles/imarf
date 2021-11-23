from datetime import date, datetime
from django.conf.urls import url
from django.contrib.admin.sites import DefaultAdminSite
from django.db import models
from django.db.models.deletion import CASCADE, PROTECT
from django.db.models.fields import CharField, DecimalField
from django.http import request
from django.utils.regex_helper import Group
from django.utils import timezone
from django.utils.tree import Node
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.conf import settings
from producao.models import *
from estoque.models import *
from bens.models import *


"""
class Aplicacao(models.Model):
    aplicacao = models.CharField(max_length=50)
    def __str__(self):
        return self.aplicacao
    class Meta:
        verbose_name = 'Aplicaçao'
        verbose_name_plural = 'Aplicaçao'

class Filial(models.Model):
    filial = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    responsavel = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, editable = False)

    def __str__(self):
        return self.filial
    class Meta:
        verbose_name = 'Filial'
        verbose_name_plural = 'Filiais'        
"""



    
NATUREZA_CHOICES = (
        ('E', 'ENTRADA'),
        ('S', 'SAIDA'),
    )
class Caixa(models.Model):    
    data = models.DateField(default=timezone.now)
    empresa = models.ForeignKey(Empresa, on_delete=PROTECT)
    #filial = models.ForeignKey(Filial, on_delete=PROTECT)
    #os = models.ForeignKey(OS, on_delete=PROTECT, null=True, blank=True)    
    natureza = models.CharField(max_length=1, default='S', choices=NATUREZA_CHOICES)
    valor = models.DecimalField(max_digits=10, decimal_places=2, default=0, editable=False)
    descricao = models.CharField(max_length=100, blank=True, null=True) 
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, editable = False)

    def full_url(self):
        url = 'https://www.ebttecnologia.com/scriptcase/app/imarf/grid_public_caixa_view/'
        from django.utils.html import format_html
        return format_html("<a href='%s'>%s</a>" % (url, url))

    def __str__(self):
        return str(self.data)
    class Meta:
        verbose_name = 'Caixa'
        verbose_name_plural = 'Caixa'

class Caixa_Item(models.Model):
    caixa = models.ForeignKey(Caixa, on_delete=CASCADE)
    item = models.ForeignKey(Item, on_delete=CASCADE)
    #aplicacao = models.ForeignKey(Aplicacao, default=1, on_delete=PROTECT)
    veiculo = models.ForeignKey(Veiculo, on_delete=PROTECT, null=True, blank=True)
    bem = models.ForeignKey(Bem, on_delete=PROTECT, null=True, blank=True)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    preco = models.DecimalField(max_digits=10, default = 0,decimal_places=4)
    unidade = models.ForeignKey(Unidade, on_delete=CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    leitura = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Itens do Caixa'
    def save(self, *args, **kwargs): 
           
        self.valor = self.quantidade * self.preco       
       
        self.caixa.valor += self.valor
        self.caixa.save()
        super(Caixa_Item, self).save(*args, **kwargs)

    
