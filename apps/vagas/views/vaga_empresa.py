from django.shortcuts import render, get_object_or_404, redirect
from vagas.models import Vaga, Requisitos, Desejavel
from apps.empresa.views.autenticacao import *

def vaga_empresa(request, vaga_id):

    if not (autenticacao(request)):
        return redirect('empresa_login')

    vaga = get_object_or_404(Vaga, pk=vaga_id)

    ''' Verificando se a empresa é a administradora da vaga '''
    if request.user.pk != vaga.empresa.pk:
        return redirect('empresa_login')

    requisitos = Requisitos.objects.order_by('vaga').filter(vaga=vaga_id)
    requisitos_desejavel = Desejavel.objects.order_by('vaga').filter(vaga=vaga_id)

    dados = {
        'vaga': vaga,
        'requisitos': requisitos,
        'requisitos_desejavel': requisitos_desejavel
    }

    return render(request, 'vagas/empresa_vaga.html', dados)