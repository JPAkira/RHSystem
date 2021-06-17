from django.urls import path
from apps.empresa.views import *

urlpatterns = [
    path('empresa/home', home, name='home'),
    path('empresa/minhas-vagas', minhas_vagas, name='minhas_vagas'),
    path('empresa/criar-vaga', criar_vaga, name='criar_vaga'),
    path('empresa/editar-vaga/<int:vaga_id>', editar_vaga, name='editar_vaga'),
    path('empresa/adicionar-requisitos/<int:vaga_id>', adicionar_requisitos, name='adicionar_requisitos'),
    path('empresa/deletar-requisito/<int:requisito_id>', deletar_requisito, name='deletar_requisito'),
    path('empresa/adicionar-desejavel/<int:vaga_id>', adicionar_desejavel, name='adicionar_desejavel'),
    path('empresa/deletar-desejavel/<int:desejavel_id>', deletar_desejavel, name='deletar_desejavel'),
    path('empresa/deletar-vaga/<int:vaga_id>', deletar_vaga, name='deletar_vaga'),
    path('empresa/buscar', buscar_vagas_empresa, name='buscar_vagas_empresa'),
]