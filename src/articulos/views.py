from django.shortcuts import render
from django.views import generic
from .models import Articulo
from .forms import CrearArticuloForm
from django.urls import reverse

# Create your views here.

class CrearArticuloView(generic.CreateView):
    model = Articulo
    template_name = 'blog/create_article.html'
    form_class = CrearArticuloForm

    def get_success_url(self):
        return reverse('blog:home')

    def form_valid(self, form):
        f = form.save(commit=False)
        f.autor_id = self.request.user.id
        return super().form_valid(f)