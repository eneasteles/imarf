from django.contrib import admin

# Register your models here.from 
from .models import Bem

# Register your models here.
@admin.register(Bem)
class BemAdmin(admin.ModelAdmin):
    search_fields = ('bem',)

