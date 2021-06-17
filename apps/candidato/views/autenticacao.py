from candidato.models import Aplicacao
from django.contrib import messages


def autenticacao(request):
    '''Autenticando o acesso a pagina'''

    autenticado = True

    if not request.user.is_authenticated:
        autenticado = False
        return autenticado
    if not request.user.is_candidato:
        autenticado = False
        return autenticado

    return autenticado


def autenticacao_duplicidade_aplicacao(request, vaga_id):
    candidato_logado = request.user

    aplicacao_existe = Aplicacao.objects.filter(vaga__id=vaga_id, candidato__id=candidato_logado.id)

    autenticado = True

    if aplicacao_existe.count() > 0:
        messages.error(request, 'Você não pode aplicar duas vezes para a mesma vaga')
        autenticado = False
        return autenticado

    return autenticado
