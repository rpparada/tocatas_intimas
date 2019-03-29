#from django.views.generic import TemplateView
from django.shortcuts import render
from tocatas.models import Tocata
from locacion.elecciones import regiones
from tocatas.elecciones import medios_pago, tipo_ti


def index(request):
    tocatas = Tocata.objects.order_by('-fecha').filter(tipo=2)[:6]
    context = {
        'tocatas': tocatas,
        'regiones': regiones,
        'medios_pago': medios_pago,
        'tipo': tipo_ti,
    }
    return render(request,'index.html',context)
