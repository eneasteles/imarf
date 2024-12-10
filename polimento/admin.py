from producao.models import Qualidade
from polimento.models import * #Abrasivo, Chp_Pol_por_Jogo_de_Abr, Jogo_de_Abrasivos, Parada_Politriz, Polimento, Qualidade, Tipo_Polimento, Chapas_Ini_Fin, polimento_chapas_ini_fin_jogo_abrasivos
from django.contrib import admin
from django.contrib.admin.sites import site
from django.db.models import Q
from .models import *
from django.contrib.admin.widgets import FilteredSelectMultiple
from django import forms
"""
class SetDeAbrasivosForm(forms.ModelForm):
    class Meta:
        model = Set_de_Abrasivos
        fields = '__all__'



class Chapas_Ini_FinInline(admin.TabularInline):    
    model = Chapas_Ini_Fin
    extra = 1
    autocomplete_fields = ('bloco',)


"""    




class ParadaPolitrizInline(admin.TabularInline):
    model = Parada_Politriz
    extra = 1

class Chapas_PolidasInline(admin.TabularInline):
    model = Chapas_Polidas
    extra = 1
    
@admin.register(Polimento)
class PolimentoAdmin(admin.ModelAdmin):
    ordering = ('data',)
    list_display = ('id', 'maquina',  'data')
    inlines = [
        Chapas_PolidasInline,
        ParadaPolitrizInline,
    ]

admin.site.register(Abrasivo)
admin.site.register(Qualidade)
admin.site.register(Tipo_Polimento)

"""
@admin.register(Jogo_de_Abrasivos)
class JogoDeAbrasivosAdmin(admin.ModelAdmin):
    list_display = ('id','abrasivo', 'finalizado', 'created', 'updated')
    list_filter = ('finalizado',)
    ordering = ('id',)

@admin.register(Consumo_de_Abrasivos)
class Consumo_de_AbrasivosAdmin(admin.ModelAdmin):
    list_display= ('data','abrasivo','quantidade','unidade','preco','valor',)
    list_filter = ('abrasivo',)



@admin.register(Set_de_Abrasivos)
class SetDeAbrasivosAdmin(admin.ModelAdmin):
    list_display = ('id', 'maquina', 'get_jogo_de_abrasivos', 'created', 'modified')
    search_fields = ('maquina__nome', 'set_de_abrasivos__nome')  # Ajuste o campo relacionado
    list_filter = ('created', 'modified')
    class Meta:
        verbose_name = "Set de Abrasivos"
    
    def get_jogo_de_abrasivos(self, obj):
        return ", ".join([str(jogo) for jogo in obj.set_de_abrasivos.all()])
    
    get_jogo_de_abrasivos.short_description = 'Jogo de Abrasivos'
"""    
@admin.register(Troca_de_jogo_de_abrasivos)
class TrocaDeJogoDeAbrasivosAdmin(admin.ModelAdmin):
    list_display = ('id','maquina', 'cabeca', 'jogo', 'tipo_de_abrasivo', 'grao', 'mudanca_numero','finalizado',)
    list_filter = ('finalizado','maquina', 'mudanca_numero')
    list_editable = ('finalizado',)
    # This is the crucial addition to filter the queryset
    """
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(finalizado=False)
    """
    

    class Meta:
        verbose_name = "Troca de Jogo de Abrasivos"
    

