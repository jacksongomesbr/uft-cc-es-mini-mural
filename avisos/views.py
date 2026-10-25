"""Páginas de avisos. O contrato de cada rota está em contrato/operacoes.md."""
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Aviso


# CA-02.3: sem conta, o framework leva à página de entrar com o caminho de volta.
# Quando HU-06 entrar, quem não entrou passa a ver os avisos abertos.
@login_required
def mural(request):
    """HU-04: os avisos publicados, do mais recente para o mais antigo."""
    return render(request, "avisos/mural.html", {"avisos": Aviso.objects.publicados()})
