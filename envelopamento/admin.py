from django.contrib import admin
from . models import *

# Register your models here.
class Envelopamento_iteminline(admin.TabularInline):
    model = Envelopamento_item
    extra = 0

class Envelopamento_blocoinline(admin.TabularInline):
    model = Envelopamento_bloco
    extra = 0

@admin.register(Envelopamento)
class EnvolopamentoAdmin(admin.ModelAdmin):
    search_fields = ('id',)
    list_display = ('data','bloco','id',)
    autocomplete_fields = ('bloco',)
    inlines = [
        Envelopamento_iteminline,
        Envelopamento_blocoinline,
    ]
