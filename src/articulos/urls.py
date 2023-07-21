from django.urls import path
from .views import *

app_name = 'articulos'

urlpatterns = [
    path('create-article/', CrearArticuloView.as_view(), name='create-article'),
    path('list-articles/', ListaArticulosView.as_view(), name='list-articles'),
    path('edit-article/<int:pk>', EditarArticuloView.as_view(), name = 'edit-article'),
    path('delete-article/<int:pk>', EliminarArticuloView.as_view(), name = 'delete-article'),
    path('detail-article/<int:pk>', DetalleArticuloView.as_view(), name='detail-article'),
    path('edit-comment/<int:pk>', EditarComentarioView.as_view(), name = 'edit-comment'),
    path('delete-comment/<int:pk>', EliminarComentarioView.as_view(), name = 'delete-comment'),
    path('category/<str:category>/', CategoryView.as_view(), name='category'),
    path('category/', CategoryListView.as_view(), name='category-list'),
]