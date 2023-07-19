from django.test import TestCase
from ..models import Usuario

class UsuarioTestCase(TestCase):
    def setUp(self):
        Usuario.objects.create(nome='esley', email='esley@gmail.com', senha="1234")

    def test_models_criado_no_banco(self):
        usuario = Usuario.objects.get(nome = 'esley')

        self.assertEqual(usuario.__str__(), 'esley')
    
    def test_add_pontos(self):
        usuario = Usuario.objects.get(nome = 'esley')
        usuario.add_pontos()

        self.assertEqual(usuario.pontos, 10)
