from django.http import Http404
from django.shortcuts import redirect, reverse
from django.views.generic import UpdateView, ListView, DetailView, FormView
from .models import Filme, Usuario
from .forms import CriarContaForm, AcessarForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class HomePage(FormView):
    template_name = 'homepage.html'
    form_class = AcessarForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('filme:homefilmes')
        else:
            return super().get(request, *args, **kwargs)
        
    def get_success_url(self):
        email = self.request.POST.get('email')
        usuario = Usuario.objects.filter(email=email)
        if usuario:
            return reverse('filme:login')
        else:
            return reverse('filme:criarconta')

class HomeFilmes(LoginRequiredMixin, ListView):
    template_name = 'homefilmes.html'
    model = Filme
   
class DetalhesFilme(LoginRequiredMixin, DetailView):
    template_name = 'detalhesfilme.html'
    model = Filme

    def get(self, request, *args, **kwargs):
        filme = self.get_object()
        filme.visualizacoes += 1
        filme.save()
        usuario = request.user
        usuario.filmes_vistos.add(filme)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(DetalhesFilme, self).get_context_data(**kwargs)
        filmes_relacionados = self.model.objects.filter(categoria=self.get_object().categoria)
        context['filmes_relacionados'] = filmes_relacionados
        return context
    
class Pesquisa(LoginRequiredMixin, ListView):
    allow_empty = False
    template_name = 'pesquisa.html'
    model = Filme


    def get_queryset(self):
        termo_pesquisa = self.request.GET.get('query')
        if termo_pesquisa:
            object_list = self.model.objects.filter(titulo__icontains=termo_pesquisa)
            return object_list

    def dispatch(self, *args, **kwargs):
        try:
            return super().dispatch(*args, **kwargs)
        except Http404:
            return redirect('filme:homefilmes')
        
class EditarPerfil(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'editarperfil.html'
    model = Usuario
    fields = ['first_name', 'last_name', 'email']

    def test_func(self):
        ''' Impede que um usuário tente editar o perfil de outro mudando a id na url'''
        user = self.get_object()
        return self.request.user == user
    
    def get_success_url(self):
        return reverse('filme:homefilmes')


class CriarConta(FormView):
    template_name = 'criarconta.html'
    form_class = CriarContaForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('filme:login')

