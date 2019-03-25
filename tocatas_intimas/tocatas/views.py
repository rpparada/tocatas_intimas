from django.shortcuts import render
from tocatas.models import Tocata, Asistencia
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
def index(request):
    # tocatas = Tocata.objects.all()
    tocatas = Tocata.objects.order_by('fecha').filter(tipo=2)
    paginator = Paginator(tocatas, 2)
    page = request.GET.get('page')
    paged_tocatas = paginator.get_page(page)
    context = {
        'tocatas': paged_tocatas
    }
    return render(request,'tocatas/tocatas.html', context)

def tocata(request, tocata_id):
    return render(request,'tocatas/tocata.html')

def busqueda(request):
    return render(request,'tocatas/busqueda.html')
