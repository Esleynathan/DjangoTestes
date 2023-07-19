from django.test import TestCase
from ..models import Usuario

class UsuarioTestCase(TestCase):
    def setUp(self):
        Usuario.objects.create(nome='esley', email='esley@gmail.com', senha="1234")

    def test_models_criado_no_banco(self):
        usuario = Usuario.objects.get(nome = 'esley') 

        #self.assertEqual(x, y) # x == y
        #self.assertNotEqual(x, y) # x != y
        #self.assertTrue(x) #bool (x) is True
        #self.assertFalse(x) #bool (x) is False
        #self.assertIs(x, y) # x is y
        #self.assertIsNot(x, y) # x is not y
        #self.assertIsNone(x, y) # x is None
        #self.assertIn(x, y) # x in y
        #self.assertNotIn(x, y) # x in not y
        #self.assertIsInstance(x, y) # isinstance(x,y)
        #self.assertNotIsInstance(x, y) # not isinstance(x,y)

        #self.assertGreater(x, y) # x > y
        #self.assertGreaterEqual(x, y) # x >= y
        #self.assertLess(x, y) # x < y
        #self.assertLessEqual(x, y) # x <= y 

        
    def test_add_pontos(self):
        usuario = Usuario.objects.get(nome = 'esley')
        usuario.add_pontos()

        self.assertEqual(usuario.pontos, 10)
