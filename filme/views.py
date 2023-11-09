from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Filme

class HomePage(TemplateView):
    template_name = 'homepage.html'

class HomeFilmes(ListView):
    template_name = 'homefilmes.html'
    model = Filme

class DetalhesFilme(DetailView):
    template_name = 'detalhesfilme.html'
    model = Filme
