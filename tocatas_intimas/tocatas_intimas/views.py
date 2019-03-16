from django.views.generic import TemplateView

class Index(TemplateView):
    print('hola')
    template_name = 'index.html'
