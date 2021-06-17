from django.db import models
from django.contrib.auth import get_user_model
from vagas.models import Vaga
User = get_user_model()

class Aplicacao(models.Model):
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE)
    candidato = models.ForeignKey(User, on_delete=models.CASCADE)
    pretencao_salarial = models.CharField(max_length=25)
    escolaridade = models.CharField(max_length=25)
    score = models.IntegerField()
    data_criacao = models.DateTimeField(auto_now_add=True)

class Experiencia(models.Model):
    aplicacao = models.ForeignKey(Aplicacao, on_delete=models.CASCADE)
    cargo = models.CharField(max_length=30)
    experiencia = models.CharField(max_length=400)
