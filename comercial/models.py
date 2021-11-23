from django.db import models
from django.contrib.auth.models import User
from datetime import date, datetime
from django.utils.html import format_html
from django.urls import reverse
from setor_pessoal.models import Cadastro_Funcionario
from bens.models import *
from controle.models import *
from datetime import date, datetime
from django.utils import timezone
from estoque.models import *
from producao.models import *
from outlet.models import *

class OSComercial(models.Model):
    STATUS_CHOICES = (
        ('P', 'PENDENTE'),
        ('A', 'EM ANDAMENTO'),
        ('F', 'FINALIZADA'),
    )
    os = models.AutoField(primary_key=True)
    data = models.DateField(default=timezone.now)
    metragem = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    data_prazo = models.DateField(auto_now_add=True)
    data_conclusao = models.DateField(auto_now_add=True, null=True, blank=True)    
    descricao = models.TextField()    
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    def __str__(self):
        return str(self.os)
    class Meta:
        verbose_name = 'OS'
        verbose_name_plural = 'OS' 

class OS_Comercial_Item(models.Model):
    os = models.ForeignKey(OSComercial, on_delete=models.PROTECT)
    material = models.ForeignKey(Material, on_delete=models.PROTECT)
    acabamento = models.ForeignKey(Acabamento, on_delete=PROTECT)
    quantidade = models.IntegerField()
    comprimento = models.DecimalField(max_digits=6, decimal_places=3, default=0) 
    altura = models.DecimalField(max_digits=6, decimal_places=3, default=0) 
    largura = models.DecimalField(max_digits=6, decimal_places=3, default=0)
    metragem = models.DecimalField(max_digits=10, decimal_places=3, default=0) 
    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'
    def save(self, *args, **kwargs):            
        self.metragem = self.quantidade * self.comprimento * self.altura * self.largura 
        self.os.metragem += self.metragem
        self.os.save()
        super(OS_Comercial_Item, self).save(*args, **kwargs)



# Pedido de Venda
class Status_da_venda(models.Model):
    status_da_venda = CharField(max_length=25)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.status_da_venda)





class Pedido_de_venda(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=PROTECT)
    pessoa = models.ForeignKey(Pessoa, on_delete=PROTECT, verbose_name="Cliente")
    data = models.DateField(default=timezone.now) 
    total = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    entrada = models.FloatField(default=100, verbose_name='Entrada %')
    forma_pagamento = models.ForeignKey(Forma_pagamento, on_delete=PROTECT)
    prazo_entrega = models.IntegerField(default=0)
    frete = models.ForeignKey(Frete, on_delete=PROTECT)
    status_venda = models.ForeignKey(Status_venda, on_delete=PROTECT, verbose_name="Status")
    observacao = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, editable = False)

    def full_url(self):
        url = 'https://www.ebttecnologia.com/scriptcase/app/imarf/grid_public_outlet_view/?nmgp_outra_jan=true&nmgp_start=SC&5216'
        from django.utils.html import format_html
        return format_html("<a href='%s'>%s</a>" % (url, url))

    def __str__(self):
        return str(f'{self.pessoa} {self.total} {self.data}')

    #def save(self, *args, **kwargs):
    #    pdtotal = Pedido_venda_item.objects.all().values()
    #    self.total = pdtotal['quantidade'] * pdtotal['preco'] * pdtotal['comprimento'] * pdtotal['largura']
    #    if pdtotal['percentual_ipi'] > 0:
    #        pdtotal['valor'] += pdtotal['valor']*(pdtotal['percentual_ipi']/100)
    #    self.save()
    #    super(Pedido_venda, self).save(*args, **kwargs)

class Pedido_de_venda_item(models.Model):
    pedido_de_venda = models.ForeignKey(Pedido_de_venda, on_delete=PROTECT)
    grupo = models.ForeignKey(Grupo, on_delete=PROTECT)
    material = models.ForeignKey(Material, on_delete=PROTECT)
    un = models.ForeignKey(Un,on_delete=PROTECT, default='M2')
    quantidade = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    preco = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    altura_espessura = models.DecimalField(max_digits=10, decimal_places=3, default=0, verbose_name="Alt/Esp")
    comprimento =  models.DecimalField(max_digits=10, decimal_places=3, default=0)
    largura =  models.DecimalField(max_digits=10, decimal_places=3, default=0)    
    acabamento = models.ForeignKey(Acabamento, on_delete=PROTECT)
    metragem = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    bloco = models.ForeignKey(Bloco, on_delete=PROTECT, blank=True, null=True)
    #identificacao = models.CharField(max_length=20, null=True)
    percentual_ipi = models.DecimalField(max_digits=6, decimal_places=3, default=5) 
    valor = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, editable = False)
    outlet = models.IntegerField(blank=True, null=True, editable = False, default=0)
    

    def __str__(self):
        return "ID:"+str(self.id)
    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Itens do Pedido'
    def save(self, *args, **kwargs): 
           
        if str(self.un) == 'M2':
            self.valor = self.quantidade * self.preco * self.comprimento * self.largura
            self.metragem = self.quantidade * self.comprimento * self.largura
        elif str(self.un) == 'M3':            
            self.valor = self.quantidade * self.preco * self.altura_espessura * self.comprimento * self.largura
            self.metragem = self.quantidade * self.altura_espessura * self.comprimento * self.largura
        else:
            self.valor = self.quantidade * self.preco
            self.metragem = self.quantidade        
        if self.percentual_ipi>0:
            self.valor += self.valor*(self.percentual_ipi/100)        
        self.pedido_de_venda.total += self.valor
        self.pedido_de_venda.save()
        super(Pedido_de_venda_item, self).save(*args, **kwargs)

class Pedido_de_venda_outlet(models.Model):
    pedido_de_venda = models.ForeignKey(Pedido_de_venda, on_delete=PROTECT)
    #produto_de_venda = models.ForeignKey(Produto_de_Venda, on_delete=PROTECT)
    lote = models.IntegerField()    
    quantidade = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.lote)
class Forma_de_pagamento(models.Model):
    pedido = models.ForeignKey(Pedido_de_venda, on_delete=models.PROTECT)
    #parcelas = models.IntegerField(default=1)
    prazo = models.IntegerField(default=0)
    percentual = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    valor = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True)
