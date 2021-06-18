from datetime import date
from django.contrib.admin.sites import DefaultAdminSite
from django.db import models
from django.db.models.deletion import CASCADE, PROTECT
from django.db.models.fields import CharField, DecimalField
from django.db.models.fields.related import ForeignKey
from django.utils.regex_helper import Group
from django.utils import timezone
from django.utils.tree import Node
#from django_pgviews import view as pg

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    cnpjcpf = models.CharField(max_length=14)

    def __str__(self):
        return self.nome

class Material(models.Model):
    material = models.CharField(max_length=100)
    dureza = models.IntegerField(default= True) 
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.material

class Status_bloco(models.Model):
    status = models.CharField(max_length=15)

    def __str__(self):
        return self.status

class Bloco(models.Model):
    TIPO_CHOICES = (
        ('A','PRIMEIRA'),
        ('B','SEGUNDA LINHA')
    )
    bloco = models.CharField(max_length=15)
    material = models.ForeignKey(Material, on_delete=models.CASCADE) 
    tipo = models.CharField(max_length=1, default='A', choices=TIPO_CHOICES)   
    comprimento = models.DecimalField(max_digits=6, decimal_places=3, default=0) 
    altura = models.DecimalField(max_digits=6, decimal_places=3, default=0) 
    largura = models.DecimalField(max_digits=6, decimal_places=3, default=0) 
    status = models.ForeignKey(Status_bloco, on_delete=models.CASCADE) 
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.bloco

class Espessura(models.Model):
    espessura = models.DecimalField(max_digits=6, decimal_places=3, default=0.02, primary_key=True)

    def __str__(self):
        return str(self.espessura)


class Status_chapa(models.Model):
    status = models.CharField(max_length=20, primary_key=True)

    def __str__(self):
        return self.status

class Acabamento(models.Model):
    acabamento = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.acabamento

class Observacao_chapa(models.Model):
    observacao_chapa = models.CharField(max_length=100)

    def __str__(self):
        return self.observacao_chapa

class Chapa(models.Model):
    chapa = models.IntegerField()
    bloco = models.ForeignKey(Bloco, on_delete=models.CASCADE)
    acabamento = models.ForeignKey(Acabamento, on_delete=CASCADE)
    espessura = models.ForeignKey(Espessura, on_delete=models.CASCADE)
    observacao_chapa = models.ForeignKey(Observacao_chapa, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.chapa)

class Insumo(models.Model):
    insumo = models.CharField(max_length=100)

    def __str__(self):
        return str(self.insumo)

class Unidade(models.Model):
    unidade = models.CharField(max_length=20)
    fator = models.DecimalField(max_digits=10, decimal_places=3, default=1)
    descricao_unidade = models.CharField(max_length=100, default='')

    def __str__(self):
        return str(self.unidade)

class Maquina(models.Model):
    maquina = models.CharField(max_length=100)
    lacada = models.FloatField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.maquina)

  

class Liga(models.Model):
    liga = models.CharField(max_length=25)
    
    def __str__(self):
        return str(self.liga)

class Fio_diamantado(models.Model):
    jogo_fio= models.IntegerField(primary_key=True)
    maquina = models.ForeignKey(Maquina, on_delete=CASCADE)
    espessura_fio = models.DecimalField(max_digits=6, decimal_places=3)
    referencia = models.CharField(max_length=50)
    nome = models.ForeignKey(Pessoa, on_delete=CASCADE)
    nota_fiscal = models.IntegerField()
    status_fio = models.CharField(max_length=1,default='A', choices=(('A','ATIVO'),('F','FINALIZADO')))
    valor_metro_fio = models.FloatField()
    liga = models.ForeignKey(Liga, on_delete=CASCADE)
    quantidade_fio = models.IntegerField(default=0)
    comprimento_fio = models.FloatField(default=0)
    garantia = models.FloatField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    


    def __str__(self):
        return str(self.jogo_fio)

class Centro_de_Custo(models.Model):
    centro_de_custo = models.CharField(max_length=100)

    def __str__(self):
        return str(self.centro_de_custo)
class Serrada(models.Model):
    serrada = models.IntegerField()
    bloco = models.ForeignKey(Bloco, on_delete=models.CASCADE)
    comprimento = models.DecimalField(max_digits=6, decimal_places=3, default=0) 
    altura = models.DecimalField(max_digits=6, decimal_places=3, default=0) 
    largura = models.DecimalField(max_digits=6, decimal_places=3, default=0) 
    data_inicial = models.DateTimeField()
    data_final = models.DateTimeField()
    maquina = models.ForeignKey(Maquina, on_delete=CASCADE)
    horimetro_inicial = models.IntegerField()
    horimetro_final = models.IntegerField()
    amperagem_max = models.DecimalField(max_digits=8, decimal_places=3)
    espessura_fio_inicial = models.DecimalField(max_digits=6, decimal_places=3, default=0)
    espessura_fio_final = models.DecimalField(max_digits=6, decimal_places=3, default=0)
    qtde_fios = models.IntegerField()
    observacoes = models.TextField()
    periferica = models.DecimalField(max_digits=5, decimal_places=3)
    cala = models.IntegerField(default=10)
    velocidade = models.FloatField(default=0)
    jogo_fio = models.ForeignKey(Fio_diamantado, on_delete=CASCADE)
    consumo_kwh = models.DecimalField(max_digits=7, decimal_places=3, default=0)
    centro_de_custo = models.ForeignKey(Centro_de_Custo, on_delete=CASCADE,default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.serrada)

class BlocoSerrada(models.Model):
    serrada = ForeignKey(Serrada, on_delete=CASCADE)
    bloco = models.ForeignKey(Bloco, on_delete=models.CASCADE)
    comprimento = models.DecimalField(max_digits=6, decimal_places=3, default=0) 
    altura = models.DecimalField(max_digits=6, decimal_places=3, default=0) 
    largura = models.DecimalField(max_digits=6, decimal_places=3, default=0) 
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.bloco)

class Chapas_produzidas(models.Model):
    serrada = models.ForeignKey(Serrada, on_delete=models.CASCADE)
    bloco = models.ForeignKey(Bloco, on_delete=models.CASCADE, default=21)
    quantidade = models.IntegerField()
    espessura = models.ForeignKey(Espessura, on_delete=models.CASCADE) 
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.quantidade)


class Grupo(models.Model):
    grupo = models.CharField(max_length=50)

    def __str__(self):
        return str(self.grupo)

class Classe(models.Model):
    classe = models.CharField(max_length=50)

    def __str__(self):
        return str(self.classe)

class Produto(models.Model):
    produto = models.CharField(max_length=100)
    unidade = models.ForeignKey(Unidade, on_delete=CASCADE)
    grupo = models.ForeignKey(Grupo, on_delete=CASCADE)
    classe = models.ForeignKey(Classe, on_delete=CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def  __str__(self):
        return str(self.produto)



class Pedreira(models.Model):
    pedreira = CharField(max_length=100)
    cidade = CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return str(self.pedreira)

class Aplicacao(models.Model):
    aplicacao = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.aplicacao)

class Despesa(models.Model):
    pedreira = models.ForeignKey(Pedreira, on_delete=CASCADE)
    centro_de_custo = models.ForeignKey(Centro_de_Custo, on_delete=CASCADE)
    aplicacao = models.ForeignKey(Aplicacao, on_delete=CASCADE)
    data = models.DateField()    
    valor = models.FloatField()
    descricao = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.centro_de_custo)

class DespesaItem(models.Model):
    despesa = models.ForeignKey(Despesa, on_delete=CASCADE)
    produto = models.ForeignKey(Produto, on_delete=CASCADE)
    quantidade = models.FloatField()
    unidade = models.ForeignKey(Unidade, on_delete=CASCADE)
    preco = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.produto)

class Detalhe(models.Model):
    detalhe = models.CharField(max_length=50)

    def __str__(self):
        return str(self.detalhe)

class Qualidade(models.Model):
    qualidade = models.CharField(max_length=50)

    def __str__(self):
        return str(self.qualidade)
class Estoque_ladrilho(models.Model):
    material = models.ForeignKey(Material, on_delete=CASCADE)
    acabamento = models.ForeignKey(Acabamento, on_delete=CASCADE)
    qualidade = models.ForeignKey(Qualidade, on_delete=CASCADE)
    detalhe = models.ForeignKey(Detalhe, on_delete=CASCADE)
    quantidade = models.FloatField()
    comprimento = DecimalField(max_digits=6, decimal_places=3)
    espessura = DecimalField(max_digits=6, decimal_places=3)
    largura = DecimalField(max_digits=6, decimal_places=3)
    preco = models.FloatField()    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.material)

class Entrada_ladrilho(models.Model):
    material = models.ForeignKey(Material, on_delete=CASCADE)
    acabamento = models.ForeignKey(Acabamento, on_delete=CASCADE)
    qualidade = models.ForeignKey(Qualidade, on_delete=CASCADE)
    detalhe = models.ForeignKey(Detalhe, on_delete=CASCADE)
    quantidade = models.FloatField()
    comprimento = DecimalField(max_digits=6, decimal_places=3)
    espessura = DecimalField(max_digits=6, decimal_places=3)
    largura = DecimalField(max_digits=6, decimal_places=3)
    preco = models.FloatField()    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.material)

class Estoque_chapa(models.Model):
    bloco = models.ForeignKey(Bloco, on_delete=models.CASCADE)
    acabamento = models.ForeignKey(Acabamento, on_delete=CASCADE)
    qualidade = models.ForeignKey(Qualidade, on_delete=CASCADE)
    detalhe = models.ForeignKey(Detalhe, on_delete=CASCADE)
    quantidade = models.FloatField()
    comprimento = DecimalField(max_digits=6, decimal_places=3)
    espessura = DecimalField(max_digits=6, decimal_places=3)
    largura = DecimalField(max_digits=6, decimal_places=3)
    preco = models.FloatField()    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.material)

class Entrada_chapa(models.Model):
    bloco = models.ForeignKey(Bloco, on_delete=models.CASCADE)
    acabamento = models.ForeignKey(Acabamento, on_delete=CASCADE)
    qualidade = models.ForeignKey(Qualidade, on_delete=CASCADE)
    detalhe = models.ForeignKey(Detalhe, on_delete=CASCADE)
    quantidade = models.FloatField()
    comprimento = DecimalField(max_digits=6, decimal_places=3)
    espessura = DecimalField(max_digits=6, decimal_places=3)
    largura = DecimalField(max_digits=6, decimal_places=3)
    preco = models.FloatField()    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.material)

class BlocoItem(models.Model):
    bloco = models.ForeignKey(Bloco, on_delete=CASCADE)
    produto = models.ForeignKey(Produto, on_delete=CASCADE)
    unidade = models.ForeignKey(Unidade, on_delete=CASCADE)
    quantidade = models.FloatField()
    valor = models.FloatField()
    descricao = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Parada(models.Model):
    serrada = models.ForeignKey(Serrada, on_delete=CASCADE)
    data_inicial = models.DateTimeField()
    data_final = models.DateTimeField() 
    motivo = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)



class Empresa(models.Model):
    empresa = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14)
    cep = models.CharField(max_length=6, default='60000')
    endereco = models.CharField(max_length=200)
    uf = CharField(max_length=2, default='CE')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.empresa)

class FioFatorConversao(models.Model):
    maquina = models.ForeignKey(Maquina, on_delete=CASCADE)
    fornecedor = models.ForeignKey(Pessoa, on_delete=CASCADE)
    dureza = models.IntegerField()
    fator = models.FloatField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Status_venda(models.Model):
    status_venda = CharField(max_length=25)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.status_venda)

class Forma_pagamento(models.Model):
    forma_pagamento = models.CharField(max_length=100)    
    parcelas = models.IntegerField(default=1)
    intervalo = models.IntegerField(default=0)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.forma_pagamento)

class Frete(models.Model):
    frete = models.CharField(max_length=10)

    def __str__(self):
        return str(self.frete)

class Pedido_venda(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=CASCADE, verbose_name="Cliente")
    data = models.DateField(default=timezone.now) 
    entrada = models.FloatField(default=100, verbose_name='Entrada %')
    forma_pagamento = models.ForeignKey(Forma_pagamento, on_delete=CASCADE)
    prazo_entrega = models.IntegerField(default=0)
    frete = models.ForeignKey(Frete, on_delete=CASCADE)
    status_venda = models.ForeignKey(Status_venda, on_delete=CASCADE, verbose_name="Status")
    observacao = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    #created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.pessoa)

class Pedido_venda_item(models.Model):
    pedido_venda = models.ForeignKey(Pedido_venda, on_delete=CASCADE)
    grupo = models.ForeignKey(Grupo, on_delete=CASCADE)
    material = models.ForeignKey(Material, on_delete=CASCADE)
    unidade = models.ForeignKey(Unidade,on_delete=CASCADE)
    quantidade = models.FloatField()
    altura_espessura = models.FloatField(verbose_name="Alt/Esp")
    comprimento = models.FloatField()
    largura = models.FloatField()
    acabamento = models.ForeignKey(Acabamento, on_delete=CASCADE)
    bloco = models.ForeignKey(Bloco, on_delete=CASCADE, blank=True, null=True)
    identificacao = models.CharField(max_length=20)
    percentual_ipi = models.FloatField(default=5)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    


    def __str__(self):
        return str(self.material)

class Mes(models.Model):
    mes = models.PositiveSmallIntegerField(primary_key=True)

    def __str__(self):
        return str(self.mes)


class Linha_Resinamento(models.Model):
    linha = CharField(max_length=15)

    def __str__(self):
        return str(self.linha)

class Setor(models.Model):
    setor = models.CharField(max_length=100)

    def __str__(self):
        return str(self.setor)

class Operador(models.Model):
    operador = models.CharField(max_length=100)
    setor = models.ForeignKey(Setor, on_delete=CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Resina(models.Model):
    resina = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.resina)
class Resinamento(models.Model):
    linha = models.ForeignKey(Linha_Resinamento, on_delete=CASCADE)
    ano = models.IntegerField()
    mes = models.ForeignKey(Mes, on_delete=CASCADE)
    operador = models.ForeignKey(Operador, on_delete=CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.ano)
class Resinamento_item(models.Model):
    resinamento_id = ForeignKey(Resinamento, on_delete=CASCADE)
    bloco = models.ForeignKey(Bloco, on_delete=CASCADE)
    resina = models.ForeignKey(Resina, on_delete=CASCADE)
    quantidade = models.FloatField()
    observacao = models.CharField(max_length=200)


class Faturamento(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=CASCADE)
    ano = models.IntegerField()
    mes = models.ForeignKey(Mes, on_delete=CASCADE)
    mercado  = models.CharField(max_length=1,default='I', choices=(('I','INTERNO'),('E','EXTERNO')))
    valor = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.ano)


        
"""
VIEW_SQL = 
    SELECT * FROM public.vw_serrada
"""

"""
class Vw_serrada(pg.View):
    serrada = models.IntegerField(primary_key=True)
    bloco = models.CharField(max_length=15)
    maquina = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    comprimento = models.DecimalField(max_digits=6, decimal_places=3, default=0) 
    altura = models.DecimalField(max_digits=6, decimal_places=3, default=0) 
    largura = models.DecimalField(max_digits=6, decimal_places=3, default=0) 
    qtde_fios = models.IntegerField()
    jogo_fio = models.IntegerField()    
    m3_liq = models.DecimalField(max_digits=15, decimal_places=3, default=0)
    comprimento_bru = models.DecimalField(max_digits=6, decimal_places=3, default=0)
    altura_bru =models.DecimalField(max_digits=6, decimal_places=3, default=0)
    largura_br = models.DecimalField(max_digits=6, decimal_places=3, default=0)
    m3_bru = models.DecimalField(max_digits=15, decimal_places=3, default=0)
    m3_perda = models.DecimalField(max_digits=15, decimal_places=3, default=0)
    prd_fio_m2  = models.DecimalField(max_digits=15, decimal_places=3, default=0)
    m2  = models.DecimalField(max_digits=15, decimal_places=3, default=0)
    dureza = models.IntegerField(default= True)
    fator = models.FloatField(default=1)
    jogo_fio = models.IntegerField()
    qtde_fios = models.IntegerField()
    qtde_chapas  = models.IntegerField()
    garantia_fio  = models.DecimalField(max_digits=15, decimal_places=3, default=0)
    custo_fio_por_m2  = models.DecimalField(max_digits=15, decimal_places=3, default=0)
    garantia_fio  = models.DecimalField(max_digits=15, decimal_places=3, default=0)
    custo_bloco = models.DecimalField(max_digits=15, decimal_places=3, default=0)
    folha = models.FloatField()
    mes = models.IntegerField(default=0)
    ano = models.IntegerField(default=0)
    custo_m2 = models.FloatField()

   # material = models.ForeignKey(Material, on_delete=models.CASCADE)

    sql = VIEW_SQL

    class Meta:
      managed = False
      db_table = 'vw_serrada'
"""
class Folha_de_Pagamento(models.Model):
    centro_de_custo = models.ForeignKey(Centro_de_Custo, on_delete=Node, default=1)
    ano = models.IntegerField(default=timezone.now().year)
    mes = models.ForeignKey(Mes, on_delete=CASCADE)
    qtde_funcionarios = models.IntegerField()
    folha = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.mes)





