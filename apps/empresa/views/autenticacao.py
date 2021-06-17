
def autenticacao(request):
    '''Autenticando o acesso a pagina'''

    autenticado = True

    if not request.user.is_authenticated:
        autenticado = False
        return autenticado
    if not request.user.is_empresa:
        autenticado = False
        return autenticado

    return autenticado
