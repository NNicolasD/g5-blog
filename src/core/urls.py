from django.urls import path, include
from .views import *

app_name = 'blog'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/', include('articulos.urls')),
]