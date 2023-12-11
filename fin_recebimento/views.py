from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Sum, Max, Min, Avg
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recebimento
from django.http import Http404
# Create your views here.
class ComissaoList(LoginRequiredMixin ,ListView):
    login_url = reverse_lazy('login')
    model = Recebimento
    template_name = '/fin_recebimento/comissao.html'
    context_object_name = 'recebimentos'
"""
    def get_context_data(self, *args, **kwargs):
        context = super(ComissaoList, self).get_context_data(*args, **kwargs)
        context['valor'] = Recebimento.objects.aggregate(Sum('valor'))        
        return context
    
    def comissao_pdf(request, data_pagamento_inicial, data_pagamento_final):    
    
       
    try:
        obj = Recebimento.objects.filter(data_pagamento>=data_pagamento_inicial).filter(data_pagamento<=data_pagamento_final).order_by('data_pagamento')
        
    except Recebimento.DoesNotExist:
        raise Http404("Pedido não encontrado")
        return render(request, "fin_recebimento/comissao.html", {'pedido': obj, 'pedido_item': obj_item, 'pedido_endereco': obj_endereco,})
"""