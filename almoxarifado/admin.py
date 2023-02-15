from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Unidade_de_Medida)
admin.site.register(Grupo_Almoxarifado)
admin.site.register(Classe_Almoxarifado)
admin.site.register(Categoria_Almoxarifado)


@admin.register(Item_de_Almoxarifado)
class Item_de_Almoxarifado_Admin(admin.ModelAdmin):
    search_fields = ('id','item','unidade','quantidade','valor')
    list_display = ('id','item','unidade','quantidade','valor', 'grupo','classe','categoria')
    list_display_links = ('id','item')
    list_filter = ('unidade','quantidade','valor')
    list_per_page = 10
    readonly_fields = ('quantidade',)



"""
@admin.register(Item_de_Almoxarifado)    
class Item_de_Almoxarifado_Admin(admin.ModelAdmin): 
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
