from django.contrib import admin
from .models import Filme, Episodio, Usuario
from django.contrib.auth.admin import UserAdmin

#para aparecer o campo filmes_vistos em Usuários
campos = list(UserAdmin.fieldsets)
campos.append(
    ('Histórico', {'fields': ('filmes_vistos',)})
)
UserAdmin.fieldsets = tuple(campos)

admin.site.register(Filme)
admin.site.register(Episodio)
admin.site.register(Usuario, UserAdmin)


