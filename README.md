# Mini Mural

Mural de avisos do curso, em que a coordenação, os professores e o centro
acadêmico publicam recados para os alunos. Este é o projeto exemplo do livro
de Engenharia de Software da UFT: ele é construído capítulo a capítulo, como
faria uma equipe da disciplina, e cada capítulo termina com uma versão marcada
por tag.

O problema que o projeto resolve, o usuário pretendido e a verificação do tema
contra os critérios da disciplina estão no [PROBLEMA.md](PROBLEMA.md).

## Equipe

Ana, Bruno, Carla, Davi e Eva. A equipe é simulada para fins didáticos: os
commits levam o nome de quem fez o trabalho na simulação, mas todo o trabalho
sai de uma única conta do GitHub. O [ROTEIRO.md](ROTEIRO.md) explica como isso
funciona nos commits, nas issues e na revisão.

## Estado atual

O projeto está nos capítulos de documentação. O código do sistema, um monólito
em Django com PostgreSQL, começa no capítulo 7. O que cada versão entregou está
no [CHANGELOG.md](CHANGELOG.md).

Para ver o projeto como estava no fim de um capítulo, abra a tag da versão,
por exemplo:

```bash
git switch --detach v0.1.0
```

O [ROTEIRO.md](ROTEIRO.md) liga cada capítulo do livro ao artefato que ele
produz e à tag que o encerra.

## Documentos

| Documento | O que contém |
|---|---|
| [PROBLEMA.md](PROBLEMA.md) | Problema, usuário pretendido e verificação do tema (capítulo 1) |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Convenções de ramos, commits, pull requests e revisão (capítulo 2) |
| [PROCESSO.md](PROCESSO.md) | Processo escolhido, iterações, papéis e definição de pronto (capítulo 3) |
| [CHANGELOG.md](CHANGELOG.md) | O que mudou em cada versão |
| [ROTEIRO.md](ROTEIRO.md) | Capítulos, artefatos e tags do semestre |

## Como contribuir

Toda mudança nasce de uma issue e entra no `main` por pull request revisado
por outra pessoa da equipe. Os detalhes estão no
[CONTRIBUTING.md](CONTRIBUTING.md).

## Licença

[MIT](LICENSE).
