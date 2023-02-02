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
    #list_select_related = ('status',)
    list_filter = ('status',)
    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
            obj.save()
        super(OSComercialAdmin, self).save_model(self, request, obj, form, change)
    
    inlines = [
    OS_Comercial_ItemInline,
    ]

###     pedido de venda
class Forma_de_pagamento_inline(admin.TabularInline):
    model = Forma_de_pagamento
    extra = 1
    readonly_fields = ('valor',)

class Pedido_de_venda_item_inline(admin.TabularInline):
    model = Pedido_de_venda_item
    extra = 0
    readonly_fields=('valor', 'metragem', )
    autocomplete_fields = ['bloco']

class Venda_chapa_produzida_inline(admin.TabularInline):
    model = Venda_chapa_produzida
    extra = 0
    readonly_fields=('status_chapa', )
    autocomplete_fields = ['bloco', ]

class Venda_chapa_mult_select_inline(admin.TabularInline):
    model = Venda_chapa_mult_select
    extra = 0
    readonly_fields=('status_chapa', )

class Pedido_de_venda_outlet_inline(admin.TabularInline):
    model = Pedido_de_venda_outlet
    extra = 1
    list_display = ('lote',)

    

@admin.register(Pedido_de_venda)    
class Pedido_de_venda_Admin(admin.ModelAdmin): 
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user_id=request.user)   
    search_fields = ('id','pessoa__nome')
    list_display = ('id','pessoa','data','total', 'full_url','user',)
    list_select_related = ('pessoa',)
    list_display_links = ('id','pessoa','data')
    readonly_fields=('total',)
    list_filter = ('user',)
    
    list_per_page = 10
    autocomplete_fields = ['pessoa']
    inlines = [
        Pedido_de_venda_item_inline,
        Venda_chapa_produzida_inline,
        #Venda_chapa_mult_select_inline,
        Pedido_de_venda_outlet_inline,
        Forma_de_pagamento_inline,      
       
    ]

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
            obj.save()
        super(Pedido_de_venda_Admin, self).save_model(request, obj, form, change)

admin.site.register(Status_pv)
"""
"""
