"""Páginas do módulo de avisos.

No esqueleto há só a página inicial. O mural (HU-04) e a publicação (HU-03)
entram na iteração 3, conforme o contrato em contrato/operacoes.md.
"""
from django.shortcuts import render


def inicio(request):
    return render(request, "avisos/inicio.html")
