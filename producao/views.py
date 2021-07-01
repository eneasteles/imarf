from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def home(request):
    return HttpResponse('Página Inicial')

class IndexView(TemplateView):
    template_name = 'index.html'


class PaginaInicial(TemplateView):
    template_name = 'producao/modelo.html'

class SobreView(TemplateView):
    template_name = 'producao/sobre.html'