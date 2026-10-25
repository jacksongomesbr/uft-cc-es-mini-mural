# Como contribuir

Convenções da equipe para o semestre. O que está aqui foi decidido uma vez e
não precisa ser negociado a cada pull request. Quando uma convenção mudar, a
mudança entra por pull request, como qualquer outra.

## Fluxo

1. Todo trabalho começa em uma issue, com a etiqueta da pessoa responsável
   (`resp:ana`, `resp:bruno`, `resp:carla`, `resp:davi` ou `resp:eva`) e o
   marco da versão em que deve entrar.
2. O ramo sai do `main` atualizado.
3. O trabalho entra no `main` por pull request revisado por outra pessoa.
   Ninguém envia commit direto ao `main`; a proteção do ramo impede.

## Ramos

- `feat/<descricao-curta>` para funcionalidade nova
- `fix/<descricao-curta>` para correção
- `docs/<descricao-curta>` para documentação
- `chore/<descricao-curta>` para configuração do repositório e ferramentas
- `test/<descricao-curta>` para testes sem mudança de comportamento
- `refactor/<descricao-curta>` para reorganização sem mudança de comportamento

A descrição usa letras minúsculas sem acento e hífens, como em
`docs/problema`.

## Commits

- Formato Conventional Commits: `tipo(escopo): resumo no imperativo`, com o
  escopo opcional e o resumo em português.
- Corpo explicando o porquê, quando a mudança não for óbvia.
- Referência à issue: `Closes #<numero>` no commit que conclui a issue, e
  `Refs #<numero>` nos demais.
- Um commit, uma mudança. Ajuste pedido na revisão entra em commit novo; o que
  já foi enviado não é reescrito.

## Pull requests

- Um item de backlog por pull request, pequeno o bastante para ser revisado em
  quinze ou vinte minutos.
- A descrição diz quem é o autor, a quem a revisão foi pedida, o que muda e
  como conferir, e termina com `Closes #<numero>`.
- A revisão é feita por uma pessoa diferente do autor, em até 24 horas.
- Depois da aprovação, o autor integra com merge commit, que preserva os
  commits e a autoria de cada um, e remove o ramo.

### Revisão na equipe simulada

Todo o trabalho sai de uma única conta do GitHub, e o GitHub não deixa o autor
aprovar o próprio pull request. Por isso a revisão é registrada como
comentário de revisão assinado, por exemplo "Revisão (Ana): ...". Um pedido de
ajuste é respondido com commit novo, e a integração só acontece depois do
comentário que diz "Aprovado para integrar". A proteção do `main` exige pull
request, mas não exige aprovação formal, que uma conta só não consegue dar.

### Lista de verificação

Quem revisa confere estas perguntas, e quem é autor confere as mesmas antes de
pedir a revisão. O modelo de descrição em `.github/pull_request_template.md` as
traz marcáveis. A lista é curta de propósito: cada pergunta nova sai de um
defeito que escapou, e a pergunta que ninguém verifica sai.

| Lente | Pergunta | De onde vem |
|---|---|---|
| Item | O pull request cumpre os critérios de aceitação do item, e só eles, em um item de backlog? | `REQUISITOS.md`; capítulo 2 |
| Projeto | A regra fica no domínio, na conta ou no aviso, e a borda só chama? | DP-08, A-03 |
| Contrato | Código de status, destino e mensagem batem com o contrato, ou o contrato mudou no mesmo pull request? | A-12 |
| Legibilidade | Os nomes usam o glossário, e cada função se entende na primeira leitura? | Glossário do `REQUISITOS.md` |
| Multiplicidade | O código trata zero, um e muitos avisos onde o modelo admite? | Modelo de domínio do `PROJETO.md` |
| Endereço depois do envio | O endereço que fica na barra depois de um envio, aceito ou recusado, abre alguma página? | Defeito de HU-16, que passou pela revisão da #94 |
| Testes | Existe teste do comportamento novo, com a expectativa tirada do critério, sem copiar o que o código faz? | Definição de pronto |
| Rastreabilidade | O commit e o pull request citam a issue, e a issue cita a história? | Capítulo 2 |
| Segurança e dados | Nenhum segredo no repositório e nenhum dado de pessoa real em teste, exemplo ou registro? | RE-02; capítulo 13 |

Ficaram fora da lista do capítulo 10 a pergunta de tamanho, que a de item já
cobre, e a revisão do contrato pelas duas partes, porque o sistema não tem
frontend separado (A-01).

### O que a ferramenta decide

O formatador e o verificador de estilo, o Ruff, rodam antes da revisão, com as
regras do `pyproject.toml`. Quem revisa não comenta recuo, aspas, quebra de
linha nem importação sem uso: a ferramenta já decidiu.

```bash
ruff format .
ruff check .
```

### Tipos de comentário

Cada comentário de revisão diz a lente e um destes tipos:

- **Bloqueia:** o pull request não é integrado antes de resolver.
- **Sugere:** o autor decide.
- **Pergunta:** quem revisa precisa entender antes de decidir.
- **Elogia:** algo bem feito, que vale preservar.

Na equipe simulada, o comentário de revisão traz uma tabela com o trecho, o
comentário, a lente e o tipo.

## Divergência técnica

- A discussão fica registrada no pull request. Decisão tomada no grupo de
  mensagens se perde.
- Sem acordo em dois turnos de comentário, decide quem prioriza o backlog,
  conforme os papéis do [PROCESSO.md](PROCESSO.md), e a decisão é registrada no
  próprio pull request.

## Definição de pronto

A definição de pronto fica no [PROCESSO.md](PROCESSO.md), em uma fonte só.
Antes de pedir revisão, confira o pull request contra ela.

## Versões

- Cada entrega relevante ganha uma versão no formato do versionamento
  semântico, com a entrada correspondente no `CHANGELOG.md`.
- A ordem é fixa: primeiro o `CHANGELOG.md` entra no `main` por pull request;
  depois, a tag anotada (`git tag -a`) é criada sobre esse commit e enviada com
  `git push origin <tag>`.
- Uma tag enviada não se move. Se algo precisar mudar, sai uma versão nova.
