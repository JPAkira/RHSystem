from django.contrib import messages
import re

def valida_nome(nome, request):
    valido = True

    if len(nome) < 2:
        messages.error(request, f'O campo de nome deve ter de 2 a 50 caracteres')
        valido = False
        return valido

    if len(nome) > 50:
        messages.error(request, f'O campo de nome deve ter de 2 a 50 caracteres')
        valido = False
        return valido

    if not re.match(r"^[A-Za-z0-9 záàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ]*$", nome):
        messages.error(request, 'Neste campo só é possivel adicionar letras e números')
        valido = False

    if not nome.strip():
        messages.error(request, 'Não pode campos em branco')
        valido = False

    return valido

def valida_senha(senha, request):
    valido = True

    if len(senha) < 8:
        messages.error(request, f'O campo de senha deve ter de 8 a 20 caracteres')
        valido = False
        return valido

    if len(senha) > 20:
        messages.error(request, f'O campo de senha deve ter de 8 a 20 caracteres')
        valido = False
        return valido

    if not re.match(r"^[A-Za-z0-9@_!#$%&]*$", senha):
        messages.error(request, 'Neste campo só é possivel adicionar letras e números e caracteres especiais')
        valido = False

    if not senha.strip():
        messages.error(request, 'Não pode campos em branco')
        valido = False

    return valido

def valida_email(email, request):
    valido = True

    if len(email) < 3:
        messages.error(request, 'O campo de email deve ter de 3 a 256 caracteres')
        valido = False
        return valido

    if len(email) > 256:
        messages.error(request, 'O campo de email deve ter de 3 a 256 caracteres')
        valido = False
        return valido

    if not re.match(r"^[A-Za-z0-9@_!#$%&.]*$", email):
        messages.error(request, 'Neste campo só é possivel adicionar letras e números')
        valido = False

    if not email.strip():
        messages.error(request, 'Não pode campos em branco')
        valido = False

    return valido
