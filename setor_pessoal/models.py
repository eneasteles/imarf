from django.db import models
from django.db.models.fields import CharField
from producao.models import Centro_de_Custo, Empresa

# Create your models here.


class Cadastro_Funcionario(models.Model):
    nome = models.CharField(max_length=100)    
    cpf = models.CharField(max_length=15, blank=True, null=True)
    #Empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, default=12)
    centro_de_custo = models.ForeignKey(Centro_de_Custo, on_delete=models.CASCADE, default=4)   
    ativo = models.BooleanField(default=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_alteracao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

