from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request, 'pages/inicio.html')
def nosotros(request):
    return render(request, 'pages/nosotros.html') 

def postulantes(request):
    return render(request, 'postulantes/index.html') 
def crear(request):
    return render(request, 'postulantes/crear.html' )
def editar(request):
    return render(request, 'postulantes/editar.html' )


# Create your views here.
