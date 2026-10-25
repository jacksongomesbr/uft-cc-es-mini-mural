"""Rotas do Mini Mural. O contrato de cada rota está em contrato/operacoes.md."""
from django.urls import include, path

urlpatterns = [
    path("", include("contas.urls")),
    path("", include("avisos.urls")),
]
