from django.utils import timezone
from django.db import models

class Ata(models.Model):
    data_reuniao = models.DateField(default=timezone.now)
    tema = models.CharField(max_length=100)
    status = models.CharField(max_length=1, default='A', choices=(('A', 'Ativo'), ('I', 'Inativo')))    
    def __str__(self):
        return str(self.data_reuniao)
    
class Ata_item(models.Model):
    ata = models.ForeignKey(Ata, on_delete=models.CASCADE)
    item = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=1, default='A', choices=(('A', 'Ativo'), ('I', 'Inativo')))
    executado = models.CharField(max_length=1, default='N', choices=(('S', 'Sim'), ('N', 'Não')))
    responsavel = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.item
    
class Ata_item_pessoa(models.Model):
    ata = models.ForeignKey(Ata, on_delete=models.CASCADE)
    pessoa = models.CharField(max_length=100)
    status = models.CharField(max_length=1, default='A', choices=(('A', 'Ativo'), ('I', 'Inativo')))
    
    def __str__(self):
        return self.pessoa
