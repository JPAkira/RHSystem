from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from apps.candidato.views import *
from vagas.models import Vaga
from candidato.models import Aplicacao, Experiencia
from django.contrib.auth import get_user_model
User = get_user_model()

class TestUrls(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('test', 'test@email.com', 'testtest', is_candidato=True)
        self.empresa = User.objects.create_user('testempresa', 'testempresa@email.com', 'testempresa', is_empresa=True)
        self.client.force_login(self.user)
        vaga = Vaga.objects.create(id=1, cargo="Teste", faixa_salarial="Teste", escolaridade="Teste", descricao="Teste", empresa=self.empresa)
        aplicacao = Aplicacao.objects.create(id=1, vaga=vaga, pretencao_salarial="Mais de 1000",
                                             escolaridade="Ensino Médio", candidato=self.user, score=8)
        Experiencia.objects.create(id=1, aplicacao=aplicacao, cargo="Teste", experiencia="Teste")

    def test_aplicacao_url_is_resolved(self):
        url = self.client.get(reverse('aplicacao', args=(1,)), follow=True)
        self.assertEqual(url.status_code, 200)
        url = self.client.get(reverse('aplicacao', args=(2,)), follow=True)
        self.assertEqual(url.status_code, 404)

    def test_adicionar_experiencia_url_is_resolved(self):
        url = self.client.get(reverse('adicionar_experiencia', args=(1,)), follow=True)
        self.assertEqual(url.status_code, 200)
        url = self.client.get(reverse('adicionar_experiencia', args=(2,)), follow=True)
        self.assertEqual(url.status_code, 404)

    def test_conhecimentos_candidato_url_is_resolved(self):
        url = self.client.get(reverse('conhecimentos_candidato', args=(1,)), follow=True)
        self.assertEqual(url.status_code, 200)
        url = self.client.get(reverse('conhecimentos_candidato', args=(2,)), follow=True)
        self.assertEqual(url.status_code, 404)

    def test_conhecimentos_candidato_desejavel_url_is_resolved(self):
        url = self.client.get(reverse('conhecimentos_candidato_desejavel', args=(1,)), follow=True)
        self.assertEqual(url.status_code, 200)
        url = self.client.get(reverse('conhecimentos_candidato_desejavel', args=(2,)), follow=True)
        self.assertEqual(url.status_code, 404)

    def test_deletar_experiencia_url_is_resolved(self):
        url = self.client.get(reverse('deletar_experiencia', args=(1,)), follow=True)
        self.assertEqual(url.status_code, 200)
        url = self.client.get(reverse('deletar_experiencia', args=(2,)), follow=True)
        self.assertEqual(url.status_code, 404)

    def test_minhas_aplicacoes_url_is_resolved(self):
        url = self.client.get(reverse('minhas_aplicacoes'))
        self.assertEqual(url.status_code, 200)

    def test_buscar_vagas_candidato_url_is_resolved(self):
        url = self.client.get(reverse('buscar_vagas_candidato'))
        self.assertEqual(url.status_code, 200)

    def test_redirect_deletar_experiencia(self):
        response = self.client.get(reverse('deletar_experiencia', args=(1,)), follow=True)
        SimpleTestCase.assertRedirects(self, response, '/candidato/adicionar-experiencia/1', status_code=302, target_status_code=200, msg_prefix='',
                                       fetch_redirect_response=True)

    def teste_se_empresa_pode_deletar_experiencia_do_candidato(self):
        self.client.force_login(self.empresa)
        response = self.client.get(reverse('deletar_experiencia', args=(1,)), follow=True)
        SimpleTestCase.assertRedirects(self, response, '/candidato/login', status_code=302, target_status_code=200, msg_prefix='',
                                       fetch_redirect_response=True)

    def teste_se_empresa_pode_acessar_vagas_do_candidato(self):
        self.client.force_login(self.empresa)
        response = self.client.get(reverse('minhas_aplicacoes'))
        SimpleTestCase.assertRedirects(self, response, '/candidato/login', status_code=302, target_status_code=200, msg_prefix='',
                                       fetch_redirect_response=True)

    def teste_se_empresa_pode_acessar_busca_de_vagas_do_candidato(self):
        self.client.force_login(self.empresa)
        response = self.client.get(reverse('buscar_vagas_candidato'))
        SimpleTestCase.assertRedirects(self, response, '/candidato/login', status_code=302, target_status_code=200, msg_prefix='',
                                       fetch_redirect_response=True)

    def teste_se_usuario_anonimo_pode_deletar_experiencia_do_candidato(self):
        self.client.logout()
        response = self.client.get(reverse('deletar_experiencia', args=(1,)), follow=True)
        SimpleTestCase.assertRedirects(self, response, '/candidato/login', status_code=302, target_status_code=200, msg_prefix='',
                                       fetch_redirect_response=True)

    def teste_se_usuario_anonimo_pode_acessar_vagas_do_candidato(self):
        self.client.logout()
        response = self.client.get(reverse('minhas_aplicacoes'))
        SimpleTestCase.assertRedirects(self, response, '/candidato/login', status_code=302, target_status_code=200, msg_prefix='',
                                       fetch_redirect_response=True)

    def teste_se_usuario_anonimo_pode_acessar_busca_de_vagas_do_candidato(self):
        self.client.logout()
        response = self.client.get(reverse('buscar_vagas_candidato'))
        SimpleTestCase.assertRedirects(self, response, '/candidato/login', status_code=302, target_status_code=200, msg_prefix='',
                                       fetch_redirect_response=True)