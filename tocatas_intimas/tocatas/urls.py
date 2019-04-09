from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='tocatas'),
    path('<int:tocata_id>',views.tocata, name='tocata'),
    path('busqueda_tocata',views.busqueda, name='busqueda_tocata'),
]
