from django.shortcuts import render, get_object_or_404
from .models import Noticia
from .forms import NoticiaForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView, DetailView

class NoticiaListView(ListView):
    model = Noticia
    form_class = NoticiaForm
    template_name = 'noticia/lista_noticias.html'
    success_url = reverse_lazy('noticia:list')

    def get_queryset(self):
        queryset = Noticia.objects.all()
        return queryset
    
class DetalleNoticia(DetailView):
    model = Noticia
    template_name = 'noticia/detalle_noticia.html'
    context_object_name = 'noticia'
    
    def get_queryset(self):
        queryset = Noticia.objects.all()
        return queryset
    