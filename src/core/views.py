from django.views import generic
from django.contrib import messages
from django.shortcuts import redirect

class InicioView(generic.TemplateView):
    template_name = 'blog/home.html'
    
class AcercaDeNosotrosView(generic.TemplateView):
    template_name = 'blog/about.html'
    
class ContactoView(generic.TemplateView):
    template_name = 'blog/contact.html'

    def post(self, request, *args, **kwargs):
        messages.success(request, 'Mensaje enviado con éxito.')
        return redirect('blog:contact')