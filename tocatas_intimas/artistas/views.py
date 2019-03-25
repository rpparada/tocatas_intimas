from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'artistas/artistas.html')

def tocata(request):
    return render(request,'artistas/artista.html')

def busqueda(request):
    return render(request,'artistas/busqueda.html')
