from django.db.models import Sum, Max, Min, Avg
from django.db.models.aggregates import Avg, Min
from django.shortcuts import render
from producao.models import View_serrada, Serrada
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt

def example(request):
    _sum = View_serrada.objects.all().aggregate(sum=Sum('m3_liquido'))
    _max = View_serrada.objects.all().aggregate(max=Max('m3_liquido'))
    _min = View_serrada.objects.all().aggregate(min=Min('m3_liquido'))
    _avg = View_serrada.objects.all().aggregate(avg=Avg('m3_liquido'))
    return render(request, 'custos_gerais/view_serrada_sum.html', {'sum':_sum, 'max':_max, 'min':_min, 'avg':_avg})

def main_view(request):
    qs = View_serrada.objects.all().values()
    data = pd.DataFrame(qs)
   # data.loc['m3_bruto'] = data.sum()

    context = {
        'df': data.to_html(),
        'describe': data.describe().to_html()
    }

    return render(request, 'custos_gerais/view_serraria.html', context)

def pd_serrada(request):
    qs = View_serrada.objects.all().values()
    data = pd.DataFrame(qs)
    producao_por_material = data[["mes","ano","material","m2"]].groupby(["mes","ano","material"]).sum()
    
    #data = data.drop(columns=['espessura','maquina','qtde_fios_aplicado','prd_fio_m2','consumo_kwh','quantidade_fio','custo_fio_por_m2','custo_fio_por_m2_aplicado','valor_do_bloco','valor_m3','custo_m2_sem_borda','custo_m2_com_borda','bloco','comprimento','altura','largura','serrada','data_inicial','data_final','observacoes','periferica','cala','jogo_fio_id','horimetro_inicial','horimetro_final','amperagem_max','espessura_fio_inicial','espessura_fio_final'])
    
    #datagb = data.groupby(['ano','mes','material'],dropna=False).sum()
    
    #datagb.loc['Total'] = data.sum()


    context = {
        #'df': datagb.to_html(),
        #'df': datagb.to_html(classes=['table', 'table-striped', 'table-hover']),
        'df': producao_por_material.to_html(classes=['table', 'table-striped', 'table-hover']),
        
        #'df': data.to_html(),        
        'describe': data.describe().to_html(classes=['table', 'table-striped', 'table-hover']),
        
    }
    return render(request, 'custos_gerais/serrada.html', context)

   
def pd_serrada_soma(request):
    pd.set_option('display.precision', 2)

    qs = View_serrada.objects.all().values()
    data_soma = pd.DataFrame(qs)  
    
    data_soma = data_soma.drop(columns=['material','espessura','maquina','qtde_fios_aplicado','prd_fio_m2','consumo_kwh','quantidade_fio','custo_fio_por_m2','custo_fio_por_m2_aplicado','valor_do_bloco','valor_m3','custo_m2_sem_borda','custo_m2_com_borda','bloco','comprimento','altura','largura','serrada','data_inicial','data_final','observacoes','periferica','cala','jogo_fio_id','horimetro_inicial','horimetro_final','amperagem_max','espessura_fio_inicial','espessura_fio_final'])
    
    #data_soma.loc['Total'] = data_soma.sum()
    data_soma.loc['Total'] = data_soma.sum()
    #data_soma2 = data_soma.groupby(['ano','mes']).sum()
    context = {
        'df': data_soma.to_html(classes=['table', 'table-striped', 'table-hover']),
        'describe': data_soma.describe().to_html(),        
    }
    return render(request, 'custos_gerais/serrada_soma.html', context)

   