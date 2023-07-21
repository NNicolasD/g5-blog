from django.views import generic

class InicioView(generic.TemplateView):
    template_name = 'blog/home.html'
    
class AcercaDeNosotrosView(generic.TemplateView):
    template_name = 'blog/about.html'