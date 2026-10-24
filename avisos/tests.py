"""Testes do esqueleto: a página inicial responde e se ajusta ao celular."""
from django.conf import settings
from django.test import SimpleTestCase


class InicioTest(SimpleTestCase):
    def test_pagina_inicial_responde(self):
        resposta = self.client.get("/")
        self.assertEqual(resposta.status_code, 200)
        self.assertContains(resposta, "Mini Mural")

    def test_pagina_se_ajusta_ao_celular(self):
        # RNF-08
        resposta = self.client.get("/")
        self.assertContains(resposta, 'name="viewport"')


class FusoTest(SimpleTestCase):
    def test_instante_com_fuso_mostrado_no_horario_de_palmas(self):
        # DP-06, CA-04.3
        self.assertTrue(settings.USE_TZ)
        self.assertEqual(settings.TIME_ZONE, "America/Araguaina")
