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





