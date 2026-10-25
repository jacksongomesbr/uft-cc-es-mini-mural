"""A conta do Mini Mural (PROJETO.md, modelo de dados; A-04 no ARQUITETURA.md).

A conta tem só os campos do PROJETO.md: nome de usuário, nome para exibição e o
valor derivado da senha. O modelo de usuário padrão do framework traria e-mail,
nome, sobrenome e último acesso, que RE-02 manda não pedir.
"""

import re

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.db.models.functions import Lower


def normalizar_nome(nome):
    """Tira os espaços das pontas e junta os repetidos (CA-01.6)."""
    return re.sub(r"\s+", " ", nome).strip()


class ContaManager(BaseUserManager):
    def create_user(self, nome_usuario, nome_exibicao, senha):
        conta = self.model(nome_usuario=nome_usuario, nome_exibicao=nome_exibicao)
        conta.set_password(senha)
        conta.save(using=self._db)
        return conta


class Conta(AbstractBaseUser):
    nome_usuario = models.CharField(max_length=150, unique=True)
    nome_exibicao = models.CharField(max_length=80)

    # O framework chama o campo de "password", mas ele guarda o valor derivado
    # da senha, nunca a senha (RNF-04). A coluna leva o nome do PROJETO.md.
    password = models.CharField(max_length=128, db_column="senha_derivada")

    # Sem último acesso: nenhum requisito pede esse dado (RE-02). Sem a coluna,
    # o framework também deixa de atualizá-la a cada entrada.
    last_login = None

    USERNAME_FIELD = "nome_usuario"
    REQUIRED_FIELDS = ["nome_exibicao"]

    objects = ContaManager()

    class Meta:
        # O nome da tabela é o do PROJETO.md.
        db_table = "conta"
        constraints = [
            # CA-01.2 e CA-01.6: os nomes não se repetem, sem diferenciar
            # maiúsculas. O banco repete a regra que o formulário confere.
            models.UniqueConstraint(Lower("nome_usuario"), name="conta_nome_usuario_unico"),
            models.UniqueConstraint(Lower("nome_exibicao"), name="conta_nome_exibicao_unico"),
            # CA-01.5: o nome para exibição é obrigatório.
            models.CheckConstraint(
                condition=~models.Q(nome_exibicao=""),
                name="conta_nome_exibicao_obrigatorio",
            ),
        ]

    def __str__(self):
        return f"{self.nome_exibicao} ({self.nome_usuario})"

    def save(self, *args, **kwargs):
        # A unicidade só vale se o nome chegar ao banco já normalizado.
        self.nome_exibicao = normalizar_nome(self.nome_exibicao)
        super().save(*args, **kwargs)

    def desativar(self):
        """Desativa a conta sem apagá-la, para manter a autoria dos avisos (DP-05).

        Sem painel administrativo (A-04), um integrante faz isso pelo terminal,
        no caso de R9. A senha passa a não conferir com nada, e as sessões
        abertas deixam de valer, porque o framework as liga ao valor da senha.
        """
        self.set_unusable_password()
        self.save(update_fields=["password"])

    def pode_publicar(self):
        """RN-01: qualquer pessoa com conta publica, até a revisão de C2 (D2).

        A regra fica aqui, e só aqui (DP-08, RNF-07). Se a coordenação restringir
        quem publica, é este método que muda, com uma coluna nova na conta.
        """
        return self.has_usable_password()
