# Roteiro do projeto

Este repositório é o projeto exemplo do livro de Engenharia de Software da
UFT. Ele percorre o semestre na ordem dos capítulos, como faria uma equipe da
disciplina, e marca com uma tag o fim de cada capítulo. Para ver o projeto em um
ponto da sequência, abra a tag correspondente:

```bash
git switch --detach v0.1.0
```

## A equipe é simulada

O livro foi escrito para equipes de cinco pessoas, e este projeto simula uma:
Ana, Bruno, Carla, Davi e Eva, os mesmos nomes que aparecem nos exemplos do
livro. Os commits levam o nome de quem, na simulação, fez o trabalho, e as
issues levam uma etiqueta com a pessoa responsável (`resp:ana`, por exemplo).
Todo o trabalho, porém, sai de uma única conta do GitHub. Por isso:

- os endereços de e-mail dos commits terminam em `.invalid` e não pertencem a
  ninguém;
- o GitHub não deixa o autor aprovar o próprio pull request, então a revisão é
  registrada como comentário assinado ("Revisão (Ana): ...") em vez de
  aprovação formal;
- a proteção do `main` impede envio direto e exige pull request, mas não exige
  aprovação, que uma conta só não consegue dar.

## Decisões que valem para todo o roteiro

- **Arquitetura:** monólito Django, com HTML montado no servidor e PostgreSQL. O
  livro apresenta frontend e backend separados; a escolha do monólito é uma
  decisão da equipe e será registrada, com a alternativa descartada e a
  consequência, no `ARQUITETURA.md` do capítulo 7. Outras arquiteturas ficam
  para um ramo ou um fork posterior.
- **Versões:** o capítulo 2 cria a `v0.1.0`, e cada capítulo seguinte termina
  com uma versão nova, em que o número do meio acompanha o capítulo
  (capítulo 3, `v0.2.0`; capítulo 4, `v0.3.0`). A review final, no capítulo
  16, marca a `v1.0.0`. Enquanto o primeiro número é zero, o versionamento
  semântico admite que tudo mude, e os capítulos só de documentação também
  ganham versão.
- **Fluxo:** a partir do capítulo 2, toda mudança nasce de uma issue, passa por
  um ramo e entra no `main` por pull request revisado, como descreve o
  `CONTRIBUTING.md`.

## Capítulos, artefatos e versões

| Capítulo | Assunto | O que a equipe entrega | Tag |
|---|---|---|---|
| 1 | Introdução | `PROBLEMA.md`: equipe formada e problema em uma página | (sem tag) |
| 2 | Gerência de configuração | `README.md`, `CONTRIBUTING.md`, `.gitignore`, `CHANGELOG.md`, proteção do `main`, um pull request por integrante | `v0.1.0` |
| 3 | Processos de desenvolvimento | `PROCESSO.md` | `v0.2.0` |
| 4 | Descoberta e requisitos | `DESCOBERTA.md` | `v0.3.0` |
| 5 | Especificação e validação | `REQUISITOS.md` (primeiro marco) | `v0.4.0` |
| 6 | Modelagem e projeto | `PROJETO.md` | `v0.5.0` |
| 7 | Arquitetura de aplicação web | `ARQUITETURA.md` e o esqueleto do Django | `v0.6.0` |
| 8 | Planejamento ágil | `ITERACOES.md` e a primeira iteração de código | `v0.7.0` |
| 9 | Review parcial | Demonstração e itens de backlog da avaliação | `v0.8.0` |
| 10 | Qualidade | Lista de revisão e modelo de pull request | `v0.9.0` |
| 11 | Verificação e validação | `TESTES.md` com estratégia e casos | `v0.10.0` |
| 12 | Testes e integração contínua | Suíte automatizada, verificação de estilo e workflow no GitHub | `v0.11.0` |
| 13 | Segurança, ética e privacidade | Segredos em variáveis de ambiente, dependências auditadas, política de acesso | `v0.12.0` |
| 14 | Implantação e operação | `OPERACAO.md`, migrações, verificação de saúde e registro de eventos | `v0.13.0` |
| 15 | Manutenção e evolução | Evolução planejada, com análise de impacto | `v0.14.0` |
| 16 | Review final | Demonstração final e retrospectiva | `v1.0.0` |

O código do sistema começa no capítulo 7. Até lá, o repositório guarda os
documentos que os capítulos 1 a 6 pedem, e o código nasce a partir deles.
