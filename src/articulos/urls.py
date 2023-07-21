from django.urls import path
from .views import *

app_name = 'articulos'

urlpatterns = [
    path('create-article/', CrearArticuloView.as_view(), name='create-article'),
    path('list-articles/', ListaArticulosView.as_view(), name='list-articles'),
    path('edit-article/<int:pk>', EditarArticuloView.as_view(), name = 'edit-article'),
    path('delete-article/<int:pk>', EliminarArticuloView.as_view(), name = 'delete-article'),
]