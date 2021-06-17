from django.urls import path
from apps.vagas.views import *

urlpatterns = [
    path('vagas/vaga/<int:vaga_id>', vaga, name='vaga'),
    path('vagas/vaga-empresa/<int:vaga_id>', vaga_empresa, name='vaga_empresa'),
    path('vagas/ver-candidatos/<int:vaga_id>', ver_candidatos, name='ver_candidatos'),
    path('vagas/buscar-candidatos/<int:vaga_id>', buscar_candidatos_vaga, name='buscar_candidatos_vaga'),
    path('vagas/ver-experiencias/<int:aplicacao_id>', ver_experiencias, name='ver_experiencias'),
]