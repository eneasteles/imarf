from django.contrib import admin

from pedreira.models import Lancamento, Lancamento_Item, Producao_pedreira_m3

# Register your models here.
class Lancamento_Item_inline(admin.TabularInline):
    model = Lancamento_Item
    extra = 1
    exclude=("valor",)
    readonly_fields=('valor', )
    autocomplete_fields = ('item','bem',)

@admin.register(Lancamento)
class CaixaAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user_id=request.user)
    exclude=("valor",)
    readonly_fields=('valor', )
    list_display = ('id', 'data',  'valor', 'descricao','user')
    list_filter = ('user',)
    search_fields = ('id', 'data',)
    exclude=("valor",)
    #raw_id_fields = ("empresa",)

    #readonly_fields = ('valor',)
    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
            obj.save()
        super(CaixaAdmin, self).save_model(request, obj, form, change)
    
    
    
    inlines = [Lancamento_Item_inline,]
@admin.register(Producao_pedreira_m3)
class Producao_pedreira_m3Admin(admin.ModelAdmin):
    list_display = ('ano', 'mes',  'empresa', 'pedreira','material','m3','m2')
