from django.shortcuts import render, redirect
from vagas.models import Vaga
from django.db.models import Q

def buscar_vagas_index(request):

    lista_vagas = Vaga.objects.order_by('data_criacao')

    if request.method == 'POST':
        nome_a_buscar = request.POST['buscar']
        if nome_a_buscar:
            lista_vagas = lista_vagas.filter(Q(cargo__icontains=nome_a_buscar)|Q(empresa__first_name__icontains=nome_a_buscar))

    dados = {
        'vagas': lista_vagas
    }

    return render(request, 'index.html', dados)