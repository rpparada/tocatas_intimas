from django.urls import path

from . import views

urlpatterns = [
    path('ingresar',views.ingresar, name='ingresar'),
    path('registrar',views.registrar, name='registrar'),
    path('salir',views.salir, name='salir'),
    path('micuenta',views.micuenta, name='micuenta'),
]
