from producao.models import Qualidade
from polimento.models import * #Abrasivo, Chp_Pol_por_Jogo_de_Abr, Jogo_de_Abrasivos, Parada_Politriz, Polimento, Qualidade, Tipo_Polimento, Chapas_Ini_Fin
from django.contrib import admin
from django.contrib.admin.sites import site

# Register your models here.

class Chapas_Ini_FinInline(admin.TabularInline):    
    model = Chapas_Ini_Fin
    extra = 1
    autocomplete_fields = ('bloco',)

class ParadaPolitrizInline(admin.TabularInline):
    model = Parada_Politriz
    extra = 1


class Chp_Pol_por_Jogo_de_AbrInline(admin.TabularInline):
    autocomplete_fields = ('bloco',)
    model = Chp_Pol_por_Jogo_de_Abr
    extra = 1
@admin.register(Polimento)
class PolimentoAdmin(admin.ModelAdmin):
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "jogo_abrasivos":
            # Filtrar para exibir apenas objetos com finalizado=False e não selecionados
            kwargs["queryset"] = Jogo_de_Abrasivos.objects.filter(finalizado=False)
        return super().formfield_for_manytomany(db_field, request, **kwargs)
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
admin.site.register(Jogo_de_Abrasivos)
"""
@admin.register(Jogo_de_Abrasivos)
class Jogo_de_AbrasivosAdmin(admin.ModelAdmin):
    list_filter = ('finalizado',)    
    inlines = [Chp_Pol_por_Jogo_de_AbrInline,]
"""


@admin.register(Consumo_de_Abrasivos)
class Consumo_de_AbrasivosAdmin(admin.ModelAdmin):
    list_display= ('data','abrasivo','quantidade','unidade','preco','valor',)
    list_filter = ('abrasivo',)


