from django.test import TestCase

class UsuarioTestCase(TestCase):
    def test_um_e_um(self):
        self.assertEqual(1,2)

    def test_dois_e_dois(self):
        self.assertEqual(2,2)    