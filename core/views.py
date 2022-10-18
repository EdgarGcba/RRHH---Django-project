from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import PostulanteForm

def inicio(request):
    return render(request, 'pages/inicio.html')
def nosotros(request):
    return render(request, 'pages/nosotros.html') 

def postulantes(request):
    postulantes = Postulante.objects.all()    
    return render(request, 'postulantes/index.html', {'postulantes': postulantes}) 

def crear(request):
    formulario = PostulanteForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('postulantes')
    return render(request, 'postulantes/crear.html', {'formulario':formulario})

def editar(request, id):
    postulante = Postulante.objects.get(id=id)
    formulario = PostulanteForm(request.POST or None, request.FILES or None, instance=postulante)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect ('postulantes')
    return render(request, 'postulantes/editar.html', {'formulario': formulario})

def eliminar(request, id):
    postulante = Postulante.objects.get(id=id)
    postulante.delete()
    return render(request, 'postulantes' )


# Create your views here.
