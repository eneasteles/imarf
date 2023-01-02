from django.urls import path

from .views import *

urlpatterns = [
    path('adm/ti/', Resumo.as_view(), name='resumo'),
]