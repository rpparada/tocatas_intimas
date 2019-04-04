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
    # tocatas = Tocata.objects.order_by('fecha').filter(tipo=2)
    paginator = Paginator(tocatas, 2)
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
    queryset_list_tocata = Tocata.objects.all()
    queryset_list_artista = Artista.objects.all()

    if 'palabra' in request.GET:
        palabra = request.GET['palabra']
        if palabra:
            queryset_list_tocata = queryset_list_tocata.filter(Q(observaciones__icontains=palabra) | Q(nombre__icontains=palabra))
            queryset_list_artista = queryset_list_artista.filter(Q(nombre__icontains=palabra) | Q(descripcion__icontains=palabra))

    context = {
        'regiones': regiones,
        'medios_pago': medios_pago,
        'tipo': tipo_ti,
        'tocatas': queryset_list_tocata,
        'artistas': queryset_list_artista,
        'valores':request.GET,
    }
    return render(request,'tocatas/busqueda.html', context)
