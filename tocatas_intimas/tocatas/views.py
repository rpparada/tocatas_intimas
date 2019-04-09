from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q

from tocatas.models import Tocata, Asistencia
from artistas.models import Artista

from locacion.elecciones import regiones
from tocatas.elecciones import medios_pago, tipo_ti


# Create your views here.
def index(request):
    tocatas = Tocata.objects.all()
    paginator = Paginator(tocatas, 10)
    page = request.GET.get('page')
    paged_tocatas = paginator.get_page(page)
    context = {
        'tocatas': paged_tocatas
    }
    return render(request,'tocatas/tocatas.html', context)

def tocata(request, tocata_id):
    tocata = get_object_or_404(Tocata, pk=tocata_id)
    context = {
        'tocata': tocata
    }
    return render(request,'tocatas/tocata.html', context)

def busqueda(request):

    queryset_list = Tocata.objects.all()

    if 'palabra' in request.GET:
        palabra = request.GET['palabra']
        if palabra:
            queryset_list = queryset_list.filter(Q(observaciones__icontains=palabra) | Q(nombre__icontains=palabra) | Q(artista__nombre__icontains=palabra))

    paginator = Paginator(queryset_list, 5)
    page = request.GET.get('page')
    paged_tocatas = paginator.get_page(page)

    context = {
        'tocatas': paged_tocatas,
        'valores': request.GET,
    }
    return render(request,'tocatas/busqueda_tocata.html', context)
