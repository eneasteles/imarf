from django.utils import timezone
from django.db import models
from producao.models import Pessoa, Empresa
from cadastro.models import Adm_empresa
from django.contrib.auth.models import User

class Fin_tipo_documento(models.Model):
    documento = models.CharField(max_length=100)
    def __str__(self):
        return self.documento
 
class Recebimento(models.Model):
    empresa = models.ForeignKey(Adm_empresa, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    tipo_documento = models.ForeignKey(Fin_tipo_documento, on_delete=models.CASCADE)
    referencia = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    valor_recebido = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    observacao = models.TextField(blank=True, null=True)
    emissao = models.DateField(default=timezone.now)
    modo_de_lancamento = models.CharField(max_length=1, default='M', choices=(('A', 'Automático'), ('M', 'Manual')))
    status = models.CharField(max_length=1, default='A', choices=(('A', 'Aberto'), ('P', 'Pago'), ('C', 'Cancelado')))
    user = models.ForeignKey(User, on_delete=models.PROTECT, editable=False)

    def __str__(self):
        return self.pessoa.nome
    
    class Meta:
        verbose_name = 'Contas a Receber'
        verbose_name_plural = 'Recebimentos'
    def save(self, *args, **kwargs):
        self.saldo = self.valor - self.valor_recebido
        #self.save()
        super(Recebimento, self).save(*args, **kwargs)

    
class Recebimento_vencimento(models.Model):
    recebimento = models.ForeignKey(Recebimento, on_delete=models.CASCADE)
    parcela = models.IntegerField(default=1)
    vencimento = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    valor_recebido = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    observacao = models.TextField(blank=True, null=True)
    emissao = models.DateField(default=timezone.now)
    data_pagamento = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=1, default='A', choices=(('A', 'Aberto'), ('P', 'Pago'), ('C', 'Cancelado')))
    


    def __str__(self):
        return self.recebimento.pessoa.nome
    
class Recebimento_comissao(models.Model):
    recebimento = models.ForeignKey(Recebimento, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    percentual = models.DecimalField(max_digits=5, decimal_places=2)
    valor = models.DecimalField(max_digits=10, decimal_places=2, default=0, editable=False)
    status = models.CharField(max_length=1, default='A', choices=(('A', 'Aberto'), ('P', 'Pago'), ('C', 'Cancelado')))


    def __str__(self):
        return self.recebimento.pessoa.nome
    
class Forma_de_pagamento(models.Model):
    recebimento = models.ForeignKey(Recebimento, on_delete=models.CASCADE)

    numero_da_parcelas = models.IntegerField(default=1)
    quantidade_de_dias = models.IntegerField(default=0)
    percentual_da_parcela = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return str(self.numero_da_parcelas)

class Pagamento_comissao(models.Model):
    recebimento_comissao = models.ForeignKey(Recebimento, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    data_pagamento = models.DateField(default=timezone.now)

    def __str__(self):
        return str(self.recebimento_comissao_id)
