from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from vagas.models import Vaga
from .autenticacao import *

def minhas_vagas(request):

    if not (autenticacao(request)):
        return redirect('empresa_login')

    id = request.user.id

    vagas = Vaga.objects.order_by('data_criacao').filter(empresa=id)

    dados = {
        'vagas': vagas
    }

    return render(request, 'empresa/minhas_vagas.html', dados)

def deletar_vaga(request, vaga_id):

    if not (autenticacao(request)):
        return redirect('empresa_login')

    vaga = get_object_or_404(Vaga, pk=vaga_id)

    ''' Verificando se a empresa é a administradora da vaga '''
    if request.user.pk != vaga.empresa.pk:
        return redirect('empresa_login')

    vaga.delete()

    messages.success(request, 'Deletado com sucesso')

    return redirect('minhas_vagas')