from django.urls import path
from apps.candidato.views import *

urlpatterns = [
    path('candidato/aplicar/<int:vaga_id>', aplicacao, name='aplicacao'),
    path('candidato/adicionar-experiencia/<int:aplicacao_id>', adicionar_experiencia, name='adicionar_experiencia'),
    path('candidato/conhecimentos-candidato/<int:aplicacao_id>', conhecimentos_candidato, name='conhecimentos_candidato'),
    path('candidato/conhecimentos-candidato-desejavel/<int:aplicacao_id>', conhecimentos_candidato_desejavel, name='conhecimentos_candidato_desejavel'),
    path('candidato/deletar-experiencia/<int:experiencia_id>', deletar_experiencia, name='deletar_experiencia'),
    path('candidato/minhas-vagas/', minhas_aplicacoes, name='minhas_aplicacoes'),
    path('candidato/buscar/', buscar_vagas_candidato, name='buscar_vagas_candidato'),
]
