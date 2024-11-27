from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.admin.filters import ListFilter

from . models import *
from resinagem.models import *

admin.site.site_header = 'SISTEMA DE CONTROLE DE PRODUÇÃO - IMARF'
admin.site.site_title = 'PRODUÇÃO'
admin.site.index_title = 'PCP IMARF'

#Acabamento, Bloco, Chapa, Fio_diamantado, Insumo, Maquina, Material, Observacao_chapa, Pessoas, Serrada, Status_bloco, Status_chapa, Chapas_produzidas, Espessura, Unidade
class Chapas_produzidasinline(admin.TabularInline):
    autocomplete_fields = ['bloco']
    model = Chapas_produzidas
    extra = 1

class BlocoIteminline(admin.TabularInline):    
    model = BlocoItem
    extra = 1


@admin.register(Bloco)
class BlocoAdmin(admin.ModelAdmin):
    #def get_queryset(self, request):
    ##    qs = super().get_queryset(request)
    #    if request.user.is_superuser:
    #        return qs
    #    return qs.filter(usuario_id=request.user)
    
    ordering = ('bloco',)
    list_filter = ('status','tipo','material')
    list_display = ('id','bloco','material','tipo','comprimento','altura','largura','status','data')
    #list_editable = ('comprimento','altura','largura','status')
    
    search_fields = ('blobo__bloco',)
    inlines = [
        BlocoIteminline
    ]

class ProducaoPedreiraInline(admin.TabularInline):
    model = Producao_Pedreira
    extra = 1
@admin.register(Custos_Pedreira)
class CustoPedreiraAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(usuario_id=request.user)
    
    list_display = ('pedreira','ano','mes', 'valor')
    inlines = [
        ProducaoPedreiraInline
    ]

class Resina_ValorInline(admin.TabularInline):
    model = Resina_Valor
    extra = 1

@admin.register(Resina)
class ResinaAdmin(admin.ModelAdmin):
    list_display = ('resina','dados_tecnicos')
    search_fields = ('resina',)
    inlines = [
        Resina_ValorInline
    ]
class Resinamento_chapaInline(admin.TabularInline):    
    model = Resinamento_chapa
    extra = 1

class Resinamento_itemInline(admin.TabularInline):    
    model = Resinamento_item
    extra = 1

class Tela_chapa_Inline(admin.TabularInline):    
    model = Tela_chapa
    extra = 1

    
class Resinamento_Insumo_Inline(admin.TabularInline):
    model = Resinamento_Insumo
    extra = 1
"""class Resinamento_Bloco_Inline(admin.TabularInline):
    model = Resinamento_Bloco
    extra = 1
    inlines = [
        Resinamento_Insumo_Inline,
    ]
"""

class ParadaResinamentoinline(admin.TabularInline):
    model = Parada_Resinamento
    extra = 0
class ResinamentoAdmin(admin.ModelAdmin):
    search_fields = ('id',)
    list_display = ('data','linha','bloco','quantidade_de_chapas','id')
    autocomplete_fields = ('bloco',)
    inlines = [
        Resinamento_itemInline,
        Resinamento_chapaInline,  
 #       Tela_chapa_Inline,     
        ParadaResinamentoinline,
        
    ]
class Fio_diamantadoinline(admin.TabularInline):
    model = Fio_diamantado
    extra = 1
class FioAdmin(admin.ModelAdmin):
    inlines = [
        Fio_diamantadoinline
    ]

#admin.site.register(Fio_diamantado)
@admin.register(Fio_diamantado)
class FioAdmin(admin.ModelAdmin):
    list_display = ('jogo_fio','maquina','espessura_fio','referencia','nome','status_fio','liga','garantia')

@admin.register(FioFatorConversao)
class FioFatorConversaoadmin(admin.ModelAdmin):
    model = FioFatorConversao
    extra = 1
    list_display = ('maquina', 'fornecedor', 'dureza', 'fator')
    search_fields = ('maquina', 'fornecedor')
#admin.site.register(FioFatorConversao)
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

class LigaFatorConversaoinline(admin.TabularInline):
    model = LigaFatorConversao
    extra = 1
@admin.register(Liga)    
class LigaAdmin(admin.ModelAdmin):
    inlines = [
        LigaFatorConversaoinline
    ]
    
        
class Forma_pagamento_inline(admin.TabularInline):
    model = Forma_pagamento
    extra = 1

class Pedido_venda_item_inline(admin.TabularInline):
    model = Pedido_venda_item
    extra = 1
    readonly_fields=('valor', )
"""
@admin.register(Pedido_venda)    
class Pedido_venda_Admin(admin.ModelAdmin): 
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user_id=request.user)   
    list_display = ('id','pessoa','data')
    list_display_links = ('id','pessoa','data')
 #   list_filter = ('id','pessoa')
    list_per_page = 10
    search_fields = ['id']
    inlines = [
        Pedido_venda_item_inline,
       # Forma_pagamento_inline,
    ]

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
            obj.save()
        super(Pedido_venda_Admin, self).save_model(request, obj, form, change)
"""


@admin.register(Serrada)
class SerradaAdmin(admin.ModelAdmin):
    search_fields = ('serrada', )
    list_filter = ['maquina', ]
    list_display = ('serrada','maquina', 'bloco_da_serrada','bloco_da_serrada_last','created') 
    
    inlines = [
        Chapas_produzidasinline,
        Paradainline,        
    ]
    def bloco_da_serrada(self, obj):
        return obj.chapas_produzidas_set.first().bloco
    bloco_da_serrada.short_description = 'Bloco'
    bloco_da_serrada.admin_order_field = 'chapas_produzidas__bloco'
    def bloco_da_serrada_last(self, obj):
        return obj.chapas_produzidas_set.last().bloco
    bloco_da_serrada_last.short_description = 'Último_Bloco'
    bloco_da_serrada_last.admin_order_field = 'chapas_produzidas__bloco'
    
@admin.register(Faturamento)
class FaturamentoAdmin(admin.ModelAdmin):
    list_display = ('ano','mes', 'empresa', 'valor_interno','valor_externo')
    ordering =('ano','mes', 'empresa',)

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    search_fields = ('nome',)
   

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    ordering = ('material',)
    list_display = ('material','dureza','pedreira')
    search_fields = ('material',)

@admin.register(Pedreira)
class PedreiraAdmin(admin.ModelAdmin):
    ordering = ('pedreira',)
    list_display = ('pedreira',)
    search_fields = ('pedreira',)

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    ordering = ('empresa',)
    list_display = ('empresa',)
    search_fields = ('empresa',)

#admin.site.register(Bloco, BlocoAdmin)
admin.site.register(Status_bloco)

admin.site.register(Status_chapa)
admin.site.register(Espessura)
admin.site.register(Acabamento)
admin.site.register(Observacao_chapa)
admin.site.register(Insumo)
admin.site.register(Unidade)
admin.site.register(Un)
admin.site.register(Maquina)     #       admin.site.register()
#admin.site.register(Serrada, SerradaAdmin) #, ChapasAdmin


admin.site.register(Grupo)
admin.site.register(Produto)
admin.site.register(Classe)
admin.site.register(Centro_de_Custo)
admin.site.register(Despesa, DespesaItemAdmin)

admin.site.register(Aplicacao)
admin.site.register(Detalhe)
admin.site.register(Qualidade)
admin.site.register(Entrada_chapa)
admin.site.register(Entrada_ladrilho)
#admin.site.register(Liga, LigaAdmin)
admin.site.register(Forma_pagamento)
#admin.site.register(Pedido_venda, Pedido_venda_Admin)

admin.site.register(Status_venda)
admin.site.register(Frete)

admin.site.register(Resinamento, ResinamentoAdmin)
admin.site.register(Resinagem)
admin.site.register(Operador)
admin.site.register(Setor)
admin.site.register(Folha_de_Pagamento)
admin.site.register(Cavalete)
admin.site.register(Status_Cavalete)
#admin.site.register(Faturamento,FaturamentoAdmin)

#admin.site.register(Custos_Pedreira, CustoPedreiraAdmin)
admin.site.register(Linha_Resinamento)


