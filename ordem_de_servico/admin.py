from django.conf import settings
from django.contrib import admin, messages
from django.contrib.admin.options import StackedInline, TabularInline
from django.contrib.auth.admin import UserAdmin

from .models import *
# Register your models here.
class DiagnosticoInline(StackedInline):
    model = Diagnostico
    extra = 0
class EquipamentoInline(StackedInline):
    model = Equipamento
    extra = 0
class OS_ItemInline(TabularInline):
    model = OS_Item
    extra = 1


@admin.register(OS)
class OSAdmin(admin.ModelAdmin):
    list_display = ('os','data', 'status')
    list_filter = ('status',)
    #search_fields = ('veiculo', 'placa', 'ano')
    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
            obj.save()
        super(OSAdmin, self).save_model(request, obj, form, change)
    
    inlines = [EquipamentoInline, 
    #VeiculoBemInline,
    DiagnosticoInline,
    OS_ItemInline,
    ]



