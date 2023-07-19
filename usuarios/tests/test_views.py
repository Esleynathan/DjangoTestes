from typing import Any
from django.test import TestCase
from django.test.client import Client
from django.urls import reverse
from ..models import Usuario

class ViewsTestCase(TestCase):

    def setUp(self):
        Usuario.objects.create(nome='esley', email='esley@gmail.com', senha="1234")


        self.client = Client()
        self.url = reverse('home')

    def test_status_code_200(self):
        responde = self.client.get(f'{self.url}?email=esley@gmail.com')

        self.assertEqual(responde.status_code, 200)