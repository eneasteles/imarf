from django.contrib import admin
from .models import *
# Register your models here.

class Caixa_Item_inline(admin.TabularInline):
    model = Caixa_Item
    extra = 1
@admin.register(Caixa)
class CaixaAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(usuario_id=request.user)

    list_display = ('id', 'data', 'filial', 'natureza', 'valor')
    list_filter = ('natureza', 'filial',)
    search_fields = ('id', 'data', 'valor')

    inlines = [Caixa_Item_inline,]

admin.site.register(Filial)
admin.site.register(Aplicacao)

