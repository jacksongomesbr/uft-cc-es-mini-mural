# Projeto

Este documento diz de que o Mini Mural é feito. O `DESCOBERTA.md` diz de onde
cada necessidade veio, o `REQUISITOS.md` diz o que o sistema faz e o
`PROCESSO.md` diz como a equipe trabalha. Onde cada parte roda e como as partes
conversam é decisão do capítulo 7, no `ARQUITETURA.md`; por isso este documento
não usa nome de framework, de tabela gerada nem de biblioteca.

As fontes dos diagramas ficam em `diagrams/`, em texto Mermaid, uma fonte por
diagrama. Quem altera o código que um diagrama descreve altera o diagrama no
mesmo pull request.

## Modelo de domínio

Fonte: [`diagrams/dominio.mmd`](diagrams/dominio.mmd).

O modelo cobre as histórias obrigatórias e as importantes, HU-01 a HU-07, como
registra a decisão DP-01. Ele tem duas classes, e esse é o tamanho do problema
nesta versão.

### Substantivos do `REQUISITOS.md`

Cada substantivo do domínio que apareceu no glossário, nas histórias, nos
critérios e no UC-01 passou por duas perguntas: o sistema precisa guardar
informação sobre isso? E isso existe no vocabulário de quem usa o sistema?

| Substantivo | Onde apareceu | Decisão | Motivo |
|---|---|---|---|
| Conta | Glossário, HU-01, RE-01 | Classe | O sistema guarda nome de usuário, nome para exibição e senha |
| Aviso | Glossário, HU-03, UC-01 | Classe | Tem texto, tipo, situação e datas próprios, e um autor |
| Autor | Glossário, CA-03.1, N7 | Papel da conta na associação com o aviso | Não guarda nada além do que a conta já guarda |
| Nome de usuário, nome para exibição, senha | CA-01.1 a CA-01.6 | Atributos da conta | São dados de uma conta, sem vida própria |
| Mural | Glossário, HU-04 | Fora do modelo: é uma consulta | É a lista dos avisos publicados e não guarda dado próprio |
| Aviso aberto, aviso interno | Glossário, HU-05, C1 | Valor do atributo `tipo` | A diferença é só quem lê; ver DP-02 |
| Aviso publicado, aviso arquivado | Glossário, HU-07 | Valor do atributo `situacao` | São situações do mesmo aviso, desenhadas no diagrama de estados |
| Data e hora da publicação e do arquivamento | CA-03.1, glossário | Atributos do aviso | São instantes de um aviso, sem vida própria |
| Data de validade | HU-13 | Fora do modelo nesta versão | HU-13 é desejável; entra quando subir no backlog (DP-01) |
| Visitante | Glossário, HU-06 | Ator, sem classe | Quem lê sem conta não deixa dado |
| Secretaria, professor, centro acadêmico | HU-03, UC-01 | Ator, sem classe | RN-01 não distingue quem publica |
| Coordenação | D2, RN-01, RN-02 | Fora do modelo | Decide as regras e não usa o sistema |
| Comunicado oficial | Glossário, D2 | Fora do modelo | Continua no e-mail institucional |
| Aviso vencido | Glossário, O1 | Fora do modelo nesta versão | O sistema não conhece a data em que o assunto de um aviso passa |
| Sessão | CA-02.4, RNF-06 | Fora do modelo de domínio | Deixa de existir junto com o sistema; é assunto de implementação |
| Tela, botão, campo | UC-01, protótipo | Fora do modelo de domínio | É interface |

A linha de secretaria, professor e centro acadêmico é a que pode mudar primeiro.
Se a coordenação restringir quem publica na revisão de C2 (D2, R9), a conta
ganha um atributo que diz o papel, e essa mudança está medida no teste de
Parnas, em "Distribuição de responsabilidades".

### Classes, atributos e associação

| Classe | Atributos | Origem no `REQUISITOS.md` |
|---|---|---|
| Conta | nome de usuário, nome para exibição, senha | HU-01, HU-02, CA-01.1 a CA-01.6, RE-01, RE-02 |
| Aviso | texto, tipo, situação, data e hora da publicação, data e hora do arquivamento | HU-03 a HU-07, CA-03.1 a CA-03.5, CA-04.1, CA-04.3 |

A associação, lida nas duas direções:

- uma conta publica zero ou mais avisos;
- um aviso é publicado por exatamente uma conta, que é o seu autor.

A leitura em voz alta levantou uma pergunta: um aviso pode ter mais de um autor,
como um aviso da secretaria assinado também pelo professor? Nenhuma fonte pediu
isso, e N7 fala em "quem publicou". A multiplicidade fica em exatamente um.

### Generalização

Aviso aberto e aviso interno poderiam ser subclasses de aviso. A generalização
pede duas condições: atributos ou regras próprios em cada subclasse, e toda
operação da superclasse fazendo sentido para todas. Os dois tipos têm os mesmos
atributos e as mesmas operações; o que muda é quem pode ler. A diferença cabe em
um valor de atributo, e a decisão está em DP-02.

## Modelo de dados

Preenchido na issue #56.

## Comportamento

Diagrama de estados preenchido na issue #57; sequência, na issue #58.

## Distribuição de responsabilidades

Preenchida na issue #58.

## Decisões de projeto

Os identificadores usam o prefixo `DP`, de decisão de projeto, para não
confundir com os documentos D1 e D2 do `DESCOBERTA.md`.

| Id | Decisão | Motivo | Consequência aceita |
|---|---|---|---|
| DP-01 | O modelo cobre HU-01 a HU-07 | São as histórias obrigatórias e importantes, previstas até a review final. Só com o MVP, o aviso teria uma situação só, e o diagrama de estados não mostraria nada | Tipo e data de arquivamento entram no modelo antes do código que os usa, que vem depois da review parcial |
| DP-02 | Aberto e interno como valor do atributo `tipo`, sem subclasse | Os dois tipos têm os mesmos atributos e operações; muda só quem lê | A regra de leitura precisa conferir o tipo do aviso |

## Protótipo

Preenchido na issue #59.

## Conferência cruzada

Preenchida na issue #60.

## Histórico de revisão

- 2026-10-24: esqueleto e modelo de domínio (#55).
