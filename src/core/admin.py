from django.contrib import admin
from .models import Contacto

# Register your models here.

class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo', 'mensaje')
    list_filter = ('nombre', 'correo')
    search_fields = ('nombre',)

admin.site.register(Contacto, ContactoAdmin)