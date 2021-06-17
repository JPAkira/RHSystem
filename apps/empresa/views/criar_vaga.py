from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from vagas.models import Vaga, Requisitos, Desejavel
from .autenticacao import *
from .validacoes import *


def criar_vaga(request):

    if not (autenticacao(request)):
        return redirect('empresa_login')

    if request.method == 'POST':
        cargo = request.POST['cargo']
        faixa_salarial = request.POST['faixa_salarial']
        escolaridade = request.POST['escolaridade']
        descricao = request.POST['descricao']

        if not (valida_campo_texto(cargo, "Cargo", 40, request)):
            return redirect('criar_vaga')

        if not (valida_campo_texto(descricao, "Descrição", 200, request)):
            return redirect('criar_vaga')

        if not (valida_faixa_salarial(faixa_salarial, request)):
            return redirect('criar_vaga')

        if not (valida_escolaridade(escolaridade, request)):
            return redirect('criar_vaga')

        empresa = request.user
        vaga = Vaga.objects.create(cargo=cargo, faixa_salarial=faixa_salarial, escolaridade=escolaridade, descricao=descricao, empresa=empresa)
        vaga.save()

        return redirect('adicionar_requisitos', vaga.id)

    return render(request, 'empresa/criar_vaga.html')

def adicionar_requisitos(request, vaga_id):

    if not (autenticacao(request)):
        return redirect('empresa_login')

    vaga = get_object_or_404(Vaga, pk=vaga_id)

    if request.method == 'POST':
        requisito = request.POST['requisito']

        if not (valida_campo_texto(requisito, "Requisito", 40, request)):
            return redirect('adicionar_requisitos', vaga_id)

        requisito = Requisitos.objects.create(vaga=vaga, requisito=requisito)
        requisito.save()
        return redirect('adicionar_requisitos', vaga.id)

    requisitos = Requisitos.objects.order_by('vaga')

    requisitos = requisitos.filter(vaga=vaga_id)

    dados = {
        'vaga_id': vaga_id,
        'requisitos': requisitos

    }

    return render(request, 'empresa/adicionar_requisitos.html', dados)

def deletar_requisito(request, requisito_id):

    if not (autenticacao(request)):
        return redirect('empresa_login')

    requisito = get_object_or_404(Requisitos, pk=requisito_id)

    vaga_id = requisito.vaga.id

    requisito.delete()

    return redirect('adicionar_requisitos', vaga_id)

def adicionar_desejavel(request, vaga_id):

    if not (autenticacao(request)):
        return redirect('empresa_login')

    vaga = get_object_or_404(Vaga, pk=vaga_id)

    if request.method == 'POST':
        desejavel = request.POST['desejavel']

        if not (valida_campo_texto(desejavel, "Desejavel", 40, request)):
            return redirect('adicionar_desejavel', vaga_id)

        desejavel = Desejavel.objects.create(vaga=vaga, desejavel=desejavel)
        desejavel.save()
        return redirect('adicionar_desejavel', vaga.id)

    requisitos_desejavel = Desejavel.objects.order_by('vaga')

    requisitos_desejavel = requisitos_desejavel.filter(vaga=vaga_id)

    dados = {
        'vaga_id': vaga_id,
        'requisitos_desejavel': requisitos_desejavel

    }

    return render(request, 'empresa/adicionar_desejavel.html', dados)

def deletar_desejavel(request, desejavel_id):

    if not (autenticacao(request)):
        return redirect('empresa_login')

    desejavel = get_object_or_404(Desejavel, pk=desejavel_id)

    vaga_id = desejavel.vaga.id

    desejavel.delete()

    return redirect('adicionar_desejavel', vaga_id)
