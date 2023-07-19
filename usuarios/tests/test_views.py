from typing import Any
from django.test import TestCase
from django.test.client import Client
from django.urls import reverse

class ViewsTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('home')

    def test_status_code_200(self):
        responde = self.client.get(self.url)

        self.assertEqual(responde.status_code, 200)