from django.contrib import admin
from .models import Setor

# Register your models here.
@admin.register(Setor)
class SetorAdmin(admin.ModelAdmin):
    list_display = ('setor',)
