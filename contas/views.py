"""Páginas de contas. O contrato de cada rota está em contrato/operacoes.md."""
from django.contrib.auth import login
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from config.respostas import redirecionar

from .forms import CadastroForm


@require_http_methods(["GET", "POST"])
def cadastro(request):
    """HU-01: cria a conta e já entra com ela (CA-01.1)."""
    if request.user.is_authenticated:
        return redirecionar(reverse("inicio"))

    form = CadastroForm(request.POST or None)
    status = 200
    if request.method == "POST":
        if form.is_valid():
            login(request, form.save())
            return redirecionar(reverse("inicio"))
        # A-07: a recusa responde 422, com a página e o que foi preenchido.
        status = 422
    return render(request, "contas/cadastro.html", {"form": form}, status=status)
