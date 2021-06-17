from django.urls import path
from apps.index.views import *

urlpatterns = [
    path('', index, name='index'),
    path('candidato/login', candidato_login, name='candidato_login'),
    path('candidato/registro', candidato_registro, name='candidato_registro'),
    path('empresa/login', empresa_login, name='empresa_login'),
    path('empresa/registro', empresa_registro, name='empresa_registro'),
    path('logout', logout, name='logout'),
    path('buscar', buscar_vagas_index, name='buscar_vagas_index'),
]