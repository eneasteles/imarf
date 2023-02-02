from django.conf.urls import url
from django.urls import  include

urlpatterns = [

    url(r'^chaining/', include('smart_selects.urls')),
]
