from django.conf.urls import url
from django.urls import path
from django.urls import  include
from . import views

urlpatterns = [
    path('pdf/<int:id>', views.pedido_pdf, name='pedido_pdf'),
    #path('<int:id>/', views.some_view, name='some_view'),
    url(r'^chaining/', include('smart_selects.urls')),
]
