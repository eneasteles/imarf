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

###     pedido de venda
class Forma_de_pagamento_inline(admin.TabularInline):
    model = Forma_de_pagamento
    extra = 1

class Pedido_de_venda_item_inline(admin.TabularInline):
    model = Pedido_de_venda_item
    extra = 1
    readonly_fields=('valor', )

@admin.register(Pedido_de_venda)    
class Pedido_de_venda_Admin(admin.ModelAdmin): 
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user_id=request.user)   
    list_display = ('id','pessoa','data')
    list_display_links = ('id','pessoa','data')
 #   list_filter = ('id','pessoa')
    list_per_page = 10
    search_fields = ['id']
    inlines = [
        Pedido_de_venda_item_inline,
       # Forma_pagamento_inline,
    ]

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
            obj.save()
        super(Pedido_de_venda_Admin, self).save_model(request, obj, form, change)



"""
"""