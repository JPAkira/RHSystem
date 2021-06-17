from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth import get_user_model
from .validacoes import *
User = get_user_model()

def candidato_login(request):
    if request.method == 'POST':
        usuario = request.POST['email']
        senha = request.POST['senha']

        if User.objects.filter(username=usuario).exists():
            user = auth.authenticate(request, username=usuario, password=senha)
            if user is not None:
                if user.is_candidato == True:
                    auth.login(request, user)
                    messages.success(request, 'Login realizado com sucesso')
                    return redirect('index')
                else:
                    messages.error(request, 'Tente logar como empresa, seu usuário não é de candidato')
            else:
                messages.error(request, 'Senha errada')
                return redirect('candidato_login')
        else:
            messages.error(request, 'Login ou senha errada')
            return redirect('candidato_login')
    return render(request, 'candidato/candidato_login.html')

def candidato_registro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['senha']

        if not (valida_nome(nome, request)):
            return redirect('candidato_registro')

        if not (valida_email(email, request)):
            return redirect('candidato_registro')

        if not (valida_senha(senha, request)):
            return redirect('candidato_registro')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email já cadastrado')
            return redirect('candidato_registro')

        user = User.objects.create_user(username=email, email=email, first_name=nome, password=senha, is_candidato=True)
        user.save()
        messages.success(request, 'Cadastro realizado com sucesso')
        return redirect('candidato_login')
    return render(request, 'candidato/candidato_registro.html')