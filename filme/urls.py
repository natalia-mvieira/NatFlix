from django.urls import path
from .views import HomePage, HomeFilmes, DetalhesFilme

app_name = 'filme' #para que os names do app filmes sejam diferenciados nas urls do projeto como um todo (namespace em natflix/urls.py)

urlpatterns = [
    path('', HomePage.as_view(), name='homepage'),
    path('filmes/', HomeFilmes.as_view(), name='homefilmes'),
    path('filmes/<int:pk>', DetalhesFilme.as_view(), name='detalhesfilme')
]