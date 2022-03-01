from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Jogo_de_Disco)
class Jogo_de_DiscoAdmin(admin.ModelAdmin):
    list_display = ('id', 'referencia', 'numero_de_dentes', 'diametro', 'espessura', 'quantidade', 'valor_unitario')
    search_fields = ('id', )

class Chapas_Cortadas_inline(admin.TabularInline):
    model = Chapas_Cortadas
    extra = 1
    autocomplete_fields = ('bloco_id','jogo_de_disco_id')


@admin.register(Corte)
class CorteAdmin(admin.ModelAdmin):
    list_display = ('id', 'maquina_id', 'jogo_de_disco_id', 'data')
    search_fields = ('maquina_id', 'jogo_de_disco_id')

    inlines = [Chapas_Cortadas_inline,] 