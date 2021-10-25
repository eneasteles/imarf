from django.db import models
from django.contrib.auth.models import User
from datetime import date, datetime
from django.urls import reverse
from setor_pessoal.models import Cadastro_Funcionario
from bens.models import *
from controle.models import *

class OS(models.Model):
    STATUS_CHOICES = (
        ('P', 'PENDENTE'),
        ('A', 'EM ANDAMENTO'),
        ('F', 'FINALIZADA'),
    )
    os = models.AutoField(primary_key=True)
    data = models.DateField()
    data_prazo = models.DateField(auto_now_add=True)
    data_conclusao = models.DateField(auto_now_add=True, null=True, blank=True)    
    descricao = models.TextField()    
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    def __str__(self):
        return self.os 

class Diagnostico(models.Model):
    os = models.ForeignKey(OS, on_delete=models.PROTECT)
    data = models.DateField(auto_now_add=True)
    funcionario = models.ForeignKey(Cadastro_Funcionario, on_delete=models.PROTECT)
    descricao = models.TextField()
    solucao = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.os



class Equipamento(models.Model):
    os = models.ForeignKey(OS, on_delete=models.PROTECT)
    equipamento = models.ForeignKey(Bem, on_delete=models.PROTECT)
    def __str__(self):
        return self.equipamento

class VeiculoBem(models.Model):
    os = models.ForeignKey(OS, on_delete=models.PROTECT)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.PROTECT)
    def __str__(self):
        return self.veiculo
