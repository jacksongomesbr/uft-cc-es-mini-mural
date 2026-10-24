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

Fonte: [`diagrams/dados.mmd`](diagrams/dados.mmd).

### Passagem do domínio para os dados

| No modelo de domínio | No modelo de dados | Decisão |
|---|---|---|
| Classe Conta | Tabela `CONTA`, com chave `id` | Chave artificial (DP-03) |
| Classe Aviso | Tabela `AVISO`, com chave `id` | Chave artificial (DP-03) |
| Conta publica aviso, um para muitos | `autor_id` em `AVISO`, chave estrangeira obrigatória | Apagar uma conta com avisos é recusado (DP-05) |
| Atributo senha | Coluna `senha_derivada` | O banco guarda o valor derivado da senha, e nunca a senha (RNF-04) |
| Atributos `tipo` e `situacao` | Colunas de valor restrito | As listas, aberto e interno, publicado e arquivado, só mudam junto com o código, e por isso não viram tabela |

### Decisões que a passagem obrigou

- **Identidade.** Toda tabela tem chave artificial gerada pelo sistema. O nome
  de usuário e o nome para exibição continuam únicos, como restrição de
  unicidade que não diferencia maiúsculas (CA-01.2, CA-01.6). O nome para
  exibição é gravado sem os espaços das pontas e sem espaços repetidos, para a
  comparação valer.
- **Apagamento.** O aviso não é apagado: arquivar é o apagamento dele, e o
  aviso arquivado continua na tabela, com a situação e a data do arquivamento
  (DP-04). Nenhuma história apaga conta; a chave estrangeira recusa apagar uma
  conta que tem avisos, para não levar a autoria junto (DP-05).
- **Tempo.** `publicado_em` e `arquivado_em` guardam o instante com fuso, e a
  tela mostra no horário de Palmas, UTC-3 (CA-04.3). O instante vem do sistema,
  e não de quem publica (CA-03.1). Dois avisos no mesmo instante saem do mais
  novo `id` para o mais antigo, o que fixa a ordem do CA-04.1 (DP-06).
- **Arquivo.** Não se aplica nesta versão: nenhum requisito guarda arquivo, e
  anexar arquivo (HU-09) está fora. Se HU-09 subir, a escolha entre guardar no
  banco ou fora dele volta para este documento.
- **Tamanho e obrigatoriedade.** `texto` aceita até 500 caracteres, contados
  como caracteres (CA-03.3, CA-03.4), e o banco recusa o que passar, além da
  regra do aviso. `nome_exibicao` é obrigatório (CA-01.5). `arquivado_em` fica
  vazio enquanto o aviso está publicado e é preenchido junto com a situação
  arquivado; uma coisa sem a outra é recusada.
- **Normalização.** As duas tabelas estão na terceira forma normal. O nome do
  autor sai da junção com `CONTA` e não é copiado para o aviso. Nenhum índice
  além dos que as chaves e as unicidades criam, até o RNF-01 ser medido (DP-07).

### O dado que cada critério exige

| Critério | Dado | Onde |
|---|---|---|
| CA-01.1 | Nome de usuário, nome para exibição e valor derivado da senha | `CONTA` |
| CA-01.2, CA-01.6 | Unicidade sem diferenciar maiúsculas | `nome_usuario`, `nome_exibicao` |
| CA-01.3 | Nenhum: a regra da senha é conferida antes de gravar | Não se aplica |
| CA-01.4, CA-03.5 | Persistência das duas tabelas | `CONTA`, `AVISO` |
| CA-01.5 | Obrigatoriedade | `nome_exibicao` |
| CA-02.1 a CA-02.4 | Nenhum dado do domínio: a sessão é assunto do capítulo 7 | Não se aplica |
| CA-03.1 | Texto, autor e instante | `texto`, `autor_id`, `publicado_em` |
| CA-03.2 | Nenhum: a recusa não grava nada | Não se aplica |
| CA-03.3, CA-03.4 | Limite de 500 caracteres | `texto` |
| CA-04.1 | Ordem, desempate e os dois nomes do autor | `publicado_em`, `id`, junção com `CONTA` |
| CA-04.2 | Nenhum | Não se aplica |
| CA-04.3 | Instante com fuso | `publicado_em` |

A conferência inversa: toda coluna tem origem. `id` vem de DP-03; `nome_usuario`,
`nome_exibicao` e `senha_derivada`, de CA-01.1 e RNF-04; `autor_id`, de CA-03.1
e N7; `texto` e `publicado_em`, de CA-03.1; `tipo`, de HU-05 e C1; `situacao` e
`arquivado_em`, de HU-07 e do glossário.

## Comportamento

### Estados do aviso

Fonte: [`diagrams/estados-aviso.mmd`](diagrams/estados-aviso.mmd).

O aviso é o objeto central do domínio: muda de situação ao longo do tempo e
aparece em mais critérios do que a conta. Ele tem dois estados, publicado e
arquivado, e cada transição aponta para um critério:

| Transição | Critério | Regra |
|---|---|---|
| Início para publicado | CA-03.1 | RN-01 |
| Publicado para arquivado | CA-07.1, com a recusa em CA-07.2 | RN-02 |
| Arquivado para o fim | CA-07.3 | Arquivado é final nesta versão |

Os dois estados são alcançáveis, e o arquivado é final declarado. O desenho
levantou três lacunas do `REQUISITOS.md`, e as três entraram lá pelo fluxo de
mudança depois da linha de base (#57):

1. A transição de publicado para arquivado não tinha critério, porque os
   critérios de HU-07 estavam previstos para o capítulo 8. Ganhou CA-07.1 a
   CA-07.5.
2. O estado arquivado não dizia se tinha saída, nem quem o vê. A equipe decidiu
   que ele é final e que só o autor o vê, e as duas decisões vão à demonstração
   do encontro 9.
3. A pergunta "o aviso publicado muda?" encontrou em E2 um pedido para alterar
   o próprio aviso, que não tinha virado necessidade. Virou N15 e HU-15, fora
   desta versão, e por isso o diagrama não tem transição de publicado para
   publicado.

A data de validade (HU-13) não cria estado: nesta versão ela só é mostrada, e o
aviso continua publicado depois dela.

### Sequência do fluxo principal

Preenchida na issue #58.

## Distribuição de responsabilidades

Preenchida na issue #58.

## Decisões de projeto

Os identificadores usam o prefixo `DP`, de decisão de projeto, para não
confundir com os documentos D1 e D2 do `DESCOBERTA.md`.

| Id | Decisão | Motivo | Consequência aceita |
|---|---|---|---|
| DP-01 | O modelo cobre HU-01 a HU-07 | São as histórias obrigatórias e importantes, previstas até a review final. Só com o MVP, o aviso teria uma situação só, e o diagrama de estados não mostraria nada | Tipo e data de arquivamento entram no modelo antes do código que os usa, que vem depois da review parcial |
| DP-02 | Aberto e interno como valor do atributo `tipo`, sem subclasse | Os dois tipos têm os mesmos atributos e operações; muda só quem lê | A regra de leitura precisa conferir o tipo do aviso |
| DP-03 | Chave artificial em todas as tabelas, com os nomes da conta como restrição de unicidade | O nome de usuário identifica a pessoa, e usá-lo como chave amarraria o banco a uma escolha que a pessoa fez ao criar a conta | Uma coluna a mais por tabela |
| DP-04 | Arquivar é o apagamento do aviso; nenhum aviso sai da tabela | O glossário diz que o arquivado continua guardado (N5) | Toda consulta do mural precisa filtrar a situação |
| DP-05 | Conta com avisos não pode ser apagada | Nenhuma história apaga conta, e apagar levaria junto a autoria que N7 exige | A conta de quem sai do curso fica até haver regra para isso |
| DP-06 | Instantes guardados com fuso e mostrados no horário de Palmas, com desempate pelo `id` | CA-04.3 pede a hora local, e CA-04.1 pede uma ordem fixa | A conversão de fuso acontece em toda tela que mostra hora |
| DP-07 | Nenhum índice além das chaves e unicidades até o RNF-01 ser medido | 200 avisos é pouco, e índice sem medição é suposição | Se o RNF-01 falhar, o primeiro reparo é um índice em `situacao` e `publicado_em` |

## Protótipo

Preenchido na issue #59.

## Conferência cruzada

Preenchida na issue #60.

## Histórico de revisão

- 2026-10-24: esqueleto e modelo de domínio (#55).
- 2026-10-24: modelo de dados e decisões de armazenamento (#56).
- 2026-10-24: diagrama de estados do aviso (#57).
