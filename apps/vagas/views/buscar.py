from django.shortcuts import render, redirect, get_object_or_404
from candidato.models import Aplicacao
from vagas.models import Vaga
from apps.empresa.views.autenticacao import *

def buscar_candidatos_vaga(request, vaga_id):

    if not (autenticacao(request)):
        return redirect('empresa_login')

    vaga = get_object_or_404(Vaga, pk=vaga_id)

    if request.user.pk != vaga.empresa.pk:
        return redirect('empresa_login')


    lista_aplicacoes = Aplicacao.objects.order_by('data_criacao').filter(vaga=vaga)

    if request.method == 'POST':
        nome_a_buscar = request.POST['buscar']
        if nome_a_buscar:
            lista_aplicacoes = lista_aplicacoes.filter(candidato__first_name__icontains=nome_a_buscar)

            numero_de_inscritos = lista_aplicacoes.count()

    dados = {
        'candidatos': lista_aplicacoes,
        'numero_de_inscritos': numero_de_inscritos,
        'vaga': vaga
    }

    return render(request, 'vagas/candidatos.html', dados)