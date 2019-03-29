from django.shortcuts import render, get_object_or_404
from tocatas.models import Tocata, Asistencia
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
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
    queryset_list = Tocata.objects.order_by('-fecha')


    # Descripcion
    if 'palabra' in request.GET:
        palabra = request.GET['palabra']
        if palabra:
            queryset_list = queryset_list.filter(observaciones__icontains=palabra)


    context = {
        'regiones': regiones,
        'medios_pago': medios_pago,
        'tipo': tipo_ti,
        'tocatas': queryset_list,
        'valores':request.GET,
    }
    return render(request,'tocatas/busqueda.html', context)
