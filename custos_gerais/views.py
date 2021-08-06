from django.db.models import Sum, Max, Min, Avg
from django.db.models.aggregates import Avg, Min
from django.shortcuts import render
from producao.models import View_serrada
import pandas as pd

def example(request):
    _sum = View_serrada.objects.all().aggregate(sum=Sum('m3_liquido'))
    _max = View_serrada.objects.all().aggregate(max=Max('m3_liquido'))
    _min = View_serrada.objects.all().aggregate(min=Min('m3_liquido'))
    _avg = View_serrada.objects.all().aggregate(avg=Avg('m3_liquido'))
    return render(request, 'custos_gerais/view_serrada_sum.html', {'sum':_sum, 'max':_max, 'min':_min, 'avg':_avg})

def main_view(request):
    qs = View_serrada.objects.all().values()
    data = pd.DataFrame(qs)
   

    context = {
        'df': data.to_html(),
        'describe': data.describe().to_html()
    }

    return render(request, 'custos_gerais/view_serraria.html', context)