from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Chapa)
class ChapaAdmin(admin.ModelAdmin):
    #def get_queryset(self, request):
    ##    qs = super().get_queryset(request)
    #    if request.user.is_superuser:
    #        return qs
    #    return qs.filter(usuario_id=request.user)
    list_display = ('id', 'bloco', 'chapa_numero','status_chapa', 'acabamento',)
    list_filter = ('status_chapa',)
    ordering = ('bloco', 'chapa_numero')
    autocomplete_fields = ['bloco']

#admin.site.register(Lancamento_manual_chapa)
@admin.register(Lancamento_manual_chapa)
class Lancamento_manual_chapaAdmin(admin.ModelAdmin):
    #def get_queryset(self, request):
    ##    qs = super().get_queryset(request)
    #    if request.user.is_superuser:
    #        return qs
    #    return qs.filter(usuario_id=request.user)
    list_display = ('id', 'bloco', 'chapa_inicial', 'chapa_final','status_chapa', 'acabamento',)
    autocomplete_fields = ['bloco']
    ordering = ('bloco',)
    search_fields = ('bloco__bloco',)

@admin.register(Lancamento_chapa_quebrada)
class Lancamento_chapa_quebradaAdmin(admin.ModelAdmin):
    #def get_queryset(self, request):
    ##    qs = super().get_queryset(request)
    #    if request.user.is_superuser:
    #        return qs
    #    return qs.filter(usuario_id=request.user)
    autocomplete_fields = ['bloco']
    ordering = ('bloco',)
    search_fields = ('bloco',)

