from django.shortcuts import render, redirect, get_object_or_404
from vagas.models import Vaga
from .validacoes import *

def editar_vaga(request, vaga_id):

    '''Autenticando o acesso a pagina'''

    if not request.user.is_authenticated:
        return redirect('empresa_login')
    if not request.user.is_empresa:
        return redirect('empresa_login')

    vaga = get_object_or_404(Vaga, pk=vaga_id)

    ''' Verificando se a empresa é a administradora da vaga '''
    if request.user.pk != vaga.empresa.pk:
        return redirect('empresa_login')

    if request.method == 'POST':

        vaga.cargo = request.POST['cargo']
        vaga.faixa_salarial = request.POST['faixa_salarial']
        vaga.escolaridade = request.POST['escolaridade']
        vaga.descricao = request.POST['descricao']
        vaga.empresa = request.user

        if not (valida_campo_texto(vaga.cargo, "Cargo", 40, request)):
            return redirect('editar_vaga', vaga_id)

        if not (valida_campo_texto(vaga.descricao, "Descrição", 200, request)):
            return redirect('editar_vaga', vaga_id)

        if not (valida_faixa_salarial(vaga.faixa_salarial, request)):
            return redirect('editar_vaga', vaga_id)

        if not (valida_escolaridade(vaga.escolaridade, request)):
            return redirect('editar_vaga', vaga_id)

        vaga.save()

        return redirect('adicionar_requisitos', vaga.id)

    dados = {
        'vaga': vaga
    }

    return render(request, 'empresa/editar_vaga.html', dados)