from django.contrib import admin

# Register your models here.
from .models import Fin_tipo_documento, Recebimento, Recebimento_vencimento, Recebimento_comissao, Forma_de_pagamento
class Recebimento_vencimentoInline(admin.TabularInline):
    model = Recebimento_vencimento
    extra = 1
class Recebimento_comissaoInline(admin.TabularInline):
    model = Recebimento_comissao
    extra = 1
    autocomplete_fields = ('vendedor', )
class Forma_de_pagamentoInline(admin.TabularInline):
    model = Forma_de_pagamento
    extra = 1

@admin.register(Recebimento)
class RecebimentoAdmin(admin.ModelAdmin):
    list_display = ('pessoa', 'tipo_documento', 'referencia', 'valor', 'valor_recebido', 'saldo', 'emissao', 'status')
    list_filter = ('tipo_documento', 'status')
    search_fields = ('pessoa', 'valor','status')
    autocomplete_fields = ('pessoa', )
    inlines = [Recebimento_vencimentoInline, Recebimento_comissaoInline, Forma_de_pagamentoInline]

admin.site.register(Fin_tipo_documento)
