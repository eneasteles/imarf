from django.contrib import admin
from custos_gerais.models import Item_de_Producao,Custos_Gerais,Custos_Gerais_Itens

class Custos_Gerais_ItensInline(admin.TabularInline):
    model = Custos_Gerais_Itens
    extra = 1

class Custos_GeraisAdmin(admin.ModelAdmin):
    list_display = ('ano', 'mes', 'producao_m2')
    inlines = [
        Custos_Gerais_ItensInline
        ]
# Register your models here.

admin.site.register(Item_de_Producao)
admin.site.register(Custos_Gerais, Custos_GeraisAdmin)
#admin.site.register(Custos_Gerais_Itens)
