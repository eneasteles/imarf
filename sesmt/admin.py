from django.contrib import admin
from .models import PDFDocument, Title
from cadastro.models import UserEnterprise
from django.db.models import QuerySet


@admin.register(PDFDocument)
class PDFDocumentoAdmin(admin.ModelAdmin):
    search_fields = ('worker__nome',)
    autocomplete_fields = ['worker']
    list_display = ('enterprise', 'worker', 'title', 'emissao_documento','pdf_file')
    list_filter = ('enterprise',)

    def get_queryset(self, request) -> QuerySet:
        """
        Filtra os documentos para que usuários normais só vejam documentos
        relacionados à empresa associada.
        """
        qs = super().get_queryset(request)

        if request.user.is_superuser:
            # Superusuários têm acesso a todos os documentos
            return qs

        try:
            # Obtém a empresa associada ao usuário
            user_enterprises = UserEnterprise.objects.filter(user=request.user).values_list('enterprise', flat=True)
            #return qs.filter(enterprise=user_enterprise)
            return qs.filter(enterprise__in=user_enterprises)
        except UserEnterprise.DoesNotExist:
            # Caso o usuário não tenha uma empresa associada, retorna um queryset vazio
            return qs.none()

    def get_search_results(self, request, queryset, search_term):
        """
        Customiza os resultados da busca para respeitar o filtro aplicado.
        """
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        # Print the search term and results in the console for debugging
        print(f"Search Term: {search_term}")
        print(f"Results: {queryset}")
        return queryset, use_distinct

admin.site.register(Title)