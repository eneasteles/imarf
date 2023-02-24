from django.conf.urls import url
import cadastro
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("producao.urls")),
    path('', include('cadastro.urls')),
    path('', include('usuarios.urls')),
    path('', include('custos_gerais.urls')),
    path('', include('setor_pessoal.urls')),
    path('', include('corte.urls')),
    path('comercial/', include('comercial.urls')),
    url(r'^chaining/', include('smart_selects.urls')),
]
