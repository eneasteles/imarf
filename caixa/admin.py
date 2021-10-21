from django.conf import settings
from django.contrib import admin, messages
from django.contrib.auth.admin import UserAdmin

from .models import *
# Register your models here.

class Caixa_Item_inline(admin.TabularInline):
    model = Caixa_Item
    extra = 1
    exclude=("valor",)
    readonly_fields=('valor', )
    

@admin.register(Caixa)
class CaixaAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user_id=request.user)
    exclude=("valor",)
    readonly_fields=('valor', )
    list_display = ('id', 'data', 'filial', 'natureza', 'valor')
    list_filter = ('natureza','filial')
    search_fields = ('id', 'data', 'valor')
    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
            obj.save()
        super(CaixaAdmin, self).save_model(request, obj, form, change)
    
    
    
    inlines = [Caixa_Item_inline,]

@admin.register(Filial)
class FilialAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user_id=request.user)
    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
            obj.save()
        super(FilialAdmin, self).save_model(request, obj, form, change)
#admin.site.register(Filial)
admin.site.register(Aplicacao)

