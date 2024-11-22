from django.contrib import admin
from .models import *

# Register your models here.a


@admin.register(PDFDocument)
class EnvolopamentoAdmin(admin.ModelAdmin):
    search_fields = ('worker__nome',)
    autocomplete_fields = ['worker']    
    list_display = ('enterprise','worker','title','pdf_file')
    list_filter = ('enterprise',)
    autocomplete_fields = ('worker',)
    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        # Print the search term and results in the console
        print(f"Search Term: {search_term}")
        print(f"Results: {queryset}")
        return queryset, use_distinct


admin.site.register(Title)