from django.db import models

# Create your models here.
from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.conf import settings

User = settings.AUTH_USER_MODEL


class NombreEstado(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    activo = models.BooleanField(default=True)
    creacion = models.DateTimeField(auto_now_add=True)
    actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Categoria(NombreEstado):
    pass


class Etiqueta(NombreEstado):
    pass


class Articulo(models.Model):
    titulo = models.CharField(max_length=250)
    bajada = models.CharField(max_length=600)
    contenido = RichTextField()
    imagen = models.ImageField(upload_to='articulo', null=True)
    publicado = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    etiqueta = models.ManyToManyField(Etiqueta)

    creacion = models.DateTimeField(auto_now_add=True)
    actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-creacion']

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('articulos:detail-article', kwargs={ 'id': self.id })

    def get_comments(self):
        return self.comentario__set.all()
    
class Comentario(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    texto = models.CharField(max_length=500, blank=True, default="")
    
    creacion = models.DateTimeField(auto_now_add=True)
    actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-creacion']

    def __str__(self):
        return self.texto