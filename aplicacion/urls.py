from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name="inicio"),
    
    #Joe
    path('perfil/', perfil, name="perfil"),
    path('amistades/', listar_amistades, name="amistades"),
    path('lecciones/', listar_lecciones, name="lecciones"),
    
    #listados
    path('usuarios/', listar_usuarios, name="usuarios"),
    path('amistades_usuarios/', listar_amistades_usuarios, name="amistades_usuarios"),

    #API
    path('clima/', open_mateo, name="clima"),
]
