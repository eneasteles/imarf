from django.contrib import admin
from django.contrib.admin.filters import ListFilter

from . models import *

#Acabamento, Bloco, Chapa, Fio_diamantado, Insumo, Maquina, Material, Observacao_chapa, Pessoas, Serrada, Status_bloco, Status_chapa, Chapas_produzidas, Espessura, Unidade
class Chapas_produzidasinline(admin.TabularInline):
    model = Chapas_produzidas
    extra = 1

class BlocoIteminline(admin.TabularInline):
    model = BlocoItem
    extra = 1

class BlocoSerradaInline(admin.TabularInline):
    model = BlocoSerrada
    extra = 1

class BlocoAdmin(admin.ModelAdmin):
    inlines = [
        BlocoIteminline
    ]

class Resinamento_itemInline(admin.TabularInline):
    model = Resinamento_item
    extra = 1

class ResinamentoAdmin(admin.ModelAdmin):
    inlines = [
        Resinamento_itemInline
    ]
class Fio_diamantadoinline(admin.TabularInline):
    model = Fio_diamantado
    extra = 1
class FioAdmin(admin.ModelAdmin):
    inlines = [
        Fio_diamantadoinline
    ]

class DespesaIteminline(admin.TabularInline):
    model = DespesaItem
    extra = 1
class DespesaItemAdmin(admin.ModelAdmin):
    inlines = [
        DespesaIteminline
    ]

class Paradainline(admin.TabularInline):
    model = Parada
    extra = 1

class Forma_pagamento_inline(admin.TabularInline):
    model = Forma_pagamento
    extra = 1

class Pedido_venda_item_inline(admin.TabularInline):
    model = Pedido_venda_item
    extra = 1

    
class Pedido_venda_Admin(admin.ModelAdmin):    
    list_display = ('id','pessoa','data')
    list_display_links = ('id','pessoa','data')
    list_filter = ('id','pessoa')
    list_per_page = 10
    search_fields = ['id']
    inlines = [
        Pedido_venda_item_inline,
       # Forma_pagamento_inline,
    ]
class SerradaAdmin(admin.ModelAdmin):
    list_display = ('serrada','data_final', 'created')
    inlines = [
        BlocoSerradaInline,
        Chapas_produzidasinline,
        Paradainline,
        
    ]

admin.site.register(Material)
admin.site.register(Bloco, BlocoAdmin)
admin.site.register(Status_bloco)
admin.site.register(Chapa)
admin.site.register(Status_chapa)
admin.site.register(Espessura)
admin.site.register(Acabamento)
admin.site.register(Observacao_chapa)
admin.site.register(Insumo)
admin.site.register(Unidade)
admin.site.register(Maquina)     #       admin.site.register()
admin.site.register(Serrada, SerradaAdmin) #, ChapasAdmin
admin.site.register(Fio_diamantado)
admin.site.register(Pessoa)
admin.site.register(Grupo)
admin.site.register(Produto)
admin.site.register(Classe)
admin.site.register(Centro_de_Custo)
admin.site.register(Despesa, DespesaItemAdmin)
admin.site.register(Pedreira)
admin.site.register(Aplicacao)
admin.site.register(Detalhe)
admin.site.register(Qualidade)
admin.site.register(Entrada_chapa)
admin.site.register(Entrada_ladrilho)
admin.site.register(Liga)
admin.site.register(Forma_pagamento)
admin.site.register(Pedido_venda, Pedido_venda_Admin)
admin.site.register(Empresa)
admin.site.register(Status_venda)
admin.site.register(Frete)
admin.site.register(FioFatorConversao)
admin.site.register(Resinamento, ResinamentoAdmin)
admin.site.register(Mes)
admin.site.register(Setor)
admin.site.register(Folha_de_Pagamento)
admin.site.register(Faturamento)

