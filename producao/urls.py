from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.ver_pedido, name='ver_pedido'),
    path('some_view/', views.some_view, name='some_view'),
    path('meufpdf/', views.meufpdf, name='meufpdf'),
    path('meupdf2/', views.meupdf2, name='meupdf2'),
   # path('view_serrada/', views.view_serrada, name='view_serrada')


]