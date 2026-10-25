"""Carrega as contas e os avisos da demonstração do encontro 9 (#88).

Nenhum dado é de pessoa real. A senha das contas de demonstração vem do
argumento --senha; o código não guarda senha. Rodar de novo não duplica as
contas.

    python manage.py carregar_demonstracao --senha VALOR
    python manage.py carregar_demonstracao --senha VALOR --avisos 200

A segunda forma acrescenta avisos até o mural ter a quantidade pedida, que é
a condição do RNF-01.
"""

from django.core.management.base import BaseCommand
from django.db import transaction

from avisos.models import Aviso
from contas.models import Conta

CONTAS = [
    ("prof.calculo", "Prof. de Cálculo"),
    ("ca.computacao", "Centro acadêmico"),
    ("aluno.demo", "Aluno de demonstração"),
]

AVISOS = [
    ("ca.computacao", "Inscrições abertas para a monitoria de Algoritmos até sexta."),
    ("prof.calculo", "A prova de Cálculo II foi adiada para 05/11, no mesmo horário."),
]


class Command(BaseCommand):
    help = "Carrega as contas e os avisos da demonstração do encontro 9."

    def add_arguments(self, parser):
        parser.add_argument("--senha", required=True, help="Senha das contas de demonstração.")
        parser.add_argument("--avisos", type=int, default=0, help="Quantidade de avisos no mural.")

    @transaction.atomic
    def handle(self, *args, senha, avisos, **opcoes):
        contas = {}
        for nome_usuario, nome_exibicao in CONTAS:
            conta = Conta.objects.filter(nome_usuario=nome_usuario).first()
            if conta is None:
                conta = Conta.objects.create_user(nome_usuario, nome_exibicao, senha)
            contas[nome_usuario] = conta

        if not Aviso.objects.filter(autor__in=contas.values()).exists():
            for nome_usuario, texto in AVISOS:
                Aviso.objects.create(autor=contas[nome_usuario], texto=texto)

        faltam = avisos - Aviso.objects.publicados().count()
        autores = list(contas.values())
        Aviso.objects.bulk_create(
            Aviso(
                autor=autores[i % len(autores)],
                texto=f"Aviso de carga número {i + 1}, para medir o mural.",
            )
            for i in range(max(faltam, 0))
        )

        no_mural = Aviso.objects.publicados().count()
        self.stdout.write(f"Contas de demonstração: {len(contas)}. Avisos no mural: {no_mural}.")
