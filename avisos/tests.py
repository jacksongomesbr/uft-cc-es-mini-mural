"""Testes do aviso e do mural (HU-04): um teste por critério, mais o RNF-01 e o RNF-05."""
from datetime import datetime, timedelta, timezone

from django.conf import settings
from django.db import DataError, IntegrityError, transaction
from django.db.models import ProtectedError
from django.test import SimpleTestCase, TestCase
from django.utils import timezone as tz

from contas.models import Conta

from .models import LIMITE_DO_TEXTO, Aviso


def instante(hora, minuto=0):
    """Um instante de 2026-10-24 no horário de Palmas (UTC-3)."""
    return datetime(2026, 10, 24, hora, minuto, tzinfo=timezone(timedelta(hours=-3)))


class MuralTest(TestCase):
    def setUp(self):
        self.paula = Conta.objects.create_user("paula.sec", "Secretaria do curso", "senha-de-teste-1")
        self.livia = Conta.objects.create_user("livia.m", "Lívia Martins", "senha-de-teste-2")
        self.client.force_login(self.livia)

    def publicar(self, texto, quando, autor=None):
        return Aviso.objects.create(autor=autor or self.paula, texto=texto, publicado_em=quando)

    def test_ca_04_1_mais_recentes_primeiro_com_autor_data_e_hora(self):
        self.publicar("Aviso das 8h", instante(8))
        self.publicar("Aviso das 10h", instante(10))
        self.publicar("Aviso das 9h", instante(9))
        conteudo = self.client.get("/").content.decode()
        posicoes = [conteudo.index(f"Aviso das {h}h") for h in (10, 9, 8)]
        self.assertEqual(posicoes, sorted(posicoes))
        self.assertIn("Secretaria do curso (paula.sec)", conteudo)
        self.assertIn("24/10/2026, 10h00", conteudo)

    def test_ca_04_1_desempate_pelo_mais_novo(self):
        self.publicar("Primeiro no mesmo instante", instante(9))
        self.publicar("Segundo no mesmo instante", instante(9))
        conteudo = self.client.get("/").content.decode()
        self.assertLess(conteudo.index("Segundo no mesmo"), conteudo.index("Primeiro no mesmo"))

    def test_ca_04_2_mural_vazio(self):
        self.assertContains(self.client.get("/"), "Ainda não há avisos.")

    def test_ca_04_3_hora_local(self):
        self.publicar("Troca de sala", datetime(2026, 10, 24, 17, 2, tzinfo=timezone.utc))
        self.assertContains(self.client.get("/"), "24/10/2026, 14h02")

    def test_arquivado_fora_do_mural(self):
        Aviso.objects.create(
            autor=self.paula, texto="Aviso que saiu", situacao=Aviso.ARQUIVADO, arquivado_em=tz.now()
        )
        self.assertNotContains(self.client.get("/"), "Aviso que saiu")

    def test_rnf_01_uma_consulta_para_os_avisos_e_autores(self):
        # Sessão, conta e avisos com autores: três consultas, com 1 ou com 200 avisos.
        self.publicar("Um aviso", instante(8))
        with self.assertNumQueries(3):
            self.client.get("/")
        for i in range(199):
            self.publicar(f"Aviso {i}", instante(9), autor=self.livia if i % 2 else self.paula)
        with self.assertNumQueries(3):
            resposta = self.client.get("/")
        self.assertEqual(len(resposta.context["avisos"]), 200)

    def test_rnf_05_texto_mostrado_como_texto(self):
        self.publicar("<script>alert(1)</script>", instante(8))
        resposta = self.client.get("/")
        self.assertNotContains(resposta, "<script>alert(1)</script>")
        self.assertContains(resposta, "&lt;script&gt;alert(1)&lt;/script&gt;")


class RestricoesDoAvisoTest(TestCase):
    """O banco recusa o que nunca pode acontecer (PROJETO.md, DP-04, DP-05, DP-09, DP-10)."""

    def setUp(self):
        self.paula = Conta.objects.create_user("paula.sec", "Secretaria do curso", "senha-de-teste-1")

    def test_instante_vem_do_banco(self):
        aviso = Aviso.objects.create(autor=self.paula, texto="Sem instante informado")
        aviso.refresh_from_db()
        self.assertLess(abs(tz.now() - aviso.publicado_em), timedelta(minutes=1))

    def test_texto_vazio(self):
        with self.assertRaises(IntegrityError), transaction.atomic():
            Aviso.objects.create(autor=self.paula, texto="")

    def test_texto_acima_do_limite(self):
        with self.assertRaises(DataError), transaction.atomic():
            Aviso.objects.create(autor=self.paula, texto="a" * (LIMITE_DO_TEXTO + 1))

    def test_limite_conta_caracteres_e_nao_bytes(self):
        Aviso.objects.create(autor=self.paula, texto="á" * LIMITE_DO_TEXTO)

    def test_arquivado_sem_data(self):
        with self.assertRaises(IntegrityError), transaction.atomic():
            Aviso.objects.create(autor=self.paula, texto="Sem data", situacao=Aviso.ARQUIVADO)

    def test_conta_com_avisos_nao_e_apagada(self):
        Aviso.objects.create(autor=self.paula, texto="Aviso com autoria")
        with self.assertRaises(ProtectedError):
            self.paula.delete()


class FusoTest(SimpleTestCase):
    def test_instante_com_fuso_mostrado_no_horario_de_palmas(self):
        # DP-06, CA-04.3
        self.assertTrue(settings.USE_TZ)
        self.assertEqual(settings.TIME_ZONE, "America/Araguaina")

    def test_pagina_se_ajusta_ao_celular(self):
        # RNF-08: o modelo base tem a meta de viewport.
        with open(settings.BASE_DIR / "templates" / "base.html") as arquivo:
            self.assertIn('name="viewport"', arquivo.read())


class PublicarTest(TestCase):
    """HU-03.1: um teste por critério, mais CA-02.4, RNF-03 e A-08."""

    def setUp(self):
        self.paula = Conta.objects.create_user("paula.sec", "Secretaria do curso", "senha-de-teste-1")
        self.livia = Conta.objects.create_user("livia.m", "Lívia Martins", "senha-de-teste-2")
        self.client.force_login(self.paula)

    def publicar(self, texto, **extra):
        return self.client.post("/avisos/", {"texto": texto, **extra})

    def test_pagina_de_publicar(self):
        self.assertContains(self.client.get("/avisos/novo/"), "Até 500 caracteres.")

    def test_ca_03_1_publicar(self):
        texto = "A aula de Engenharia de Software de amanhã muda para a sala 12 do bloco B."
        resposta = self.publicar(texto)
        self.assertEqual(resposta.status_code, 303)
        self.assertEqual(resposta["Location"], "/")
        aviso = Aviso.objects.get()
        self.assertEqual((aviso.autor, aviso.texto), (self.paula, texto))
        mural = self.client.get("/").content.decode()
        self.assertLess(mural.index(texto), mural.index("Secretaria do curso (paula.sec)"))

    def test_ca_03_2_texto_vazio_ou_so_com_espacos(self):
        for texto in ("", "  \r\n  "):
            with self.subTest(texto=texto):
                resposta = self.publicar(texto)
                self.assertContains(resposta, "O aviso precisa de texto. Nada foi publicado.", status_code=422)
        self.assertFalse(Aviso.objects.exists())

    def test_ca_03_3_acima_do_limite(self):
        texto = "a" * 501
        resposta = self.publicar(texto)
        self.assertContains(
            resposta,
            "O aviso tem 501 caracteres, e o limite é 500. Corte 1 caractere e publique de novo.",
            status_code=422,
        )
        self.assertContains(resposta, texto, status_code=422)
        self.assertFalse(Aviso.objects.exists())

    def test_ca_03_4_no_limite_com_acento(self):
        self.assertEqual(self.publicar("á" * 500).status_code, 303)
        self.assertEqual(len(Aviso.objects.get().texto), 500)

    def test_quebra_de_linha_do_navegador_conta_um(self):
        texto = "a" * 250 + "\r\n" + "b" * 249
        self.assertEqual(self.publicar(texto).status_code, 303)
        self.assertEqual(Aviso.objects.get().texto, "a" * 250 + "\n" + "b" * 249)

    def test_ca_03_5_o_aviso_continua(self):
        self.publicar("Aviso que fica")
        self.client.force_login(self.livia)
        resposta = self.client.get("/")
        self.assertContains(resposta, "Aviso que fica")
        self.assertContains(resposta, "Secretaria do curso (paula.sec)")

    def test_ca_02_4_depois_de_sair_nada_e_publicado(self):
        self.client.post("/sair/")
        resposta = self.publicar("Aviso depois de sair")
        self.assertEqual(resposta.status_code, 302)
        self.assertEqual(
            resposta["Location"], "/entrar/?next=%2Favisos%2Fnovo%2F&motivo=aviso-nao-publicado"
        )
        self.assertFalse(Aviso.objects.exists())

    def test_rnf_03_recarregar_nao_publica_de_novo(self):
        resposta = self.publicar("Aviso único")
        for _ in range(3):
            self.client.get(resposta["Location"])
        self.assertEqual(Aviso.objects.count(), 1)

    def test_a_08_autor_vem_da_sessao(self):
        self.publicar("Aviso com autor forjado", autor=self.livia.pk, autor_id=self.livia.pk)
        self.assertEqual(Aviso.objects.get().autor, self.paula)

    def test_pagina_de_publicar_sem_conta(self):
        self.client.logout()
        resposta = self.client.get("/avisos/novo/")
        self.assertEqual(resposta["Location"], "/entrar/?next=/avisos/novo/")


class CarregarDemonstracaoTest(TestCase):
    """#88: o comando da demonstração não duplica contas e completa o mural."""

    def carregar(self, *argumentos):
        from io import StringIO

        from django.core.management import call_command

        call_command("carregar_demonstracao", "--senha", "senha-de-teste-1", *argumentos, stdout=StringIO())

    def test_rodar_de_novo_nao_duplica(self):
        self.carregar()
        self.carregar()
        self.assertEqual(Conta.objects.count(), 3)
        self.assertEqual(Aviso.objects.count(), 2)

    def test_completa_o_mural_ate_a_quantidade_pedida(self):
        self.carregar("--avisos", "200")
        self.assertEqual(Aviso.objects.publicados().count(), 200)

    def test_senha_vem_do_argumento(self):
        self.carregar()
        self.assertTrue(Conta.objects.get(nome_usuario="aluno.demo").check_password("senha-de-teste-1"))
