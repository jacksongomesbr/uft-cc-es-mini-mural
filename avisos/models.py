"""O aviso (PROJETO.md: modelo de dados e estados do aviso)."""
from django.conf import settings
from django.db import models
from django.db.models.functions import Now

# CA-03.3 e CA-03.4. O banco repete o limite no tamanho da coluna (DP-09).
LIMITE_DO_TEXTO = 500



def caracteres(quantidade):
    """"1 caractere", "12 caracteres"."""
    return "1 caractere" if quantidade == 1 else f"{quantidade} caracteres"


def preparar_texto(texto):
    """Normaliza o texto do aviso e confere o limite (CA-03.2 a CA-03.4).

    Devolve o texto normalizado e a mensagem de recusa, ou None quando o texto
    é aceito. O navegador envia cada quebra de linha como dois caracteres, e
    ela conta um, como no banco. Os espaços das pontas não contam.
    """
    texto = texto.replace("\r\n", "\n").replace("\r", "\n").strip()
    if not texto:
        return texto, "O aviso precisa de texto. Nada foi publicado."
    if len(texto) > LIMITE_DO_TEXTO:
        excesso = len(texto) - LIMITE_DO_TEXTO
        return texto, (
            f"O aviso tem {caracteres(len(texto))}, e o limite é {LIMITE_DO_TEXTO}. "
            f"Corte {caracteres(excesso)} e publique de novo."
        )
    return texto, None

class AvisoQuerySet(models.QuerySet):
    def publicados(self):
        """Os avisos do mural: publicados, com o autor na mesma consulta.

        A junção evita uma ida ao banco por aviso para buscar o nome do autor
        (ARQUITETURA.md, o custo escondido do mural).
        """
        return self.filter(situacao=Aviso.PUBLICADO).select_related("autor")

    def do_mural(self, conta):
        """Os avisos que o mural mostra a quem pede (HU-04, HU-06).

        É a regra de pode_ser_visto_por escrita como consulta, para o mural
        não buscar aviso por aviso. Um teste confere que as duas concordam.
        """
        avisos = self.publicados()
        if not conta.is_authenticated:
            avisos = avisos.filter(tipo=Aviso.ABERTO)
        return avisos


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

    def pode_ser_visto_por(self, conta):
        """Quem vê o aviso (RNF-06, RNF-07; CA-06.1 a CA-06.4, CA-07.4, CA-07.5).

        O arquivado, só o autor. O interno publicado, quem entrou com uma conta.
        O aberto publicado, qualquer pessoa.
        """
        if self.situacao == self.ARQUIVADO:
            return conta.is_authenticated and conta.pk == self.autor_id
        if self.tipo == self.INTERNO:
            return conta.is_authenticated
        return True

    def pode_ser_arquivado_por(self, conta):
        """RN-02: só o autor arquiva o próprio aviso (CA-07.1, CA-07.2)."""
        return conta.is_authenticated and conta.pk == self.autor_id

    def arquivar(self):
        """Tira o aviso do mural e registra o instante (CA-07.1).

        Só muda o aviso que ainda está publicado: arquivar de novo não muda
        nada, e a data do primeiro arquivamento fica (CA-07.3). O instante vem
        do banco, como o da publicação (DP-10).
        """
        Aviso.objects.filter(pk=self.pk, situacao=self.PUBLICADO).update(
            situacao=self.ARQUIVADO, arquivado_em=Now()
        )
        self.refresh_from_db()
