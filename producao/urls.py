from django.urls import path

from . import views

urlpatterns = [
    path('current_datetime/', views.current_datetime, name='current_datetime'),
    # path('', views.home, name='home')
    path('', views.PaginaInicial.as_view(), name='index'),
    path('teste', views.IndexView.as_view(), name='inicio'),
    path('sobre/', views.SobreView.as_view(), name='sobre'),

]