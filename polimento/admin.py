from producao.models import Qualidade
from polimento.models import Abrasivo, Chp_Pol_por_Jogo_de_Abr, Jogo_de_Abrasivos, Parada_Politriz, Polimento, Qualidade, Tipo_Polimento, Chapas_Ini_Fin
from django.contrib import admin
from django.contrib.admin.sites import site

# Register your models here.

class Chapas_Ini_FinInline(admin.TabularInline):    
    model = Chapas_Ini_Fin
    extra = 1

class ParadaPolitrizInline(admin.TabularInline):
    model = Parada_Politriz
    extra = 1


class Chp_Pol_por_Jogo_de_AbrInline(admin.TabularInline):
    autocomplete_fields = ('bloco',)
    model = Chp_Pol_por_Jogo_de_Abr
    extra = 1
@admin.register(Polimento)
class PolimentoAdmin(admin.ModelAdmin):
    ordering = ('data',)
    list_display = ('id','maquina','bloco','acabamento','qualidade', 'data')
    inlines = [
        Chapas_Ini_FinInline,
        ParadaPolitrizInline,
        #Jogo_de_AbrasivoInline,
        
    ]


admin.site.register(Abrasivo)
admin.site.register(Qualidade)
admin.site.register(Tipo_Polimento)

@admin.register(Jogo_de_Abrasivos)
class Jogo_de_AbrasivosAdmin(admin.ModelAdmin):
    list_filter = ('finalizado',)    
    inlines = [Chp_Pol_por_Jogo_de_AbrInline,]



