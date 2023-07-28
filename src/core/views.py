from django.views import generic
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from articulos.models import Articulo
from core.models import Contacto
from .forms import ContactoForm

class InicioView(generic.TemplateView):
    template_name = 'blog/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articulos'] = Articulo.objects.order_by('-creacion')[:3]
        return context
    
class AcercaDeNosotrosView(generic.TemplateView):
    template_name = 'blog/about.html'
    
class ContactoView(generic.CreateView):
    model = Contacto
    form_class = ContactoForm
    template_name = 'blog/contact.html'
    
    def get_success_url(self):
        return reverse('blog:contact')

    def form_valid(self, form):
        messages.success(self.request, 'Mensaje enviado con éxito.')
        return super().form_valid(form)