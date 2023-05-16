from django.db import models

from producao.models import Empresa, Pessoa

# Create your models here.

"""
   
class Servico(models.Model):
    servico = models.CharField(max_length=150)
    descricao = models.TextField()

    def __str__(self):
        return self.servico

class Contrato(models.Model):    
    autorizado = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    entrada = models.DecimalField(max_digits=10, decimal_places=2)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    dia_vencimento = models.IntegerField(default=10)
    recorrente = models.BooleanField(default=True)
    objeto = models.TextField()
    contratante = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    contratado = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)    
    ativo = models.BooleanField(default=True)
    observacao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.objeto
     
    """