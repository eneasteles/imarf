from django.db import models
from setor.models import Setor

# Create your models here.

class Unidade_de_Medida(models.Model):
    unidade = models.CharField(max_length=20, primary_key=True)
    fator = models.FloatField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.unidade}'

class Item_de_Almoxarifado(models.Model):
    item = models.CharField(max_length=200)
    unidade = models.ForeignKey(Unidade_de_Medida, on_delete=models.CASCADE)
    quantidade = models.FloatField(default=0)
    valor = models.FloatField(default=0)
    grupo = models.ForeignKey('Grupo_Almoxarifado', on_delete=models.CASCADE)
    classe = models.ForeignKey('Classe_Almoxarifado', on_delete=models.CASCADE)
    categoria = models.ForeignKey('Categoria_Almoxarifado', on_delete=models.CASCADE)
    #setor = models.ForeignKey(Setor, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.item}'

class Grupo_Almoxarifado(models.Model):
    grupo = models.CharField(max_length=100, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.grupo}'

class Classe_Almoxarifado(models.Model):
    classe = models.CharField(max_length=100, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.classe}'

class Categoria_Almoxarifado(models.Model):
    categoria = models.CharField(max_length=100, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.categoria}'