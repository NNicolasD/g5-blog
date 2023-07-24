from django.views import generic
from django.contrib import messages
from django.shortcuts import redirect
from articulos.models import Articulo

class InicioView(generic.TemplateView):
    template_name = 'blog/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articulos'] = Articulo.objects.order_by('-creacion')[:3]
        return context
    
class AcercaDeNosotrosView(generic.TemplateView):
    template_name = 'blog/about.html'
    
class ContactoView(generic.TemplateView):
    template_name = 'blog/contact.html'

    def post(self, request, *args, **kwargs):
        messages.success(request, 'Mensaje enviado con éxito.')
        return redirect('blog:contact')