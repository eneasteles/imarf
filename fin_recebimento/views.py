from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recebimento

# Create your views here.
class ComissaoList(LoginRequiredMixin ,ListView):
    login_url = reverse_lazy('login')
    model = Recebimento
    template_name = 'fin_recebimento/comissao.html'