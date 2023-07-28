from django.db import models

# Create your models here.

class Contacto(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    nombre = models.CharField(max_length=60)
    correo = models.EmailField()
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre