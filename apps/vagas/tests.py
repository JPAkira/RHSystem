from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from apps.vagas.views import *
from vagas.models import Vaga, Requisitos, Desejavel
from candidato.models import Aplicacao, Experiencia
from django.contrib.auth import get_user_model
User = get_user_model()

class TestUrls(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('test', 'test@email.com', 'testtest', is_candidato=True)
        self.empresa = User.objects.create_user('testempresa', 'testempresa@email.com', 'testempresa', is_empresa=True)
        self.client.force_login(self.empresa)
        vaga = Vaga.objects.create(id=1, cargo="Teste", faixa_salarial="Teste", escolaridade="Teste", descricao="Teste", empresa=self.empresa)
        aplicacao = Aplicacao.objects.create(id=1, vaga=vaga, pretencao_salarial="Mais de 1000",
                                             escolaridade="Ensino Médio", candidato=self.user, score=8)
        Experiencia.objects.create(id=1, aplicacao=aplicacao, cargo="Teste", experiencia="Teste")
        Requisitos.objects.create(id=1, vaga=vaga, requisito="Teste")
        Desejavel.objects.create(id=1, vaga=vaga, desejavel="Teste")

    def test_vaga_url_is_resolved(self):
        url = self.client.get(reverse('vaga', args=(1,)), follow=True)
        self.assertEqual(url.status_code, 200)
        url = self.client.get(reverse('vaga', args=(2,)), follow=True)
        self.assertEqual(url.status_code, 404)

    def test_vaga_empresa_url_is_resolved(self):
        url = self.client.get(reverse('vaga_empresa', args=(1,)), follow=True)
        self.assertEqual(url.status_code, 200)
        url = self.client.get(reverse('vaga_empresa', args=(2,)), follow=True)
        self.assertEqual(url.status_code, 404)

    def test_ver_candidatos_url_is_resolved(self):
        url = self.client.get(reverse('vaga', args=(1,)), follow=True)
        self.assertEqual(url.status_code, 200)
        url = self.client.get(reverse('vaga', args=(2,)), follow=True)
        self.assertEqual(url.status_code, 404)

    def test_ver_experiencias_url_is_resolved(self):
        url = self.client.get(reverse('ver_experiencias', args=(1,)), follow=True)
        self.assertEqual(url.status_code, 200)
        url = self.client.get(reverse('ver_experiencias', args=(2,)), follow=True)
        self.assertEqual(url.status_code, 404)