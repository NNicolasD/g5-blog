from django.views import generic
from .models import Articulo, Categoria, Comentario
from .forms import CrearArticuloForm, CrearComentarioForm, CrearCategoriaForm, EditarComentarioForm
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import ArticulosMixin

# Create your views here.

class CrearArticuloView(ArticulosMixin, LoginRequiredMixin, generic.CreateView):
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all() 
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        categoria = self.request.GET.get('categoria')
        antiguedad = self.request.GET.get('antiguedad')
        orden = self.request.GET.get('orden')

        if categoria:
            queryset = queryset.filter(categoria__nombre__iexact=categoria)

        if antiguedad:
            if antiguedad == 'asc':
                queryset = queryset.order_by('creacion')
            elif antiguedad == 'desc':
                queryset = queryset.order_by('-creacion')

        if orden:
            if orden == 'asc':
                queryset = queryset.order_by('titulo')
            elif orden == 'desc':
                queryset = queryset.order_by('-titulo')

        return queryset

class EditarArticuloView(ArticulosMixin, LoginRequiredMixin, generic.UpdateView):
    model = Articulo
    template_name = 'blog/edit_article.html'
    form_class = CrearArticuloForm

    def get_success_url(self):
        return reverse('articulos:list-articles')
    
class EliminarArticuloView(ArticulosMixin, LoginRequiredMixin, generic.DeleteView):
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
        context['formularios_editar_comentario'] = {comentario.id: EditarComentarioForm(instance=comentario) for comentario in self.object.comentario_set.all()}
        return context       

    def post(self, request, *args, **kwargs):
        articulo = self.get_object()
        
        if 'eliminar_imagen' in request.POST and (request.user.is_superuser or request.user.es_colaborador):
            if articulo.imagen:
                articulo.imagen.delete(save=True)
                return redirect('articulos:detail-article', pk=articulo.pk)

        if 'crear_comentario' in request.POST:
            form = CrearComentarioForm(request.POST)
            if form.is_valid():
                comentario = form.save(commit=False)
                comentario.user_id = self.request.user.id
                comentario.articulo = articulo
                comentario.save()
                return redirect('articulos:detail-article', pk=articulo.pk)
        
        elif 'editar_comentario' in request.POST:
            comentario_id = request.POST.get('comentario_id')
            comentario = get_object_or_404(Comentario, id=comentario_id)
            form = EditarComentarioForm(request.POST, instance=comentario)
            if form.is_valid():
                form.save()
                return redirect('articulos:detail-article', pk=articulo.pk)
            
        if 'eliminar_comentario' in request.POST:
            comentario_id = request.POST.get('comentario_id')
            comentario = get_object_or_404(Comentario, id=comentario_id)
            comentario.delete()

            return redirect('articulos:detail-article', pk=articulo.pk)

        return super().get(request)
        
    
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
    
class CrearCategoriaView(ArticulosMixin, LoginRequiredMixin, generic.CreateView):
    model = Categoria
    template_name = 'blog/create_category.html'
    form_class = CrearCategoriaForm

    def get_success_url(self):
        return reverse('articulos:category-list')
    
class EditarCategoriaView(ArticulosMixin, LoginRequiredMixin, generic.UpdateView):
    model = Categoria
    template_name = 'blog/edit_category.html'
    form_class = CrearCategoriaForm
    
    def get_success_url(self):
        return reverse('articulos:category-list') 
    
class EliminarCategoriaView(ArticulosMixin, LoginRequiredMixin, generic.DeleteView):
    model = Categoria
    template_name = 'blog/delete_category.html'

    def get_success_url(self):
        return reverse('articulos:category-list')