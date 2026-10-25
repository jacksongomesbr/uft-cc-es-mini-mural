"""Páginas de contas. O contrato de cada rota está em contrato/operacoes.md."""

from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.shortcuts import render
from django.urls import reverse
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.decorators.http import require_http_methods

from config.respostas import redirecionar

from .forms import CadastroForm, EntrarForm

# Mensagens que a página de entrar mostra conforme o motivo do redirecionamento.
MOTIVOS = {
    "aviso-nao-publicado": "Você saiu da conta em outra aba. Entre de novo; o aviso não foi publicado.",
}


@require_http_methods(["GET", "POST"])
def cadastro(request):
    """HU-01: cria a conta e já entra com ela (CA-01.1)."""
    if request.user.is_authenticated:
        return redirecionar(reverse("mural"))

    form = CadastroForm(request.POST or None)
    status = 200
    if request.method == "POST":
        if form.is_valid():
            try:
                conta = form.save()
            except IntegrityError:
                # Outra conta com o mesmo nome foi gravada entre a conferência e
                # a gravação. Conferir de novo põe a mensagem no campo certo.
                form = CadastroForm(request.POST)
                form.is_valid()
            else:
                login(request, conta)
                return redirecionar(reverse("mural"))
        # A-07: a recusa responde 422, com a página e o que foi preenchido.
        status = 422
    return render(request, "contas/cadastro.html", {"form": form}, status=status)


def destino_seguro(request, endereco):
    """Aceita só caminho deste site; qualquer outro vira o mural."""
    if endereco and url_has_allowed_host_and_scheme(
        endereco, allowed_hosts={request.get_host()}, require_https=request.is_secure()
    ):
        return endereco
    return reverse("mural")


@require_http_methods(["GET", "POST"])
def entrar(request):
    """HU-02: CA-02.1 e CA-02.2; a volta ao endereço pedido é o CA-02.3."""
    destino = destino_seguro(request, request.POST.get("next") or request.GET.get("next"))
    if request.method == "GET" and request.user.is_authenticated:
        return redirecionar(reverse("mural"))

    form = EntrarForm(request.POST or None)
    erro = None
    status = 200
    if request.method == "POST":
        conta = None
        if form.is_valid():
            conta = authenticate(
                request,
                nome_usuario=form.cleaned_data["nome_usuario"],
                password=form.cleaned_data["senha"],
            )
        if conta is not None:
            login(request, conta)
            return redirecionar(destino)
        # CA-02.2: a mensagem não diz qual dos dois errou.
        erro = "Nome de usuário ou senha não conferem."
        status = 422
    return render(
        request,
        "contas/entrar.html",
        {
            "form": form,
            "erro": erro,
            "aviso": MOTIVOS.get(request.GET.get("motivo", "")),
            "next": destino,
        },
        status=status,
    )


@require_http_methods(["GET", "POST"])
def sair(request):
    """CA-02.4: apaga a sessão no servidor.

    Por GET, 405: uma ligação não tira a pessoa da conta. A resposta tem página,
    com o botão de sair, porque o endereço pode ficar na barra depois de um
    envio recusado.
    """
    if request.method == "GET":
        return render(request, "contas/sair.html", status=405)
    logout(request)
    return redirecionar(reverse("entrar"))
