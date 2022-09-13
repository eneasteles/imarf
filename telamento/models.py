from django.db import models
from django.utils import timezone
from django.db.models.deletion import PROTECT

from producao.models import Bloco, Linha_Resinamento, Operador, Resina, Unidade

# Create your models here.
class Telamento(models.Model):
    linha = models.ForeignKey(Linha_Resinamento, on_delete=PROTECT)
    data = models.DateField(default=timezone.now)
    operador = models.ForeignKey(Operador, on_delete=PROTECT)
    bloco = models.ForeignKey(Bloco, on_delete=PROTECT, default=2)
    quantidade_de_chapas = models.PositiveIntegerField(default=0)
    #acabamento = models.ForeignKey(Acabamento, default=2 ,on_delete=PROTECT)    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.id) +" -- " +str(self.data)


class Telamento_item(models.Model):
    telamento = models.ForeignKey(Telamento, on_delete=PROTECT, verbose_name="Insumo")
    #bloco = models.ForeignKey(Bloco, on_delete=PROTECT)
    resina = models.ForeignKey(Resina, on_delete=PROTECT)
    #quantidade_de_chapas = models.FloatField()
    quantidade_insumo = models.FloatField(default=0)
    unidade = models.ForeignKey(Unidade, on_delete=PROTECT, default=1)
    #observacao = models.CharField(max_length=200, blank=True)
 #   usuario = models.ForeignKey(User, on_delete=PROTECT)
    def __str__(self):
        return f'{self.resina}'
