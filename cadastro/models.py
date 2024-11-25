from django.contrib.auth.models import User
from django.db import models


class Adm_empresa(models.Model):
    empresa = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14, blank=True, null=True)
    ie = models.CharField(max_length=20, blank=True, null=True)
    im = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.empresa


class UserEnterprise(models.Model):
    user = models.ManyToManyField(User, verbose_name="Usuário")
    enterprise = models.ForeignKey(Adm_empresa, on_delete=models.CASCADE, verbose_name="Empresa")

    def __str__(self):
        return f"{self.enterprise} - {', '.join(user.username for user in self.user.all())}"
