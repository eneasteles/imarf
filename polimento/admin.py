from producao.models import Qualidade
from polimento.models import Abrasivo, Chapas_Polidas, Parada_Politriz, Polimento, Qualidade_Polimento, Tipo_Polimento
from django.contrib import admin
from django.contrib.admin.sites import site

# Register your models here.
class ChapasPolidasInline(admin.TabularInline):    
    model = Chapas_Polidas
    extra = 1
class ParadaPolitrizInline(admin.TabularInline):
    model = Parada_Politriz
    extra = 1


class PolimentoAdmin(admin.ModelAdmin):
    ordering = ('data',)
    list_display = ('data','maquina','turno')
    inlines = [
        ChapasPolidasInline,
        ParadaPolitrizInline,
    ]

admin.site.register(Polimento, PolimentoAdmin)
admin.site.register(Abrasivo)
admin.site.register(Qualidade_Polimento)
admin.site.register(Tipo_Polimento)

