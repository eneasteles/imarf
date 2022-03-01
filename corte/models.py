from django.db import models
from datetime import datetime, date
from django.utils import timezone
from producao.models import Maquina, Bloco    

class Jogo_de_Disco(models.Model):
    data = models.DateField(default=timezone.now)
    referencia = models.CharField(max_length=30, null=True, blank=True)
    numero_de_dentes = models.IntegerField(default=0)
    diametro = models.DecimalField(max_digits=5, decimal_places=2)
    espessura = models.DecimalField(max_digits=5, decimal_places=2)
    quantidade = models.IntegerField(default=5)
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    

    def __str__(self):
        return self.referencia

class Corte(models.Model):
    maquina_id = models.ForeignKey(Maquina, on_delete=models.PROTECT)
    jogo_de_disco_id = models.ForeignKey(Jogo_de_Disco, on_delete=models.PROTECT)
    data = models.DateField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.data.strftime('%d/%m/%Y')

class Chapas_Cortadas(models.Model):
    corte_id = models.ForeignKey(Corte, on_delete=models.PROTECT, default=1)
    bloco_id = models.ForeignKey(Bloco, on_delete=models.PROTECT)
    jogo_de_disco_id = models.ForeignKey(Jogo_de_Disco, on_delete=models.PROTECT)
    quantidade = models.IntegerField(default=0)
    quantidade_de_ladrilho = models.IntegerField(default=0)
    dimensao_x = models.DecimalField(max_digits=5, decimal_places=2)
    dimensao_y = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)