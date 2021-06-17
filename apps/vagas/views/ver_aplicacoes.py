from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from vagas.models import Vaga
from candidato.models import Aplicacao, Experiencia
from apps.empresa.views.autenticacao import *

def ver_candidatos(request, vaga_id):

    if not (autenticacao(request)):
        return redirect('empresa_login')

    vaga = get_object_or_404(Vaga, pk=vaga_id)

    if request.user.pk != vaga.empresa.pk:
        return redirect('empresa_login')

    candidatos = Aplicacao.objects.order_by('-score').filter(vaga=vaga)

    numero_de_inscritos = Aplicacao.objects.order_by('score').filter(vaga=vaga).count()

    dados = {
        'candidatos': candidatos,
        'numero_de_inscritos': numero_de_inscritos,
        'vaga': vaga
    }

    return render(request, 'vagas/candidatos.html', dados)

def ver_experiencias(request, aplicacao_id):

    if not (autenticacao(request)):
        return redirect('empresa_login')

    aplicacao = get_object_or_404(Aplicacao, pk=aplicacao_id)

    experiencias = Experiencia.objects.order_by('cargo').filter(aplicacao__id=aplicacao.id)

    dados = {
        'candidato': aplicacao,
        'experiencias': experiencias
    }

    return render(request, 'vagas/ver_experiencias.html', dados)