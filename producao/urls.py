from django.urls import path

from . import views

urlpatterns = [
    path('current_datetime/', views.current_datetime, name='current_datetime'),
    path('', views.views.home, name='home')

]