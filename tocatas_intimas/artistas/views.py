from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q

from tocatas.models import Tocata, Asistencia
from artistas.models import Artista

from locacion.elecciones import regiones
from tocatas.elecciones import medios_pago, tipo_ti

# Create your views here.
def index(request):
    artistas = Artista.objects.all()
    paginator = Paginator(artistas, 10)
    page = request.GET.get('page')
    paged_artistas = paginator.get_page(page)
    context = {
        'artistas': paged_artistas
    }
    return render(request,'artistas/artistas.html', context)

def artista(request, artista_id):
    artista = get_object_or_404(Artista, pk=artista_id)
    context = {
        'artista': artista
    }
    return render(request,'artistas/artista.html', context)

def busqueda(request):

    queryset_list = Artista.objects.all()

    if 'palabra' in request.GET:
        palabra = request.GET['palabra']
        if palabra:
            queryset_list = queryset_list.filter(Q(descripcion__icontains=palabra) | Q(nombre__icontains=palabra))

    paginator = Paginator(queryset_list, 5)
    page = request.GET.get('page')
    paged_artistas = paginator.get_page(page)

    context = {
        'artistas': paged_artistas,
        'valores': request.GET,
    }

    return render(request,'artistas/busqueda_artista.html', context)
