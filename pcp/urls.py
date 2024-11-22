from django.conf.urls import url
import cadastro
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("producao.urls")),
    path('', include('cadastro.urls')),
    path('', include('usuarios.urls')),
    path('', include('custos_gerais.urls')),
    path('', include('setor_pessoal.urls')),
    path('', include('corte.urls')),
    path('', include('fin_recebimento.urls')),
    path('', include('sesmt.urls')),
    path('comercial/', include('comercial.urls')),
    url(r'^chaining/', include('smart_selects.urls')),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
