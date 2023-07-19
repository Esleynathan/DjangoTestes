from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
from django.shortcuts import get_object_or_404

def home(request):
    email = request.GET.get('email')

    cond = request.GET.get('cond')
    
    usuario = get_object_or_404(Usuario, email=email)

    if cond == '1':
        return render(request, 'home.html')
    else:
        return render(request, 'logar.html')

    #usuario = Usuario.objects.filter(email=email)