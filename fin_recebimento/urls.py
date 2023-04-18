from django.conf.urls import url
from django.urls import path
from .views import *

urlpatterns = [
    path('comissao/', ComissaoList.as_view(), name='comissao'),
]