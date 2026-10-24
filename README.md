# Mini Mural

Mural de avisos do curso, em que a coordenação, os professores e o centro
acadêmico publicam avisos para os alunos. Este é o projeto exemplo do livro
de Engenharia de Software da UFT: ele é construído capítulo a capítulo, como
faria uma equipe da disciplina, e cada capítulo termina com uma versão marcada
por tag.

A proposta inicial do problema está no [PROBLEMA.md](PROBLEMA.md), a
descoberta feita com os usuários, no [DESCOBERTA.md](DESCOBERTA.md), e o que o
sistema vai fazer, no [REQUISITOS.md](REQUISITOS.md). De que o sistema é feito
está no [PROJETO.md](PROJETO.md).

## Equipe

Ana, Bruno, Carla, Davi e Eva. A equipe é simulada para fins didáticos: os
commits levam o nome de quem fez o trabalho na simulação, mas todo o trabalho
sai de uma única conta do GitHub. O [ROTEIRO.md](ROTEIRO.md) explica como isso
funciona nos commits, nas issues e na revisão.

## Estado atual

O código começou no capítulo 7, com o esqueleto do projeto Django: a
configuração, os módulos `contas` e `avisos`, o modelo de conta e uma página
inicial. O mural e a publicação de avisos entram na iteração 3. O que cada versão entregou está
no [CHANGELOG.md](CHANGELOG.md).

Para ver o projeto como estava no fim de um capítulo, abra a tag da versão,
por exemplo:

```bash
git switch --detach v0.5.0
```

O [ROTEIRO.md](ROTEIRO.md) liga cada capítulo do livro ao artefato que ele
produz e à tag que o encerra.

## Como rodar em desenvolvimento

O código é um projeto Django 5.2 com PostgreSQL, como decide o
[ARQUITETURA.md](ARQUITETURA.md). Você precisa de Python 3.12 e de um
PostgreSQL local em que seu usuário possa criar bancos.

```bash
python3.12 -m venv .venv
```

```bash
source .venv/bin/activate
```

```bash
pip install -r requirements.txt
```

```bash
createdb mini_mural_es
```

```bash
python manage.py migrate
```

```bash
python manage.py test
```

```bash
python manage.py runserver
```

O último comando sobe o servidor de desenvolvimento do framework em
<http://127.0.0.1:8000/>. Ele serve para trabalhar e para a demonstração do
encontro 9, e não é servidor de produção: a hospedagem e o servidor de produção
são decididos no capítulo 14 (A-11).

A configuração vem de variáveis de ambiente, e cada uma tem um valor de
desenvolvimento (A-10):

| Variável | Para quê | Valor de desenvolvimento |
|---|---|---|
| `MURAL_DB_NAME` | Nome do banco | `mini_mural_es` |
| `MURAL_DB_USER`, `MURAL_DB_PASSWORD` | Usuário e senha do banco | O usuário do sistema, sem senha |
| `MURAL_DB_HOST`, `MURAL_DB_PORT` | Onde está o banco | O soquete local |
| `MURAL_DEBUG` | `1` mostra os erros na página | `1` |
| `MURAL_HOSTS` | Endereços aceitos, separados por vírgula | `localhost,127.0.0.1` |
| `MURAL_SECRET_KEY` | Chave secreta do framework | Uma chave de desenvolvimento, que não pode ir para a hospedagem |

## Documentos

| Documento | O que contém |
|---|---|
| [PROBLEMA.md](PROBLEMA.md) | Problema, usuário pretendido e verificação do tema (capítulo 1) |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Convenções de ramos, commits, pull requests e revisão (capítulo 2) |
| [PROCESSO.md](PROCESSO.md) | Processo escolhido, iterações, papéis e definição de pronto (capítulo 3) |
| [DESCOBERTA.md](DESCOBERTA.md) | Partes interessadas, personas, necessidades, escopo, MVP e riscos (capítulo 4) |
| [descoberta/](descoberta/) | Roteiro de entrevista e atas da elicitação, sem identificação (capítulos 4 e 5) |
| [REQUISITOS.md](REQUISITOS.md) | Glossário, backlog ordenado, histórias com critérios de aceitação, caso de uso, requisitos não funcionais, regras, rastreabilidade e validação (capítulo 5) |
| [validacao/](validacao/) | Protótipo do MVP e registro das sessões de validação (capítulo 5) |
| [PROJETO.md](PROJETO.md) | Modelo de domínio, modelo de dados, estados, responsabilidades, decisões de projeto e conferência cruzada (capítulo 6) |
| [diagrams/](diagrams/) | Fontes Mermaid dos diagramas do `PROJETO.md`, desenhadas pelo GitHub na página de cada arquivo (capítulo 6) |
| [prototipo/](prototipo/) | Protótipo navegável do fluxo principal, com as recusas (capítulo 6) |
| [CHANGELOG.md](CHANGELOG.md) | O que mudou em cada versão |
| [ROTEIRO.md](ROTEIRO.md) | Capítulos, artefatos e tags do semestre |

## Como contribuir

Toda mudança nasce de uma issue e entra no `main` por pull request revisado
por outra pessoa da equipe. Os detalhes estão no
[CONTRIBUTING.md](CONTRIBUTING.md).

## Licença

[MIT](LICENSE).
