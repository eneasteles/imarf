from django.utils import timezone
from django.db import models
from django.db.models.deletion import PROTECT

from producao.models import Bloco, Operador, Resina, Unidade

# Create your models here.
class Envelopamento(models.Model):
    data = models.DateField(default=timezone.now)
    operador = models.ForeignKey(Operador, on_delete=PROTECT)
    bloco = models.ForeignKey(Bloco, on_delete=PROTECT, default=2)
    observacao = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.id) +" -- " +str(self.data)

class Envelopamento_item(models.Model):
    envelopamento = models.ForeignKey(Envelopamento, on_delete=PROTECT, verbose_name="Insumo")
    resina = models.ForeignKey(Resina, on_delete=PROTECT)
    quantidade_insumo = models.FloatField(default=0)
    unidade = models.ForeignKey(Unidade, on_delete=PROTECT, default=1)
 #   usuario = models.ForeignKey(User, on_delete=PROTECT)
    def __str__(self):
        return f'{self.resina}'
