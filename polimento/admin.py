from producao.models import Qualidade
from polimento.models import * #Abrasivo, Chp_Pol_por_Jogo_de_Abr, Jogo_de_Abrasivos, Parada_Politriz, Polimento, Qualidade, Tipo_Polimento, Chapas_Ini_Fin, polimento_chapas_ini_fin_jogo_abrasivos
from django.contrib import admin
from django.contrib.admin.sites import site
from django.db.models import Q
from .models import Polimento, Jogo_de_Abrasivos, Chapas_Ini_Fin


class Chapas_Ini_FinInline(admin.TabularInline):    
    model = Chapas_Ini_Fin
    extra = 1
    autocomplete_fields = ('bloco',)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "jogo_abrasivos":
            # Verifica se o inline está sendo editado (existem instâncias de Chapas_Ini_Fin)
            if hasattr(self, 'parent_model') and hasattr(request, 'obj'):
                chapas_ini_fin_id = request.obj.id

                # Consulta os IDs relacionados usando a tabela intermediária
                from django.db import connection
                with connection.cursor() as cursor:
                    cursor.execute("""
                        SELECT jogo_de_abrasivos_id 
                        FROM polimento_chapas_ini_fin_jogo_abrasivos 
                        WHERE chapas_ini_fin_id = %s
                    """, [chapas_ini_fin_id])
                    selecionados_ids = [row[0] for row in cursor.fetchall()]

                # Filtrar o queryset baseado na condição desejada
                kwargs["queryset"] = Jogo_de_Abrasivos.objects.filter(
                    Q(finalizado=False) | Q(id__in=selecionados_ids)
                )
            else:
                # Caso seja um novo objeto, exibir apenas itens não finalizados
                kwargs["queryset"] = Jogo_de_Abrasivos.objects.filter(finalizado=False)
    
        return super().formfield_for_manytomany(db_field, request, **kwargs)




class ParadaPolitrizInline(admin.TabularInline):
    model = Parada_Politriz
    extra = 1


@admin.register(Polimento)
class PolimentoAdmin(admin.ModelAdmin):
    ordering = ('data',)
    list_display = ('id', 'maquina', 'bloco', 'acabamento', 'qualidade', 'data')
    inlines = [
        Chapas_Ini_FinInline,  # Usar o inline com a lógica de filtragem ajustada
        ParadaPolitrizInline,
    ]

admin.site.register(Abrasivo)
admin.site.register(Qualidade)
admin.site.register(Tipo_Polimento)
admin.site.register(Jogo_de_Abrasivos)
#admin.site.register(Set_de_Abrasivos)


@admin.register(Consumo_de_Abrasivos)
class Consumo_de_AbrasivosAdmin(admin.ModelAdmin):
    list_display= ('data','abrasivo','quantidade','unidade','preco','valor',)
    list_filter = ('abrasivo',)

@admin.register(Set_de_Abrasivos)
class SetDeAbrasivosAdmin(admin.ModelAdmin):
    list_display = ('id', 'maquina', 'created', 'modified', 'get_abrasivos')
    search_fields = ('maquina__nome', 'set_de_abrasivos__nome')  # Ajuste o campo relacionado
    list_filter = ('created', 'modified')
    
    def get_abrasivos(self, obj):
        return ", ".join([str(abrasivo) for abrasivo in obj.set_de_abrasivos.all()])
    
    get_abrasivos.short_description = 'Abrasivos'
