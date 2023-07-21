from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('create-article/', CrearArticuloView.as_view(), name='create-article'),
]