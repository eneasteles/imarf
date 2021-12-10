from django.db import models
from estoque.models import *
from producao.models import *
from django.utils import timezone



# Create your models here.
class Tipo_Produto(models.Model):
    tipo = models.CharField(max_length=50, primary_key=True)
    def __str__(self):
        return self.tipo

class Estoque(models.Model):
    material = models.ForeignKey(Material, on_delete=PROTECT)
    tipo = models.ForeignKey(Tipo_Produto, on_delete=PROTECT)
    #acabamento = models.ForeignKey(Acabamento, on_delete=PROTECT)
    qualidade = models.ForeignKey(Qualidade, on_delete=PROTECT)
    #detalhe = models.ForeignKey(Detalhe, on_delete=PROTECT)
    quantidade = models.FloatField()
    unidade = models.ForeignKey(Un, on_delete=PROTECT)
    comprimento = DecimalField(max_digits=6, decimal_places=3)
    altura_espessura = DecimalField(max_digits=6, decimal_places=3)
    largura = DecimalField(max_digits=6, decimal_places=3)
    preco = models.FloatField()    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.material)

class Classe_do_Item(models.Model):
    classe_do_item = models.CharField(max_length=50, primary_key=True)
    def __str__(self):
        return self.classe_do_item
class Grupo_do_Item(models.Model):
    grupo_do_item = models.CharField(max_length=50, primary_key=True)
    def __str__(self):
        return self.grupo_do_item

class Item(models.Model):
    item = models.CharField(max_length=100)
    #classe_do_item = models.ManyToManyField(Classe_do_Item)
    classe_do_item = models.ForeignKey(Classe_do_Item, on_delete=PROTECT)
    grupo_do_item = models.ForeignKey(Grupo_do_Item, on_delete=PROTECT)
    def __str__(self):
        return self.item

class Item_valor(models.Model):
    item = models.ForeignKey(Item, on_delete=PROTECT)
    unidade = models.ForeignKey(Unidade, on_delete=PROTECT)
    valor = models.FloatField(default=0)
    data_ultima_compra = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


"""
class Emp(models.Model):
    empresa = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14, null=True, blank=True)

    def __str__(self):
        return str(self.empresa)
"""

class Git(models.Model):
    grupo = models.CharField(max_length=100)

    def __str__(self):
        return str(self.grupo)



class Cla(models.Model):
    classe = models.CharField(max_length=100)

    def __str__(self):
        return self.classe

class Uni(models.Model):
    unidade = models.CharField(max_length=100, primary_key=True)
    descricao = models.CharField(max_length=100)
    fator = models.FloatField()

    def __str__(self):
        return self.unidade



class Pro(models.Model):
    nome = models.CharField(max_length=150)
    apelido = models.CharField(max_length=150, blank=True, null=True)
    empresa = models.ForeignKey(Empresa, on_delete=PROTECT)
    grupo = models.ForeignKey(Git, on_delete=PROTECT, blank=True, null=True)
    classe = models.ForeignKey(Cla, on_delete=PROTECT, blank=True, null=True)
    unidade = models.CharField(max_length=50, null=True, blank=True)
    unidadeentrada = models.CharField(max_length=50, null=True, blank=True)
    fatorconversao = models.FloatField(default=0)
    inativo = models.IntegerField(default=0)
    valor = models.FloatField(default=0)
    saldo = models.FloatField(default=0)
    fornecedor = models.ForeignKey(Pessoa, on_delete=PROTECT, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        #return self.nome
        return '{}  -->> Saldo: {}'.format(self.nome, self.saldo)


class Apl(models.Model):
    aplicacao = models.CharField(max_length=100)

    def __str__(self):
        return self.aplicacao

class Req(models.Model): 
    STATUS_CHOICES = (
        ('P', 'PENDENTE'),
        ('A', 'ATENDIDO'),
        ('C', 'CANCELADO'),
    )
    item = models.ForeignKey(Pro, on_delete=PROTECT)
    aplicacao = models.ForeignKey(Apl, on_delete=PROTECT)
    quantidade = models.FloatField(default=0)
    unidade = models.ForeignKey(Uni, on_delete=PROTECT)    
    data = models.DateField(default=timezone.now)
    #empresa = models.ForeignKey(Apl, on_delete=PROTECT, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    status = models.CharField(max_length=1, default='P', choices=STATUS_CHOICES, editable = False)    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, editable = False)

    def __str__(self):
        return str(self.item)
        
