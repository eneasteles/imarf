from django.contrib import admin
from models import *
from producao.models import *

class BlocosItemsinline(admin.TabularInline):    
    model = BlocoItem
    extra = 1


@admin.register(Blocos)
class BlocosAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(usuario_id=request.user)
    
    ordering = ('bloco',)
    list_filter = ('status','tipo','material',)
    list_display = ('bloco','material','tipo','comprimento','altura','largura','status')
    #list_editable = ('comprimento','altura','largura','status')
    
    search_fields = ('bloco',)
    inlines = [
        BlocosItemsinline
    ]

