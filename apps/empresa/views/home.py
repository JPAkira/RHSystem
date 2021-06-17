from django.shortcuts import render, redirect
from vagas.models import Vaga
from candidato.models import Aplicacao
from django.db.models import Count
from datetime import datetime
import calendar
from .autenticacao import *

def home(request):

    if not (autenticacao(request)):
        return redirect('empresa_login')

    id = request.user.id

    dados_vagas_mes = retorna_vagas_mes(id)

    dados_candidatos_mes = retorna_candidatos_mes(id)

    dados = {}

    dados.update(dados_vagas_mes)
    dados.update(dados_candidatos_mes)

    return render(request, 'empresa/home.html', dados)

def retorna_vagas_mes(id):
    date = datetime.now()

    vagas = Vaga.objects.filter(empresa=id, data_criacao__year=date.year).values('data_criacao__month').annotate(total=Count('id')).order_by('data_criacao__month')

    labels = []
    data = []

    for vaga in vagas:
        labels.append(calendar.month_name[vaga.get('data_criacao__month')])
        data.append(vaga.get('total'))

    dados = {
        'data_vagas_mes': data,
        'labels_vagas_mes': labels
    }

    return dados

def retorna_candidatos_mes(id):
    date = datetime.now()

    aplicacoes = Aplicacao.objects.filter(vaga__empresa=id, data_criacao__year=date.year).values('data_criacao__month').annotate(total=Count('id')).order_by('data_criacao__month')

    labels = []
    data = []

    for aplicacao in aplicacoes:
        labels.append(calendar.month_name[aplicacao.get('data_criacao__month')])
        data.append(aplicacao.get('total'))

    dados = {
        'data_candidatos_mes': data,
        'labels_candidatos_mes': labels
    }

    return dados