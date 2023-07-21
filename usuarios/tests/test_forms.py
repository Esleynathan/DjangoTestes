from django.test import TestCase
from ..forms import FormUsuario

class FormTestCase(TestCase):

    def setUp(self):
        self.form = FormUsuario()


    def test_campos_form(self):
        self.assertIn('nome', self.form.fields)
        self.assertIn('email', self.form.fields)
        self.assertIn('senha', self.form.fields)
        self.assertIn('pontos', self.form.fields)
        
