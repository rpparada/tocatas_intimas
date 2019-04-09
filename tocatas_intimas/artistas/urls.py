from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='artistas'),
    path('<int:artista_id>',views.artista, name='artista'),
    path('busqueda_artista',views.busqueda, name='busqueda_artista'),
]
