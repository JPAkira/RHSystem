from django.shortcuts import render, get_object_or_404, redirect
from vagas.models import Vaga, Requisitos, Desejavel
from candidato.models import Aplicacao, Experiencia
from .validacoes import *
from .autenticacao import *


def aplicacao(request, vaga_id):
    if not (autenticacao(request)):
        return redirect('candidato_login')

    if not (autenticacao_duplicidade_aplicacao(request, vaga_id)):
        return redirect('index')

    vaga = get_object_or_404(Vaga, pk=vaga_id)

    dados = {
        'vaga': vaga
    }

    if request.method == 'POST':
        pretencao_salarial = request.POST['faixa_salarial']
        escolaridade = request.POST['escolaridade']

        if not (valida_pretencao_salarial(pretencao_salarial, request)):
            return redirect('aplicacao', vaga_id)

        if not(valida_escolaridade(escolaridade, request)):
            return redirect('aplicacao', vaga_id)

        candidato = request.user

        score = retorna_score(vaga_id, escolaridade, pretencao_salarial)

        aplicacao = Aplicacao.objects.create(vaga=vaga, pretencao_salarial=pretencao_salarial,
                                             escolaridade=escolaridade, candidato=candidato, score=score)
        aplicacao.save()

        return redirect('adicionar_experiencia', aplicacao.id)

    return render(request, 'candidato/aplicacao.html', dados)


def retorna_score(vaga_id, escolaridade, pretencao_salarial):
    vaga = get_object_or_404(Vaga, pk=vaga_id)

    escolaridades = [
        'Ensino fundamental', 'Ensino médio', 'Tecnólogo', 'Ensino superior',
        'Pós / MBA / Mestrado', 'Doutorado'
    ]

    vaga_escolaridade = vaga.escolaridade

    escolaridade_minimo = escolaridades.index(vaga_escolaridade)

    score = 0

    if escolaridade in escolaridades[escolaridade_minimo:]:
        score = 1

    if pretencao_salarial == vaga.faixa_salarial:
        score += 1

    return score


def adicionar_experiencia(request, aplicacao_id):

    if not (autenticacao(request)):
        return redirect('candidato_login')

    aplicacao = get_object_or_404(Aplicacao, pk=aplicacao_id)
    vaga = get_object_or_404(Vaga, pk=aplicacao.vaga.id)

    experiencias = Experiencia.objects.order_by('aplicacao_id').filter(aplicacao=aplicacao_id)

    dados = {
        'vaga': vaga,
        'aplicacao': aplicacao,
        'experiencias': experiencias
    }

    if request.method == 'POST':
        cargo = request.POST['cargo']
        experiencia = request.POST['experiencia']

        if not (valida_campo_texto(cargo, "Cargo", 30, request)):
            return redirect('adicionar_experiencia', aplicacao_id)

        if not (valida_campo_texto(experiencia, "Experiência", 400,  request)):
            return redirect('adicionar_experiencia', aplicacao_id)

        experiencia = Experiencia.objects.create(aplicacao=aplicacao, cargo=cargo, experiencia=experiencia)
        experiencia.save()

        return redirect('adicionar_experiencia', aplicacao.id)

    return render(request, 'candidato/adicionar_experiencia.html', dados)


def deletar_experiencia(request, experiencia_id):
    if not (autenticacao(request)):
        return redirect('candidato_login')

    experiencia = get_object_or_404(Experiencia, pk=experiencia_id)

    aplicacao_id = experiencia.aplicacao.id

    experiencia.delete()

    return redirect('adicionar_experiencia', aplicacao_id)


def conhecimentos_candidato(request, aplicacao_id):
    if not (autenticacao(request)):
        return redirect('candidato_login')

    aplicacao = get_object_or_404(Aplicacao, pk=aplicacao_id)
    vaga = get_object_or_404(Vaga, pk=aplicacao.vaga.id)

    requisitos = Requisitos.objects.order_by('vaga').filter(vaga=vaga.id)

    dados = {
        'vaga': vaga,
        'aplicacao': aplicacao,
        'requisitos': requisitos
    }

    if request.method == 'POST':
        nivel_conhecimentos = request.POST['nivel_conhecimentos']
        aplicacao.score += int(nivel_conhecimentos)
        aplicacao.save()

        return redirect('conhecimentos_candidato_desejavel', aplicacao_id)

    return render(request, 'candidato/conhecimentos_candidato.html', dados)


def conhecimentos_candidato_desejavel(request, aplicacao_id):
    if not (autenticacao(request)):
        return redirect('candidato_login')

    aplicacao = get_object_or_404(Aplicacao, pk=aplicacao_id)
    vaga = get_object_or_404(Vaga, pk=aplicacao.vaga.id)

    desejavel = Desejavel.objects.order_by('vaga').filter(vaga=vaga.id)

    dados = {
        'vaga': vaga,
        'aplicacao': aplicacao,
        'requisitos': desejavel
    }

    if request.method == 'POST':
        nivel_conhecimentos = request.POST['nivel_conhecimentos']
        aplicacao.score += int(nivel_conhecimentos)
        aplicacao.save()
        return redirect('index')

    return render(request, 'candidato/conhecimentos_candidato_desejavel.html', dados)
