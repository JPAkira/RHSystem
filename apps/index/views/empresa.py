from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth import get_user_model
from .validacoes import *
User = get_user_model()

def empresa_login(request):
    if request.method == 'POST':
        usuario = request.POST['email']
        senha = request.POST['senha']

        if User.objects.filter(username=usuario).exists():
            user = auth.authenticate(request, username=usuario, password=senha)
            if user is not None:
                if user.is_empresa == True:
                    auth.login(request, user)
                    messages.success(request, 'Login realizado com sucesso')
                    return redirect('home')
                else:
                    messages.error(request, 'Seu usuário pode ser de candidato ou não estar ativo ainda.')
            else:
                messages.error(request, 'Senha errada')
                return redirect('candidato_login')
        else:
            messages.error(request, 'Login ou senha errada')
            return redirect('candidato_login')
    return render(request, 'empresa/empresa_login.html')

def empresa_registro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['senha']

        if not (valida_nome(nome, request)):
            return redirect('empresa_registro')

        if not (valida_email(email, request)):
            return redirect('empresa_registro')

        if not (valida_senha(senha, request)):
            return redirect('empresa_registro')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email já cadastrado')
            return redirect('empresa_registro')

        user = User.objects.create_user(username=email, email=email, first_name=nome, password=senha, is_empresa=False)
        user.save()
        messages.success(request, 'Cadastro realizado com sucesso, em breve ativaremos seu usuário ')
        return redirect('index')
    return render(request, 'empresa/empresa_registro.html')