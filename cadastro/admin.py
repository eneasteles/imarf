from django.contrib import admin
from .models import Adm_empresa

@admin.register(Adm_empresa)
class Adm_empresaAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'cnpj', 'ie', 'im')
    search_fields = ('empresa', 'cnpj', 'ie', 'im')