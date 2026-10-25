"""Testes do esqueleto da conta: os campos que existem e as restrições do banco."""
from unittest import mock

from django.contrib.auth import get_user_model
from django.db import IntegrityError, transaction
from django.test import SimpleTestCase, TestCase

from .forms import CadastroForm
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

    def test_conta_desativada_nao_entra_nem_publica(self):
        # A-04 e R9: desativar pelo terminal, sem apagar a conta
        self.paula.desativar()
        self.paula.refresh_from_db()
        self.assertFalse(self.paula.check_password("senha-de-teste-1"))
        self.assertFalse(self.paula.pode_publicar())
        self.assertTrue(Conta.objects.filter(nome_usuario="paula.sec").exists())


class CadastroTest(TestCase):
    """HU-01: um teste por critério de aceitação."""

    def cadastrar(self, nome_usuario="livia.m", nome_exibicao="Lívia Martins", senha="senha-com-12"):
        return self.client.post(
            "/cadastro/",
            {"nome_usuario": nome_usuario, "nome_exibicao": nome_exibicao, "senha": senha},
        )

    def test_ca_01_1_conta_criada_e_ja_dentro(self):
        resposta = self.cadastrar()
        self.assertEqual(resposta.status_code, 303)
        self.assertEqual(resposta["Location"], "/")
        conta = Conta.objects.get(nome_usuario="livia.m")
        self.assertEqual(int(self.client.session["_auth_user_id"]), conta.pk)

    def test_ca_01_2_nome_de_usuario_em_uso(self):
        self.cadastrar()
        self.client.logout()
        resposta = self.cadastrar(nome_usuario="Livia.M", nome_exibicao="Outra Lívia", senha="outra-senha-1")
        self.assertEqual(resposta.status_code, 422)
        self.assertContains(resposta, "Esse nome de usuário já está em uso.", status_code=422)
        # Mantém o que foi preenchido, menos a senha.
        self.assertContains(resposta, 'value="Outra Lívia"', status_code=422)
        self.assertNotContains(resposta, "outra-senha-1", status_code=422)

    def test_ca_01_3_senha_fraca(self):
        for senha in ("1234567", "12345678"):
            with self.subTest(senha=senha):
                resposta = self.cadastrar(senha=senha)
                self.assertContains(
                    resposta,
                    "A senha precisa de pelo menos 8 caracteres, com algo além de números.",
                    status_code=422,
                )
        self.assertFalse(Conta.objects.exists())

    def test_ca_01_4_a_conta_continua(self):
        self.cadastrar()
        self.client.logout()
        self.assertTrue(self.client.login(nome_usuario="livia.m", password="senha-com-12"))

    def test_ca_01_5_nome_para_exibicao_obrigatorio(self):
        resposta = self.cadastrar(nome_exibicao="   ")
        self.assertContains(
            resposta,
            "Escolha um nome para exibição; ele aparece como autor dos avisos.",
            status_code=422,
        )

    def test_ca_01_6_nome_para_exibicao_em_uso(self):
        Conta.objects.create_user("paula.sec", "Secretaria do curso", "senha-de-teste-1")
        resposta = self.cadastrar(nome_usuario="secretaria", nome_exibicao="secretaria  do curso ")
        self.assertContains(
            resposta, "Esse nome para exibição já está em uso. Escolha outro.", status_code=422
        )
        self.assertFalse(Conta.objects.filter(nome_usuario="secretaria").exists())

    def test_quem_ja_entrou_vai_para_o_mural(self):
        self.cadastrar()
        resposta = self.client.get("/cadastro/")
        self.assertEqual(resposta.status_code, 303)

    def test_nome_gravado_por_outra_pessoa_entre_conferir_e_gravar(self):
        # A restrição do banco recusa, e a página mostra a mensagem do CA-01.2.
        salvar = CadastroForm.save

        def salvar_depois_de_outra_pessoa(form):
            Conta.objects.create_user("livia.m", "Outra pessoa", "senha-de-teste-9")
            return salvar(form)

        with mock.patch.object(CadastroForm, "save", salvar_depois_de_outra_pessoa):
            resposta = self.cadastrar()
        self.assertContains(resposta, "Esse nome de usuário já está em uso.", status_code=422)
        self.assertEqual(Conta.objects.filter(nome_usuario__iexact="livia.m").count(), 1)


class EntrarESairTest(TestCase):
    """HU-02: um teste por critério de aceitação."""

    def setUp(self):
        Conta.objects.create_user("paula.sec", "Secretaria do curso", "senha-de-teste-1")

    def entrar(self, senha="senha-de-teste-1", **extra):
        return self.client.post("/entrar/", {"nome_usuario": "paula.sec", "senha": senha, **extra})

    def test_ca_02_1_entrar_leva_ao_mural_e_mostra_quem_entrou(self):
        resposta = self.entrar()
        self.assertEqual(resposta.status_code, 303)
        self.assertEqual(resposta["Location"], "/")
        self.assertContains(self.client.get("/"), "Secretaria do curso")

    def test_ca_02_2_senha_errada(self):
        resposta = self.entrar(senha="errada-123")
        self.assertContains(resposta, "Nome de usuário ou senha não conferem.", status_code=422)
        self.assertContains(resposta, 'value="paula.sec"', status_code=422)
        self.assertNotIn("_auth_user_id", self.client.session)

    def test_ca_02_3_mural_sem_conta_vai_para_entrar_e_volta(self):
        resposta = self.client.get("/")
        self.assertEqual(resposta.status_code, 302)
        self.assertEqual(resposta["Location"], "/entrar/?next=/")
        resposta = self.entrar(next="/")
        self.assertEqual(resposta["Location"], "/")

    def test_ca_02_4_depois_de_sair_a_sessao_acabou(self):
        self.entrar()
        resposta = self.client.post("/sair/")
        self.assertEqual(resposta.status_code, 303)
        self.assertEqual(resposta["Location"], "/entrar/")
        self.assertEqual(self.client.get("/").status_code, 302)

    def test_sair_por_get_responde_405(self):
        self.entrar()
        self.assertEqual(self.client.get("/sair/").status_code, 405)

    def test_endereco_de_outro_site_vira_o_mural(self):
        resposta = self.entrar(next="https://exemplo.invalid/")
        self.assertEqual(resposta["Location"], "/")

    def test_motivo_mostra_a_mensagem_do_aviso_nao_publicado(self):
        resposta = self.client.get("/entrar/?next=/avisos/novo/&motivo=aviso-nao-publicado")
        self.assertContains(resposta, "Você saiu da conta em outra aba. Entre de novo; o aviso não foi publicado.")
