from django.shortcuts import render
from django.http import HttpResponse
from django.utils.html import escape

# Create your views here.

def home(request):
    return render(request, 'index.html')

def cadastrar(request):
    return render(request, 'cadastrar.html', {})
    
def cadastrar_evento(request):
	return render(request, 'cadastrar_evento.html', {})
