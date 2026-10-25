"""Formulários de avisos. As mensagens são as do contrato/operacoes.md."""
from django import forms
from django.core.exceptions import ValidationError

from .models import LIMITE_DO_TEXTO, Aviso, preparar_texto


class AvisoForm(forms.Form):
    # Obrigatório na regra, e não no campo, para a mensagem ser a do contrato.
    # O campo não limita a digitação: quem passa do limite recebe a recusa com
    # a contagem (CA-03.3), e o contador da página só ajuda.
    texto = forms.CharField(
        label="Texto do aviso",
        required=False,
        widget=forms.Textarea(
            attrs={"rows": 6, "required": True, "data-limite": LIMITE_DO_TEXTO, "data-contador": "contador"}
        ),
    )

    # HU-05. Sem escolha, o aviso é interno (CA-05.1), o tipo mais restritivo
    # (C1). Valor fora da lista é recusado com a mensagem do contrato (CA-05.3).
    tipo = forms.ChoiceField(
        label="Quem pode ler",
        choices=[
            (Aviso.INTERNO, "Interno: só quem entrou com uma conta"),
            (Aviso.ABERTO, "Aberto: qualquer pessoa, mesmo sem conta"),
        ],
        required=False,
        initial=Aviso.INTERNO,
        widget=forms.RadioSelect,
        error_messages={"invalid_choice": "Escolha se o aviso é aberto ou interno."},
    )

    def clean_tipo(self):
        return self.cleaned_data["tipo"] or Aviso.INTERNO

    def clean_texto(self):
        texto, erro = preparar_texto(self.cleaned_data["texto"])
        if erro:
            raise ValidationError(erro)
        return texto
