from django.contrib import messages
import re

def valida_pretencao_salarial(pretencao_salarial, request):

    valido = True

    faixas_salariais = [
        'Até 1.000', 'De 1.000 a 2.000', 'De 2.000 a 3.000',
        'Acima de 3.000']

    if pretencao_salarial not in faixas_salariais:
        messages.error(request, 'Selecione uma faixa salarial')
        valido = False
        return valido

    return valido

def valida_escolaridade(escolaridade, request):

    valido = True

    escolaridades = [
        'Ensino fundamental', 'Ensino médio', 'Tecnólogo', 'Ensino superior',
        'Pós / MBA / Mestrado', 'Doutorado'
    ]

    if escolaridade not in escolaridades:
        messages.error(request, 'Selecione uma escolaridade')
        valido = False
        return valido

    return valido

def valida_campo_texto(texto, campo, maximo, request):
    valido = True

    if len(texto) < 3:
        messages.error(request, f'O campo de {campo} deve ter de 3 a {maximo} caracteres')
        valido = False
        return valido

    if len(texto) > maximo:
        messages.error(request, f'O campo de {campo} deve ter de 3 a {maximo} caracteres')
        valido = False
        return valido

    if not re.match(r"^[A-Za-z0-9 záàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ.,]*$", texto):
        messages.error(request, 'Neste campo só é possivel adicionar letras e números')
        valido = False

    if not texto.strip():
        messages.error(request, 'Não pode campos em branco')
        valido = False

    return valido