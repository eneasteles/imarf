from django.contrib import admin
from .models import Adm_empresa, UserEnterprise

@admin.register(Adm_empresa)
class AdmEmpresaAdmin(admin.ModelAdmin):
    list_display = ['empresa', 'cnpj', 'ie', 'im']


@admin.register(UserEnterprise)
class UserEnterpriseAdmin(admin.ModelAdmin):
    list_display = ['enterprise', 'get_users']
    filter_horizontal = ['user']

    def get_users(self, obj):
        # Exibe os nomes dos usuários associados como string
        return ", ".join([user.username for user in obj.user.all()])
    get_users.short_description = "Usuários"
