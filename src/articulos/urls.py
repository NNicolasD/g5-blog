from django.urls import path
from .views import *

app_name = 'articulos'

urlpatterns = [
    path('create-article/', CrearArticuloView.as_view(), name='create-article'),
    path('list-articles/', ListaArticulosView.as_view(), name='list-articles'),
]