from django.shortcuts import render, redirect
from candidato.models import Aplicacao
from .autenticacao import *

def minhas_aplicacoes(request):

    if not (autenticacao(request)):
        return redirect('candidato_login')

    id = request.user.id

    aplicacoes = Aplicacao.objects.order_by('data_criacao').filter(candidato=id)

    dados = {
        'vagas': aplicacoes
    }

    return render(request, 'candidato/minhas_vagas.html', dados)