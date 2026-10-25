"""Respostas usadas pelos dois módulos."""
from django.http import HttpResponseRedirect


def redirecionar(endereco):
    """Redireciona com 303, para a página seguinte ser lida com GET (A-06).

    Recarregar a página de destino não reenvia o formulário (RNF-03). O
    redirecionamento padrão do framework responde 302; o 303 deixa explícito
    que o pedido seguinte é um GET.
    """
    resposta = HttpResponseRedirect(endereco)
    resposta.status_code = 303
    return resposta
