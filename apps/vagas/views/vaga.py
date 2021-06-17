from django.shortcuts import render, get_object_or_404
from vagas.models import Vaga, Requisitos, Desejavel

def vaga(request, vaga_id):

    vaga = get_object_or_404(Vaga, pk=vaga_id)
    requisitos = Requisitos.objects.order_by('vaga').filter(vaga=vaga_id)
    requisitos_desejavel = Desejavel.objects.order_by('vaga').filter(vaga=vaga_id)

    dados = {
        'vaga': vaga,
        'requisitos': requisitos,
        'requisitos_desejavel': requisitos_desejavel
    }

    return render(request, 'vagas/vaga.html', dados)