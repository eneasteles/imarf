from django.contrib import admin
from .models import *

@admin.register(Produto_de_Venda)
class Produto_de_VendaAdmin(admin.ModelAdmin):


    list_display = ('id', 'material', 'tipo', 'acabamento','identificacao','quantidade','comprimento','altura_espessura','largura','preco',)
    list_filter = ('tipo','material')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
            obj.save()
        super(Produto_de_VendaAdmin, self).save_model(request, obj, form, change)


