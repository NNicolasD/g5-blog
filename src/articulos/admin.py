from django.contrib import admin
from .models import Categoria, Articulo, Etiqueta, Comentario

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'activo')
    search_fields = ('nombre', 'descripcion')
    readonly_fields = ('get_sub_categories',)

    def get_sub_categories(self, instance):
        sub_categories = Categoria.get_sub_categories(instance)
        return ', '.join(str(category) for category in sub_categories)
    get_sub_categories.short_description = 'Sub Categorías'
    
class EtiquetaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'activo')
    list_filter = ('activo',)
    search_fields = ('nombre', 'activo')

class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'categoria', 'creacion', 'publicado')
    list_filter = ('autor', 'categoria', 'creacion', 'publicado')
    search_fields = ('titulo', 'resumen', 'articulo')
    readonly_fields = ('get_comments',)

    def get_comments(self, instance):
        comments = instance.get_comments()
        return ', '.join(str(comment) for comment in comments)
    get_comments.short_description = 'Comentarios'
    
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('texto', 'user', 'articulo', 'creacion')
    list_filter = ('user', 'articulo')
    search_fields = ('texto',)

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(Etiqueta, EtiquetaAdmin)
admin.site.register(Comentario, ComentarioAdmin)