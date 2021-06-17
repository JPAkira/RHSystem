from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth import get_user_model
from vagas.models import Vaga
User = get_user_model()

def index(request):
    vagas = Vaga.objects.order_by('data_criacao')

    dados = {
        'vagas': vagas
    }

    return render(request, 'index.html', dados)

def logout(request):
    auth.logout(request)
    messages.success(request, 'Você fez logout com sucesso!')
    return redirect('index')

