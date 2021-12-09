from estoque.models import Estoque, Tipo_Produto
from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Estoque)
class EstoqueAdmin(admin.ModelAdmin):
    list_display = ('material', 'tipo', 'qualidade','unidade', 'quantidade', 'comprimento', 'altura_espessura','largura','preco')
    list_filter = ( 'material', 'tipo')
    

class Item_valor_inline(admin.TabularInline):
    model = Item_valor
    extra = 1

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('item',  'grupo_do_item','classe_do_item')
    inlines = [Item_valor_inline,]
    #autocomplete_fields = ['classe_do_item']

@admin.register(Pro)
class ProAdmin(admin.ModelAdmin):
    ordering = ('nome',)
    list_display = ('nome', 'apelido','saldo','classe','grupo')
    list_filter = ('classe','grupo')
    search_fields = ('nome', 'apelido')

@admin.register(Req)    
class ReqAdmin(admin.ModelAdmin):    
    list_display = ('item', 'aplicacao','quantidade','unidade','data')
    list_filter = ('status',)


admin.site.register(Tipo_Produto)

admin.site.register(Classe_do_Item)
admin.site.register(Grupo_do_Item)
admin.site.register(Apl)
#admin.site.register(Req)
#admin.site.register(Git)

