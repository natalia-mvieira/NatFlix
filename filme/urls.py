from django.urls import path
from .views import HomePage, HomeFilmes, DetalhesFilme, Pesquisa, EditarPerfil, CriarConta
from django.contrib.auth import views as auth_view
app_name = 'filme' #para que os names do app filmes sejam diferenciados nas urls do projeto como um todo (namespace em natflix/urls.py)

urlpatterns = [
    path('', HomePage.as_view(), name='homepage'),
    path('filmes/', HomeFilmes.as_view(), name='homefilmes'),
    path('filmes/<int:pk>', DetalhesFilme.as_view(), name='detalhesfilme'),
    path('pesquisa/', Pesquisa.as_view(), name='pesquisa'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('perfil/', EditarPerfil.as_view(), name='editarperfil'),
    path('criarconta/', CriarConta.as_view(), name='criarconta')
]