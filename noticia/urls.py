from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import (
    NoticiaListView,
    DetalleNoticia
)

app_name = 'noticia'

urlpatterns = [
    path('list/', login_required(NoticiaListView.as_view()), name='list'),
     path('detalle/<int:pk>/', DetalleNoticia.as_view(), name='detalle'),
]
