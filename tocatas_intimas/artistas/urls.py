from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='artistas'),
    path('<int:artista_id>',views.tocata, name='artista'),
    #path('busqueda',views.busqueda, name='busqueda'),
]
