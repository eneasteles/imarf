from django.urls import path

from .views import *

urlpatterns = [
    path('custos_gerais/sum/', example, name='sum_m3_liquido'),
    path('custos_gerais/', main_view, name='pandas-serraria'),
    path('custos_gerais/serrada/', pd_serrada, name='pd_serrada'),
    path('custos_gerais/serrada/soma/', pd_serrada_soma, name='pd_serrada_soma'),
]