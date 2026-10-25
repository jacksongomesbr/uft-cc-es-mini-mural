"""O aviso (PROJETO.md: modelo de dados e estados do aviso)."""
from django.conf import settings
from django.db import models
from django.db.models.functions import Now

# CA-03.3 e CA-03.4. O banco repete o limite no tamanho da coluna (DP-09).
LIMITE_DO_TEXTO = 500


class AvisoQuerySet(models.QuerySet):
    def publicados(self):
        """Os avisos do mural: publicados, com o autor na mesma consulta.

        A junção evita uma ida ao banco por aviso para buscar o nome do autor
        (ARQUITETURA.md, o custo escondido do mural).
        """
        return self.filter(situacao=Aviso.PUBLICADO).select_related("autor")


class Aviso(models.Model):
    ABERTO = "aberto"
    INTERNO = "interno"
    TIPOS = [(ABERTO, "Aberto"), (INTERNO, "Interno")]

    PUBLICADO = "publicado"
    ARQUIVADO = "arquivado"
    SITUACOES = [(PUBLICADO, "Publicado"), (ARQUIVADO, "Arquivado")]

    # DP-05: conta com avisos não é apagada, para não levar a autoria junto.
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="avisos")
    texto = models.CharField(max_length=LIMITE_DO_TEXTO)
    # DP-01: tipo e arquivamento entram no modelo antes do código que os usa.
    tipo = models.CharField(max_length=10, choices=TIPOS, default=INTERNO)
    situacao = models.CharField(max_length=10, choices=SITUACOES, default=PUBLICADO)
    # DP-10: o instante vem do banco, e não de quem publica.
    publicado_em = models.DateTimeField(db_default=Now())
    arquivado_em = models.DateTimeField(null=True, blank=True)

    objects = AvisoQuerySet.as_manager()

    class Meta:
        db_table = "aviso"
        # CA-04.1, com o desempate de DP-06.
        ordering = ["-publicado_em", "-id"]
        constraints = [
            models.CheckConstraint(condition=~models.Q(texto=""), name="aviso_texto_obrigatorio"),
            models.CheckConstraint(condition=models.Q(tipo__in=["aberto", "interno"]), name="aviso_tipo_valido"),
            models.CheckConstraint(
                condition=models.Q(situacao__in=["publicado", "arquivado"]), name="aviso_situacao_valida"
            ),
            # Estados do aviso: a data do arquivamento existe se, e só se, o
            # aviso está arquivado.
            models.CheckConstraint(
                condition=(
                    models.Q(situacao="publicado", arquivado_em__isnull=True)
                    | models.Q(situacao="arquivado", arquivado_em__isnull=False)
                ),
                name="aviso_arquivado_com_data",
            ),
        ]

    def __str__(self):
        return self.texto[:40]
