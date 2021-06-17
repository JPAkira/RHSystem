from django.db import models

class Empresa(models.Model):
    nome = models.CharField(max_length=20)
