from django.shortcuts import render, redirect
from vagas.models import Vaga
from django.db.models import Q
from .autenticacao import *

def buscar_vagas_empresa(request):

    if not (autenticacao(request)):
        return redirect('empresa_login')

    id = request.user.id

    lista_vagas = Vaga.objects.order_by('data_criacao').filter(empresa=id)

    if request.method == 'POST':
        nome_a_buscar = request.POST['buscar']
        if nome_a_buscar:
            lista_vagas = lista_vagas.filter(Q(cargo__icontains=nome_a_buscar)|Q(empresa__first_name__icontains=nome_a_buscar))

    dados = {
        'vagas': lista_vagas
    }

    return render(request, 'empresa/minhas_vagas.html', dados)