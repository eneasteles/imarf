from django.contrib import admin

# Register your models here.
from .models import *
class Recebimento_vencimentoInline(admin.TabularInline):
    model = Recebimento_vencimento
    extra = 1
class Recebimento_comissaoInline(admin.TabularInline):
    model = Recebimento_comissao
    extra = 1
    autocomplete_fields = ('vendedor', )
    readonly_fields = ('valor', 'status')
class Forma_de_pagamentoInline(admin.TabularInline):
    model = Forma_de_pagamento
    extra = 1

@admin.register(Recebimento)
class RecebimentoAdmin(admin.ModelAdmin):
    list_display = ('pessoa', 'tipo_documento', 'referencia', 'valor', 'valor_recebido', 'saldo', 'emissao', 'status')
    list_filter = ('tipo_documento', 'status')
    search_fields = ('pessoa', 'valor','status')
    autocomplete_fields = ('pessoa', )
    readonly_fields = ( 'saldo', 'user')
    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
            obj.save()
        super(RecebimentoAdmin, self).save_model(request, obj, form, change)
    inlines = [Recebimento_vencimentoInline, Recebimento_comissaoInline, Forma_de_pagamentoInline]

admin.site.register(Fin_tipo_documento)
admin.site.register(Pagamento_comissao)
