from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
from django.shortcuts import get_object_or_404

def home(request):
    email = request.GET.get('email')

    usuario = get_object_or_404(Usuario, email=email)
    #usuario = Usuario.objects.filter(email=email)

    return HttpResponse('Teste')
