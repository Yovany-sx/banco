from django.contrib.auth.models import User
from django.core import validators
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def contenido_formateado(self):
        return format_html(self.contenido)
    
    def __str__(self):
        return self.titulo