from django.contrib import admin

# Register your models here.
from . models import *

# Register your models here.
class Telamento_iteminline(admin.TabularInline):
    model = Telamento_item
    extra = 0

@admin.register(Telamento)
class EnvolopamentoAdmin(admin.ModelAdmin):
    search_fields = ('id',)
    list_display = ('data','bloco','id',)
    autocomplete_fields = ('bloco',)
    inlines = [
        Telamento_iteminline,
        
    ]