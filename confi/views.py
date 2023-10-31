from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView, DetailView, TemplateView

class ConfiguracionView(TemplateView):
    template_name = 'confi/confi.html'
