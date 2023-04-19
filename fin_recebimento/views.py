from django.shortcuts import render
from django.db.models import Sum, Max, Min, Avg
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recebimento

# Create your views here.
class ComissaoList(LoginRequiredMixin ,ListView):
    login_url = reverse_lazy('login')
    model = Recebimento
    template_name = 'fin_recebimento/comissao.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ComissaoList, self).get_context_data(*args, **kwargs)
        context['valor'] = Recebimento.objects.aggregate(Sum('valor'))        
        return context