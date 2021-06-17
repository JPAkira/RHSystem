from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from apps.empresa.views import *
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

    def test_home_url_is_resolved(self):
        url = self.client.get(reverse('home'))
        self.assertEqual(url.status_code, 200)

    def test_minhas_vagas_url_is_resolved(self):
        url = self.client.get(reverse('minhas_vagas'))
        self.assertEqual(url.status_code, 200)

    def test_criar_vaga_url_is_resolved(self):
        url = self.client.get(reverse('criar_vaga'))
        self.assertEqual(url.status_code, 200)

    def test_editar_vaga_url_is_resolved(self):
        url = self.client.get(reverse('editar_vaga', args=(1,)), follow=True)
        self.assertEqual(url.status_code, 200)
        url = self.client.get(reverse('editar_vaga', args=(2,)), follow=True)
        self.assertEqual(url.status_code, 404)

    def test_adicionar_requisitos_url_is_resolved(self):
        url = self.client.get(reverse('adicionar_requisitos', args=(1,)), follow=True)
        self.assertEqual(url.status_code, 200)
        url = self.client.get(reverse('adicionar_requisitos', args=(2,)), follow=True)
        self.assertEqual(url.status_code, 404)

    def test_deletar_requisito_url_is_resolved(self):
        url = self.client.get(reverse('deletar_requisito', args=(1,)), follow=True)
        self.assertEqual(url.status_code, 200)
        url = self.client.get(reverse('deletar_requisito', args=(2,)), follow=True)
        self.assertEqual(url.status_code, 404)

    def test_adicionar_desejavel_url_is_resolved(self):
        url = self.client.get(reverse('adicionar_desejavel', args=(1,)), follow=True)
        self.assertEqual(url.status_code, 200)
        url = self.client.get(reverse('adicionar_desejavel', args=(2,)), follow=True)
        self.assertEqual(url.status_code, 404)

    def test_deletar_desejavel_url_is_resolved(self):
        url = self.client.get(reverse('deletar_desejavel', args=(1,)), follow=True)
        self.assertEqual(url.status_code, 200)
        url = self.client.get(reverse('deletar_desejavel', args=(2,)), follow=True)
        self.assertEqual(url.status_code, 404)

    def test_deletar_vaga_url_is_resolved(self):
        url = self.client.get(reverse('deletar_vaga', args=(1,)), follow=True)
        self.assertEqual(url.status_code, 200)
        url = self.client.get(reverse('deletar_vaga', args=(2,)), follow=True)
        self.assertEqual(url.status_code, 404)

    def test_buscar_vagas_empresa_url_is_resolved(self):
        url = self.client.get(reverse('buscar_vagas_empresa'))
        self.assertEqual(url.status_code, 200)

    def test_usuario_anonimo_deletar_vaga(self):
        self.client.logout()
        response = self.client.get(reverse('deletar_vaga', args=(1,)), follow=True)
        SimpleTestCase.assertRedirects(self, response, '/empresa/login', status_code=302, target_status_code=200, msg_prefix='',
                                       fetch_redirect_response=True)

    def test_usuario_anonimo_acessar_home(self):
        self.client.logout()
        response = self.client.get(reverse('home'))
        SimpleTestCase.assertRedirects(self, response, '/empresa/login', status_code=302, target_status_code=200, msg_prefix='',
                                       fetch_redirect_response=True)

    def test_usuario_anonimo_acessar_minhas_vagas(self):
        self.client.logout()
        response = self.client.get(reverse('minhas_vagas'))
        SimpleTestCase.assertRedirects(self, response, '/empresa/login', status_code=302, target_status_code=200, msg_prefix='',
                                       fetch_redirect_response=True)

    def test_usuario_anonimo_acessar_criar_vaga(self):
        self.client.logout()
        response = self.client.get(reverse('criar_vaga'))
        SimpleTestCase.assertRedirects(self, response, '/empresa/login', status_code=302, target_status_code=200, msg_prefix='',
                                       fetch_redirect_response=True)

    def test_usuario_anonimo_acessar_editar_vaga(self):
        self.client.logout()
        response = self.client.get(reverse('editar_vaga', args=(1,)), follow=True)
        SimpleTestCase.assertRedirects(self, response, '/empresa/login', status_code=302, target_status_code=200, msg_prefix='',
                                       fetch_redirect_response=True)

    def test_usuario_anonimo_acessar_adicionar_requisitos(self):
        self.client.logout()
        response = self.client.get(reverse('adicionar_requisitos', args=(1,)), follow=True)
        SimpleTestCase.assertRedirects(self, response, '/empresa/login', status_code=302, target_status_code=200, msg_prefix='',
                                       fetch_redirect_response=True)

    def test_usuario_anonimo_deletar_requisito(self):
        self.client.logout()
        response = self.client.get(reverse('deletar_requisito', args=(1,)), follow=True)
        SimpleTestCase.assertRedirects(self, response, '/empresa/login', status_code=302, target_status_code=200, msg_prefix='',
                                       fetch_redirect_response=True)

    def test_usuario_anonimo_acessar_adicionar_desejavel(self):
        self.client.logout()
        response = self.client.get(reverse('adicionar_desejavel', args=(1,)), follow=True)
        SimpleTestCase.assertRedirects(self, response, '/empresa/login', status_code=302, target_status_code=200, msg_prefix='',
                                       fetch_redirect_response=True)

    def test_usuario_anonimo_deletar_desejavel(self):
        self.client.logout()
        response = self.client.get(reverse('deletar_desejavel', args=(1,)), follow=True)
        SimpleTestCase.assertRedirects(self, response, '/empresa/login', status_code=302, target_status_code=200, msg_prefix='',
                                       fetch_redirect_response=True)

    def test_usuario_anonimo_acessar_buscar_vagas_empresa(self):
        self.client.logout()
        response = self.client.get(reverse('buscar_vagas_empresa'))
        SimpleTestCase.assertRedirects(self, response, '/empresa/login', status_code=302, target_status_code=200, msg_prefix='',
                                       fetch_redirect_response=True)

    def test_usuario_candidato_deletar_vaga(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('deletar_vaga', args=(1,)), follow=True)
        SimpleTestCase.assertRedirects(self, response, '/empresa/login', status_code=302, target_status_code=200,
                                       msg_prefix='',
                                       fetch_redirect_response=True)

    def test_usuario_candidato_acessar_home(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('home'))
        SimpleTestCase.assertRedirects(self, response, '/empresa/login', status_code=302, target_status_code=200,
                                       msg_prefix='',
                                       fetch_redirect_response=True)

    def test_usuario_candidato_acessar_minhas_vagas(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('minhas_vagas'))
        SimpleTestCase.assertRedirects(self, response, '/empresa/login', status_code=302, target_status_code=200,
                                       msg_prefix='',
                                       fetch_redirect_response=True)

    def test_usuario_candidato_acessar_criar_vaga(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('criar_vaga'))
        SimpleTestCase.assertRedirects(self, response, '/empresa/login', status_code=302, target_status_code=200,
                                       msg_prefix='',
                                       fetch_redirect_response=True)

    def test_usuario_candidato_acessar_editar_vaga(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('editar_vaga', args=(1,)), follow=True)
        SimpleTestCase.assertRedirects(self, response, '/empresa/login', status_code=302, target_status_code=200,
                                       msg_prefix='',
                                       fetch_redirect_response=True)

    def test_usuario_candidato_acessar_adicionar_requisitos(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('adicionar_requisitos', args=(1,)), follow=True)
        SimpleTestCase.assertRedirects(self, response, '/empresa/login', status_code=302, target_status_code=200,
                                       msg_prefix='',
                                       fetch_redirect_response=True)

    def test_usuario_candidato_deletar_requisito(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('deletar_requisito', args=(1,)), follow=True)
        SimpleTestCase.assertRedirects(self, response, '/empresa/login', status_code=302, target_status_code=200,
                                       msg_prefix='',
                                       fetch_redirect_response=True)

    def test_usuario_candidato_acessar_adicionar_desejavel(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('adicionar_desejavel', args=(1,)), follow=True)
        SimpleTestCase.assertRedirects(self, response, '/empresa/login', status_code=302, target_status_code=200,
                                       msg_prefix='',
                                       fetch_redirect_response=True)

    def test_usuario_candidato_deletar_desejavel(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('deletar_desejavel', args=(1,)), follow=True)
        SimpleTestCase.assertRedirects(self, response, '/empresa/login', status_code=302, target_status_code=200,
                                       msg_prefix='',
                                       fetch_redirect_response=True)

    def test_usuario_candidato_acessar_buscar_vagas_empresa(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('buscar_vagas_empresa'))
        SimpleTestCase.assertRedirects(self, response, '/empresa/login', status_code=302, target_status_code=200,
                                       msg_prefix='',
                                       fetch_redirect_response=True)