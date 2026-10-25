"""Filtros que levam as regras do aviso aos modelos de página, sem repeti-las."""
from django import template

register = template.Library()


@register.filter
def pode_ser_arquivado_por(aviso, conta):
    """O botão de arquivar segue a mesma regra que a rota confere (RN-02)."""
    return aviso.pode_ser_arquivado_por(conta)
