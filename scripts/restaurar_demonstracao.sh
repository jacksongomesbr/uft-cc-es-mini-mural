#!/bin/sh
# Devolve o banco da demonstração ao estado do passo 1 do roteiro da review
# parcial (ITERACOES.md): apaga o banco, recria, aplica as migrações e carrega
# as contas e os avisos de demonstração.
#
#   scripts/restaurar_demonstracao.sh UMA-SENHA-DE-TESTE
#
# O banco é sempre um que termina em _demo, para que o script nunca apague o
# banco de desenvolvimento por engano.
set -eu

if [ "$#" -ne 1 ]; then
  echo "Uso: $0 SENHA-DAS-CONTAS-DE-DEMONSTRACAO" >&2
  exit 2
fi

BANCO="${MURAL_DEMO_DB:-mini_mural_demo}"
case "$BANCO" in
  *_demo) ;;
  *) echo "Recusado: o banco da demonstração precisa terminar em _demo ($BANCO)." >&2; exit 2 ;;
esac

PYTHON="${PYTHON:-python}"
cd "$(dirname "$0")/.."

dropdb --if-exists "$BANCO"
createdb "$BANCO"
MURAL_DB_NAME="$BANCO" "$PYTHON" manage.py migrate --verbosity 0
MURAL_DB_NAME="$BANCO" "$PYTHON" manage.py carregar_demonstracao --senha "$1"
echo "Banco $BANCO pronto para o passo 1."
