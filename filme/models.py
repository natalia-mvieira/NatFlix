from django.db import models
from django.utils import timezone

CATEGORIAS = (
    ('ANALISES', 'Análises'),
    ('PROGRAMAÇÃO', 'Programação'),
    ('APRESENTAÇÃO', 'Apresentação'),
    ('OUTROS', 'Outros'))

class Filme(models.Model):
    titulo = models.CharField(max_length=250, null=False, blank=False)
    descricao = models.TextField(max_length=1000)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    visualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)
    thumb = models.ImageField(upload_to='thumb_filmes')

    def __str__(self):
        return self.titulo

