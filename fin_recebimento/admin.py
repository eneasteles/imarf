from django.contrib import admin

# Register your models here.
from .models import Fin_tipo_documento, Recebimento, Recebimento_vencimento, Recebimento_comissao, Forma_de_pagamento

@admin.register(Recebimento)
class RecebimentoAdmin(admin.ModelAdmin):
    list_display = ('pessoa', 'tipo_documento', 'referencia', 'valor', 'valor_recebido', 'saldo', 'emissao', 'status')
    list_filter = ('tipo_documento', 'status')
    search_fields = ('pessoa', 'valor','status')

admin.site.register(Fin_tipo_documento)
