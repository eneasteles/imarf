from django.db import models
from django.contrib.auth.models import User
from datetime import date, datetime
from django.urls import reverse
from setor_pessoal.models import Cadastro_Funcionario
from bens.models import *
from controle.models import *
from datetime import date, datetime
from django.utils import timezone
from estoque.models import *

class OS(models.Model):
    STATUS_CHOICES = (
        ('P', 'PENDENTE'),
        ('A', 'EM ANDAMENTO'),
        ('F', 'FINALIZADA'),
    )
    os = models.AutoField(primary_key=True)
    data = models.DateField(default=timezone.now)
    valor = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    data_prazo = models.DateField(auto_now_add=True)
    data_conclusao = models.DateField(auto_now_add=True, null=True, blank=True)    
    descricao = models.TextField()    
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    def __str__(self):
        return str(self.os) 

class Diagnostico(models.Model):
    os = models.ForeignKey(OS, on_delete=models.PROTECT)
    funcionario = models.ForeignKey(Cadastro_Funcionario, on_delete=models.PROTECT)
    descricao = models.TextField()
    solucao = models.TextField(null=True, blank=True)


class OSVeiculo(models.Model):
    os = models.ForeignKey(OS, on_delete=models.PROTECT)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.PROTECT)

class Equipamento(models.Model):
    os = models.ForeignKey(OS, on_delete=models.PROTECT)
    equipamento = models.ForeignKey(Bem, on_delete=models.PROTECT)

class OS_Item(models.Model):
    os = models.ForeignKey(OS, on_delete=models.PROTECT)
    item = models.ForeignKey(Item, on_delete=models.PROTECT)
    quantidade = models.IntegerField()
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'
    def save(self, *args, **kwargs): 
           
        self.valor_total = self.quantidade * self.valor_unitario       
       
        self.os.valor += self.valor_total
        self.os.save()
        super(OS_Item, self).save(*args, **kwargs)




