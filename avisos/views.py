"""Páginas do módulo de avisos.

No esqueleto há só a página inicial. O mural (HU-04) e a publicação (HU-03)
entram na iteração 3, conforme o contrato em contrato/operacoes.md.
"""
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# CA-02.3: sem conta, o framework leva à página de entrar com o caminho de volta.
@login_required
def inicio(request):
    return render(request, "avisos/inicio.html")
