from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='locaciones'),
    path('<int:locacion_id>',views.locacion, name='locacion'),
]
