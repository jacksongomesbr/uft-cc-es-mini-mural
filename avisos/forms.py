"""Formulários de avisos. As mensagens são as do contrato/operacoes.md."""
from django import forms
from django.core.exceptions import ValidationError

from .models import LIMITE_DO_TEXTO, preparar_texto


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

    def clean_texto(self):
        texto, erro = preparar_texto(self.cleaned_data["texto"])
        if erro:
            raise ValidationError(erro)
        return texto
