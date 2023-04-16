from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'recipes/home.html', context={'name': 'Lucas Mateus Sousa Sales'})


def contato(request):
    return render(request, 'temp/temp.html')


def sobre(request):
    return HttpResponse('Sobre')
