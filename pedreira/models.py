from datetime import timezone, datetime
from django.db import models
from django.db.models.deletion import CASCADE, PROTECT
from django.contrib.auth.models import User
from bens.models import Bem
from estoque.models import Item


from producao.models import Centro_de_Custo, Empresa, Unidade, Pedreira, Material

class Lancamento(models.Model):    
    data = models.DateField(default=datetime.now)
    empresa = models.ForeignKey(Empresa, on_delete=PROTECT)
    centro_de_custo = models.ForeignKey(Centro_de_Custo, on_delete=PROTECT, null=True, blank=True)
    pedreira = models.ForeignKey(Pedreira, on_delete=PROTECT, default=19)
    material = models.ForeignKey(Material, on_delete=models.PROTECT, default=18) 
    valor = models.DecimalField(max_digits=10, decimal_places=2, default=0, editable=False)
    descricao = models.CharField(max_length=100, blank=True, null=True) 
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, editable = False)

    def __str__(self):
        return str(self.data)
    class Meta:
        verbose_name = 'Lancamento de Custos'
        verbose_name_plural = 'Custos'

class Lancamento_Item(models.Model):
    lancamento = models.ForeignKey(Lancamento, on_delete=CASCADE)
    item = models.ForeignKey(Item, on_delete=CASCADE)
    descricao = models.CharField(max_length=100, blank=True, null=True)
    bem = models.ForeignKey(Bem, on_delete=PROTECT, null=True, blank=True)
    quantidade = models.DecimalField(max_digits=10, decimal_places=3)
    preco = models.DecimalField(max_digits=10, default = 0,decimal_places=2)
    unidade = models.ForeignKey(Unidade, on_delete=CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    leitura = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    caixa = models.BooleanField(default=False)
    

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Itens do Custo'
    def save(self, *args, **kwargs):           
        self.valor = self.quantidade * self.preco 
        self.lancamento.valor += self.valor
        self.lancamento.save()
        super(Lancamento_Item, self).save(*args, **kwargs)

class Producao_pedreira_m3(models.Model):
    ano = models.IntegerField(default=datetime.now().year)
    mes = models.IntegerField(default=datetime.now().month)
    empresa = models.ForeignKey(Empresa, on_delete=PROTECT)
    pedreira = models.ForeignKey(Pedreira, on_delete=PROTECT, null=True, blank=True)
    material = models.ForeignKey(Material, on_delete=models.PROTECT) 
    m3 = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, editable = False)

    def __str__(self):
        return str(self.ano)+'/'+str(self.mes)+' - '+str(self.material)+' - '+str(self.m3)+' m3'
    class Meta:
        verbose_name = 'Lancamento de Produção'
        verbose_name_plural = 'Produção M3'


