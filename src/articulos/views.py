from django.shortcuts import render
from django.views import generic
from .models import Articulo, Categoria, Comentario
from .forms import CrearArticuloForm, CrearComentarioForm
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect

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
    
class DetalleArticuloView(generic.DetailView):
    template_name = 'blog/detail_article.html'
    model = Articulo
    context_object_name = 'articulo'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)    
        context['formulario_comentario'] = CrearComentarioForm()
        return context       

    def post(self, request, *args, **kwargs):
        articulo = self.get_object()
        form = CrearComentarioForm(request.POST)

        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.user_id = self.request.user.id
            comentario.articulo = articulo
            comentario.save()
            return redirect('articulos:detail-article', pk=articulo.pk)
        else:
            return super().get(request)
        
class EditarComentarioView(generic.UpdateView):
    model = Comentario
    template_name = 'blog/edit_comment.html'     
    fields = ['texto']  
    
    def get_success_url(self):
        return reverse('articulos:detail-article', args = [self.object.articulo.id])
        
class EliminarComentarioView(generic.DeleteView):
    model = Comentario
    template_name = 'blog/delete_comment.html'       
    
    def get_success_url(self):
        return reverse('articulos:detail-article', args = [self.object.articulo.id])
    
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