from django.conf.urls import url
from django.urls import path
from .views import *

urlpatterns = [
    path('recebimento/', ComissaoList.as_view(), name='comissao'),
]