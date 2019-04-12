from django.urls import path

from . import views

urlpatterns = [
    path('ingresar_registrar',views.ingresar_registrar, name='ingresar_registrar'),
    path('micuenta',views.micuenta, name='micuenta'),
    path('salir',views.salir, name='salir'),
]
