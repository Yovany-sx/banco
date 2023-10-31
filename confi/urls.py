from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import (
    ConfiguracionView,
)

app_name = 'confi'

urlpatterns = [
    path('list/', login_required(ConfiguracionView.as_view()), name='list'),
     #path('detalle/<int:pk>/', DetalleNoticia.as_view(), name='detalle'),
]
