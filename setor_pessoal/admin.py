from setor_pessoal.models import *
from django.contrib import admin

admin.site.register(Funcao)

@admin.register(Cadastro_Funcionario)
class Cadastro_FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'centro_de_custo',)
    search_fields = ('nome', 'cpf', )
    list_filter = ('centro_de_custo',)
    #list_editable = ('cpf','folha','outros','centro_de_custo',)

