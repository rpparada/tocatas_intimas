from django.contrib import admin
from .models import Tocata, Asistencia

# Register your models here.

class TocataAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','artista','fecha','adhesion','tipo','direccion')
    list_display_links = ('id','artista')
    list_filter = ('artista',)
    list_editable = ('tipo',)
    search_fields = ('nombre',)
    list_per_page = 10

admin.site.register(Tocata, TocataAdmin)

class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ('id','tocata','asistente','evaluacion')

admin.site.register(Asistencia, AsistenciaAdmin)
