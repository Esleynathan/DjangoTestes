from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    id = request.GET.get('id')
    if id == '1':
        return HttpResponse('Teste')
    else:
        return HttpResponse(status=500)