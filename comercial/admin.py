from django.conf import settings
from django.contrib import admin, messages
from django.contrib.admin.options import StackedInline, TabularInline
from django.contrib.auth.admin import UserAdmin

from .models import *
# Register your models here.

class OS_Comercial_ItemInline(TabularInline):
    model = OS_Comercial_Item
    extra = 1


@admin.register(OSComercial)
class OSComercialAdmin(admin.ModelAdmin):
    list_display = ('os','data', 'status')
    list_filter = ('status',)
    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
            obj.save()
        super(OSComercialAdmin, self).save_model(request, obj, form, change)
    
    inlines = [
    OS_Comercial_ItemInline,
    ]




