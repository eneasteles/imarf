from django.contrib import admin

# Register your models here.
from .models import *
class Recebimento_vencimentoInline(admin.TabularInline):
    model = Recebimento_vencimento
    extra = 0
class Recebimento_comissaoInline(admin.TabularInline):
    model = Recebimento_comissao
    extra = 0
    autocomplete_fields = ('vendedor', )
    readonly_fields = ('valor', 'status')

@admin.register(Pagamento_comissao)
class Pagamento_comissaoAdmim(admin.ModelAdmin):
    list_display = ( 'data_pagamento','valor','comissao_da_venda','recebimento_comissao_id',)
 
    def comissao_da_venda(self, obj):
        return Recebimento_comissao.objects.filter(recebimento_id=obj.recebimento_comissao_id).values_list('percentual', flat=True).get()
    comissao_da_venda.short_description = 'Percentual'
    comissao_da_venda.admin_order_field = 'recebimento_comissao__percentual'
""""""

class Forma_de_pagamentoInline(admin.TabularInline):
    model = Forma_de_pagamento
    extra = 0

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

