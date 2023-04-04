from django.db import models
#from caixa.models import Filial

# Create your models here.
class Adm_empresa(models.Model):
    empresa = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14, blank=True, null=True)
    ie = models.CharField(max_length=20, blank=True, null=True)
    im = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.empresa
