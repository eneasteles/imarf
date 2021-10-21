from django.conf import settings
from django.contrib import admin, messages
from django.contrib.auth.admin import UserAdmin

from .models import *
# Register your models here.


@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('veiculo','placa', 'modelo', 'filial', 'ano', 'marca',)
    list_filter = ('filial',)
    search_fields = ('veiculo', 'placa', 'ano')
    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
            obj.save()
        super(VeiculoAdmin, self).save_model(request, obj, form, change)
    


@admin.register(Movimentacao)
class MovimentacaoAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user_id=request.user)
    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
            obj.save()
        super(MovimentacaoAdmin, self).save_model(request, obj, form, change)


