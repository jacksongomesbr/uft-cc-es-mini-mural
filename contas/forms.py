"""Formulários de contas. As mensagens são as do contrato/operacoes.md."""

from django import forms
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from django.db import transaction

from .models import Conta, normalizar_nome


class CadastroForm(forms.Form):
    nome_usuario = forms.CharField(label="Nome de usuário", max_length=150)
    # Obrigatório na regra, e não no campo, para a mensagem ser a do contrato.
    nome_exibicao = forms.CharField(
        label="Nome para exibição, que aparece como autor dos avisos",
        max_length=80,
        required=False,
    )
    senha = forms.CharField(label="Senha", widget=forms.PasswordInput)

    def clean_nome_usuario(self):
        nome = self.cleaned_data["nome_usuario"].strip()
        # CA-01.2
        if Conta.objects.filter(nome_usuario__iexact=nome).exists():
            raise ValidationError("Esse nome de usuário já está em uso.")
        return nome

    def clean_nome_exibicao(self):
        nome = normalizar_nome(self.cleaned_data["nome_exibicao"])
        # CA-01.5
        if not nome:
            raise ValidationError(
                "Escolha um nome para exibição; ele aparece como autor dos avisos."
            )
        # CA-01.6: a comparação usa o nome já normalizado, como o banco.
        if Conta.objects.filter(nome_exibicao__iexact=nome).exists():
            raise ValidationError("Esse nome para exibição já está em uso. Escolha outro.")
        return nome

    def clean_senha(self):
        senha = self.cleaned_data["senha"]
        # CA-01.3: as duas regras estão em AUTH_PASSWORD_VALIDATORS, e a
        # mensagem do contrato junta as duas.
        try:
            password_validation.validate_password(senha)
        except ValidationError as recusa:
            # A recusa original fica ligada à nova, e o registro de um erro
            # mostra as duas.
            raise ValidationError(
                "A senha precisa de pelo menos 8 caracteres, com algo além de números."
            ) from recusa
        return senha

    def save(self):
        # Um ponto de salvamento próprio: se o banco recusar, só esta gravação
        # é desfeita.
        with transaction.atomic():
            return Conta.objects.create_user(
                self.cleaned_data["nome_usuario"],
                self.cleaned_data["nome_exibicao"],
                self.cleaned_data["senha"],
            )


class EntrarForm(forms.Form):
    nome_usuario = forms.CharField(label="Nome de usuário", max_length=150)
    senha = forms.CharField(label="Senha", widget=forms.PasswordInput)
