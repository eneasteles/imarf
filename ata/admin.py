from django.contrib import admin
from .models import *

# Register your models here.
class Ata_item_pessoaInline(admin.TabularInline):  
    model = Ata_item_pessoa
    extra = 0

class Ata_itemInline(admin.TabularInline):
    model = Ata_item
    extra = 0

@admin.register(Ata)
class AtaAdmin(admin.ModelAdmin):
    list_display = ('data_reuniao', 'tema', 'status')
    list_filter = ('status',)
    search_fields = ('data', 'tema')
    inlines = [Ata_itemInline,Ata_item_pessoaInline,]

