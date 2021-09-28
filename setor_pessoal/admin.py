from setor_pessoal.models import Cadastro_Funcionario
from django.contrib import admin

@admin.register(Cadastro_Funcionario)
class Cadastro_FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'Centro_de_Custo', 'folha')
    search_fields = ('nome', 'cpf', 'Centro_de_Custo')
    list_filter = ( 'cpf', 'Centro_de_Custo')
    list_editable = ('cpf','Centro_de_Custo','folha',)

