from estoque.models import Estoque, Tipo_Produto
from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Estoque)
class EstoqueAdmin(admin.ModelAdmin):
    list_display = ('material', 'tipo',  'acabamento','qualidade','detalhe','unidade', 'quantidade', 'comprimento', 'altura_espessura','largura','preco')
    list_filter = ( 'material', 'tipo')

admin.site.register(Tipo_Produto)
admin.site.register(Item)
admin.site.register(Classe_do_Item)
admin.site.register(Grupo_do_Item)

