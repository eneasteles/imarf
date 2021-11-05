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
    list_display = ('item', 'classe_do_item',  'grupo_do_item')
    inlines = [Item_valor_inline,]

admin.site.register(Tipo_Produto)

admin.site.register(Classe_do_Item)
admin.site.register(Grupo_do_Item)

