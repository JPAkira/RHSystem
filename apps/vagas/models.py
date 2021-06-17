from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Vaga(models.Model):
    cargo = models.CharField(max_length=40)
    empresa = models.ForeignKey(User, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=200)
    faixa_salarial = models.CharField(max_length=40)
    escolaridade = models.CharField(max_length=20)
    data_criacao = models.DateTimeField(auto_now_add=True)


class Requisitos(models.Model):
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE)
    requisito = models.CharField(max_length=40)


class Desejavel(models.Model):
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE)
    desejavel = models.CharField(max_length=40)
