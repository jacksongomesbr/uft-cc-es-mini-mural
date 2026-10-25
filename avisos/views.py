"""Páginas de avisos. O contrato de cada rota está em contrato/operacoes.md."""
from urllib.parse import urlencode

from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import redirect_to_login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from config.respostas import redirecionar

from .forms import AvisoForm
from .models import LIMITE_DO_TEXTO, Aviso


def mural(request):
    """HU-04 e HU-06: os avisos que quem pede pode ver, do mais recente para o
    mais antigo. Sem conta, só os abertos."""
    return render(request, "avisos/mural.html", {"avisos": Aviso.objects.do_mural(request.user)})


def nao_encontrado(request):
    """A mesma resposta para aviso que não existe e para o que a pessoa não pode
    ver, para não revelar que ele existe (CA-07.4)."""
    return render(request, "avisos/nao_encontrado.html", status=404)


def detalhe(request, id):
    """O aviso pelo endereço (CA-06.3, CA-06.4, CA-07.4, CA-07.5)."""
    aviso = Aviso.objects.select_related("autor").filter(pk=id).first()
    if aviso is None:
        return nao_encontrado(request)
    if not aviso.pode_ser_visto_por(request.user):
        # Interno publicado e pedido sem conta: a página de entrar, com o caminho
        # de volta, e sem o texto (CA-06.3). Os outros casos são arquivado de
        # outra pessoa, e a resposta é a de aviso inexistente.
        if aviso.situacao == Aviso.PUBLICADO and not request.user.is_authenticated:
            return redirect_to_login(request.get_full_path())
        return nao_encontrado(request)
    return render(request, "avisos/detalhe.html", {"aviso": aviso})


def pagina_de_publicar(request, form=None, status=200):
    contexto = {"form": form or AvisoForm(), "limite": LIMITE_DO_TEXTO}
    return render(request, "avisos/publicar.html", contexto, status=status)


@login_required
def novo(request):
    """UC-01, passos 1 e 2: a página de publicar."""
    return pagina_de_publicar(request)


@require_http_methods(["GET", "POST"])
def criar(request):
    """HU-03.1 no POST: registra o aviso (UC-01, passos 3 e 4).

    HU-16 no GET: o endereço que fica na barra depois de uma recusa leva de
    volta à página de publicar.
    """
    if request.method == "GET":
        # HU-16: depois de uma recusa, a barra mostra /avisos/. Abrir esse
        # endereço de novo leva à página de publicar (CA-16.1).
        return redirecionar(reverse("novo"))

    conta = request.user
    if not conta.is_authenticated or not conta.pode_publicar():
        # UC-01, 4c: a sessão acabou, por exemplo porque a pessoa saiu em outra
        # aba. Nada é gravado, e a página de entrar explica o que houve.
        parametros = urlencode({"next": reverse("novo"), "motivo": "aviso-nao-publicado"})
        return HttpResponseRedirect(f"{reverse('entrar')}?{parametros}")

    form = AvisoForm(request.POST)
    if not form.is_valid():
        # A-07: 422, com o texto mantido para a pessoa corrigir.
        return pagina_de_publicar(request, form, status=422)

    # A-08: o autor vem da sessão; o formulário não tem campo de autor, e um
    # campo forjado é ignorado. O instante vem do banco (DP-10).
    Aviso.objects.create(autor=conta, texto=form.cleaned_data["texto"], tipo=form.cleaned_data["tipo"])
    return redirecionar(reverse("mural"))
