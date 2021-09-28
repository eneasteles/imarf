from setor_pessoal.models import Cadastro_Funcionario
from django.contrib import admin

@admin.register(Cadastro_Funcionario)
class Cadastro_FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf',  'folha','outros','Centro_de_Custo',)
    search_fields = ('nome', 'cpf', )
    list_filter = ( 'cpf', 'Centro_de_Custo')
    list_editable = ('cpf','folha','outros','Centro_de_Custo',)

