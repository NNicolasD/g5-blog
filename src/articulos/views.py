from django.shortcuts import render
from django.views import generic
from .models import Articulo, Categoria
from .forms import CrearArticuloForm
from django.urls import reverse
from django.shortcuts import get_object_or_404

# Create your views here.

class CrearArticuloView(generic.CreateView):
    model = Articulo
    template_name = 'blog/create_article.html'
    form_class = CrearArticuloForm

    def get_success_url(self):
        return reverse('articulos:list-articles')

    def form_valid(self, form):
        f = form.save(commit=False)
        f.autor_id = self.request.user.id
        return super().form_valid(f)
    
class ListaArticulosView(generic.ListView):
    model = Articulo
    template_name = 'blog/articles.html'
    context_object_name = 'articulos'
    paginate_by = 25

class EditarArticuloView(generic.UpdateView):
    model = Articulo
    template_name = 'blog/edit_article.html'
    form_class = CrearArticuloForm

    def get_success_url(self):
        return reverse('articulos:list-articles')
    
class EliminarArticuloView(generic.DeleteView):
    model = Articulo
    template_name = 'blog/delete_article.html'

    def get_success_url(self):
        return reverse('articulos:list-articles')
    
class CategoryView(generic.TemplateView):
    template_name = 'blog/category.html'

    def get_context_data(self, **kwargs):
        category_slug = self.kwargs['category']
        category_obj = get_object_or_404(Categoria, nombre__iexact=category_slug.replace('-', ' '))
        category_article = Articulo.objects.filter(categoria=category_obj)
        context = super().get_context_data(**kwargs)
        context['category'] = category_obj.nombre
        context['category_article'] = category_article
        return context

class CategoryListView(generic.ListView):
    model = Categoria
    template_name = 'blog/category_list.html'
    context_object_name = 'category_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset