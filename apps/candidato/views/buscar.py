from django.shortcuts import render, redirect
from candidato.models import Aplicacao
from django.db.models import Q
from .autenticacao import *

def buscar_vagas_candidato(request):

    if not (autenticacao(request)):
        return redirect('candidato_login')

    id = request.user.id

    lista_aplicacoes = Aplicacao.objects.order_by('data_criacao').filter(candidato=id)

    if request.method == 'POST':
        nome_a_buscar = request.POST['buscar']
        if nome_a_buscar:
            lista_aplicacoes = lista_aplicacoes.filter(Q(vaga__cargo__icontains=nome_a_buscar)|Q(vaga__empresa__first_name__icontains=nome_a_buscar))

    dados = {
        'vagas': lista_aplicacoes
    }

    return render(request, 'candidato/minhas_vagas.html', dados)