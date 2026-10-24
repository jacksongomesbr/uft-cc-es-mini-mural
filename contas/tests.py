"""Testes do esqueleto da conta: os campos que existem e as restrições do banco."""
from django.contrib.auth import get_user_model
from django.db import IntegrityError, transaction
from django.test import SimpleTestCase, TestCase

from .models import Conta, normalizar_nome


class CamposDaContaTest(SimpleTestCase):
    """A-04 e RE-02: a conta tem só os campos do PROJETO.md."""

    def test_modelo_de_usuario_e_a_conta(self):
        self.assertIs(get_user_model(), Conta)

    def test_so_os_campos_do_projeto(self):
        campos = {campo.name for campo in Conta._meta.concrete_fields}
        self.assertEqual(campos, {"id", "nome_usuario", "nome_exibicao", "password"})

    def test_coluna_da_senha_tem_o_nome_do_projeto(self):
        self.assertEqual(Conta._meta.get_field("password").column, "senha_derivada")

    def test_normalizar_nome_tira_espacos_a_mais(self):
        self.assertEqual(normalizar_nome("  Secretaria   do curso "), "Secretaria do curso")


class RestricoesDaContaTest(TestCase):
    """O banco recusa o que nunca pode acontecer, venha de onde vier a gravação."""

    def setUp(self):
        self.paula = Conta.objects.create_user("paula.sec", "Secretaria do curso", "senha-de-teste-1")

    def test_senha_guardada_como_valor_derivado(self):
        # RNF-04: o banco não guarda a senha.
        self.assertNotIn("senha-de-teste-1", self.paula.password)
        self.assertTrue(self.paula.check_password("senha-de-teste-1"))

    def test_nome_de_usuario_repetido_com_maiusculas(self):
        # CA-01.2
        with self.assertRaises(IntegrityError), transaction.atomic():
            Conta.objects.create_user("Paula.Sec", "Outro nome", "senha-de-teste-2")

    def test_nome_para_exibicao_repetido_com_espacos_e_maiusculas(self):
        # CA-01.6
        with self.assertRaises(IntegrityError), transaction.atomic():
            Conta.objects.create_user("secretaria", "secretaria  do curso ", "senha-de-teste-2")

    def test_nome_para_exibicao_vazio(self):
        # CA-01.5
        with self.assertRaises(IntegrityError), transaction.atomic():
            Conta.objects.create_user("vazio", "   ", "senha-de-teste-2")

    def test_qualquer_conta_publica(self):
        # RN-01, até a revisão de C2
        self.assertTrue(self.paula.pode_publicar())
