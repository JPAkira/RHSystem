from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from apps.index.views import *
from django.contrib.auth import get_user_model
User = get_user_model()

class TestUrls(TestCase):

    def test_index_url_is_resolved(self):
        url = self.client.get(reverse('index'))
        self.assertEqual(url.status_code, 200)

    def test_candidato_login_url_is_resolved(self):
        url = self.client.get(reverse('candidato_login'))
        self.assertEqual(url.status_code, 200)

    def test_empresa_login_url_is_resolved(self):
        url = self.client.get(reverse('empresa_login'))
        self.assertEqual(url.status_code, 200)

    def test_candidato_registro_url_is_resolved(self):
        url = self.client.get(reverse('candidato_registro'))
        self.assertEqual(url.status_code, 200)

    def test_empresa_registro_url_is_resolved(self):
        url = self.client.get(reverse('empresa_registro'))
        self.assertEqual(url.status_code, 200)

    def test_logout_url_is_resolved(self):
        url = self.client.get(reverse('logout'))
        self.assertEqual(url.status_code, 302)

    def test_logout(self):
        response = self.client.get(reverse('logout'))
        SimpleTestCase.assertRedirects(self, response, '/', status_code=302, target_status_code=200, msg_prefix='',
                                       fetch_redirect_response=True)

    def test_buscar_vagas_index_url_is_resolved(self):
        url = self.client.get(reverse('buscar_vagas_index'))
        self.assertEqual(url.status_code, 200)