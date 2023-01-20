from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Chapa)
#admin.site.register(Lancamento_manual_chapa)
@admin.register(Lancamento_manual_chapa)
class Lancamento_manual_chapaAdmin(admin.ModelAdmin):
    #def get_queryset(self, request):
    ##    qs = super().get_queryset(request)
    #    if request.user.is_superuser:
    #        return qs
    #    return qs.filter(usuario_id=request.user)
    autocomplete_fields = ['bloco']
    ordering = ('bloco',)
    search_fields = ('bloco',)


