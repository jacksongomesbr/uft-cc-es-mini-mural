# Projeto

Este documento diz de que o Mini Mural é feito. O `DESCOBERTA.md` diz de onde
cada necessidade veio, o `REQUISITOS.md` diz o que o sistema faz e o
`PROCESSO.md` diz como a equipe trabalha. Onde cada parte roda e como as partes
conversam é decisão do capítulo 7, no `ARQUITETURA.md`; por isso este documento
não usa nome de framework, de tabela gerada nem de biblioteca.

As fontes dos diagramas ficam em `diagrams/`, em texto Mermaid, uma fonte por
diagrama, e o GitHub desenha cada uma na página do arquivo. Quem altera o
código que um diagrama descreve altera o diagrama no mesmo pull request.

O que a equipe mantém até o fim do semestre: o modelo de domínio, o modelo de
dados e, enquanto a situação do aviso for regra de negócio, o diagrama de
estados. A sequência, a atividade e a ficha de responsabilidades resolvem uma
dúvida cada e podem ser apagadas depois que o código existir; a decisão que
cada uma sustentou fica na tabela de decisões.

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
| CA-07.1, CA-07.3 | Situação e instante do arquivamento, que não muda depois de gravado | `situacao`, `arquivado_em` |
| CA-07.2 | Autor, para recusar quem não é | `autor_id` |
| CA-07.4, CA-07.5 | Situação e autor, para decidir quem vê | `situacao`, `autor_id`, `arquivado_em` |

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

Fonte: [`diagrams/sequencia-publicar.mmd`](diagrams/sequencia-publicar.mmd).

O desenho cobre o fluxo principal do UC-01 e as alternativas 4a e 4b. Os nomes
dos participantes são provisórios; o capítulo 7 decide onde cada um roda. Três
decisões ficam visíveis no desenho:

- o aviso confere o texto antes do registro, e por isso a recusa não grava nada
  (CA-03.2);
- o registro atribui o instante da publicação (DP-10);
- o mural mostrado depois da publicação sai do que foi registrado, e por isso
  mostra o que ficou gravado.

Como a tela evita publicar de novo quando a pessoa recarrega a página (RNF-03)
depende de como a tela conversa com o servidor, e é decisão do capítulo 7.

### Aviso vencido de outra pessoa

Fonte: [`diagrams/atividade-aviso-vencido.mmd`](diagrams/atividade-aviso-vencido.mmd).

O fluxo atravessa duas pessoas, e a decisão fica fora do sistema. A secretaria
não arquiva o aviso de outra pessoa (RN-02, D2): ela pede ao autor, por fora, e
o sistema só registra o que o autor fizer. Se o autor não arquivar, o aviso
continua no mural, e é esse o caso que N12 e HU-08 guardam para depois.

## Distribuição de responsabilidades

A pergunta que distribui é "quem já tem a informação para cumprir isto?". A
regra do aviso fica no aviso, porque é ele que conhece o texto, o tipo, a
situação e o autor.

| Parte | Sabe | Faz |
|---|---|---|
| Conta | Nome de usuário, nome para exibição, valor derivado da senha | Confere a senha; compara nomes sem espaços a mais e sem diferenciar maiúsculas (CA-01.2, CA-01.6); diz se pode publicar (RN-01) |
| Aviso | Texto, tipo, situação, autor, instantes | Confere o texto (CA-03.2 a CA-03.4), pela função `preparar_texto` do módulo do aviso; diz se pode ser visto por uma pessoa (RNF-06, CA-07.4, CA-07.5); diz se pode ser arquivado por uma conta e se arquiva (RN-02, CA-07.1 a CA-07.3) |
| Mural | Nada próprio: é uma consulta | Lista os avisos publicados que uma pessoa pode ver, do mais recente para o mais antigo, com o desempate de DP-06 (CA-04.1) |
| Registro de avisos | Onde os avisos ficam guardados | Grava e recupera avisos e atribui o instante da publicação (DP-10) |
| Tela de publicação | Nada do domínio | Recebe o texto, mostra a recusa com o texto mantido e mostra o mural; não decide regra nenhuma (DP-08) |

A ficha do aviso, na sessão de responsabilidades, com o cenário da troca de
sala publicada e arquivada no dia seguinte:

```text
+-------------------------------------------------------------+
| Aviso                                                       |
+----------------------------------+--------------------------+
| Responsabilidades                | Colaboradores            |
| - conhecer texto, tipo, situacao |                          |
| - conferir o texto               |                          |
| - dizer se pode ser visto        | Conta (quem pede)        |
| - dizer se pode ser arquivado    | Conta (quem pede)        |
| - arquivar, com o instante       | Registro de avisos       |
+----------------------------------+--------------------------+
```

As responsabilidades couberam na ficha, e nenhuma ficou sem dono.

### Teste de Parnas

O teste conta quantos lugares a mudança mais provável obriga a alterar.

- **Quem publica.** É a mudança que D2 já anuncia: a coordenação revê C2 depois
  do encontro 9, e R9 leva a ela a opção de restringir a publicação a
  servidores e professores. A mudança toca a regra "pode publicar", em um lugar
  só, na conta (DP-08), e uma coluna nova na conta, com o papel. Ela também
  exige um jeito de marcar esse papel, que não existe e depende de quem a
  coordenação indicar, porque a secretaria não quer administrar contas (E1).
- **Limite do texto.** Já mudou uma vez, de 280 para 500, na V1. A mudança toca
  a constante do aviso e a restrição do banco: dois lugares, aceitos em DP-09,
  e alterados no mesmo pull request. A tela mostra o limite lendo o valor do
  aviso.

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
| DP-07 | Nenhum índice escolhido pela equipe além das chaves e unicidades até o RNF-01 ser medido. O framework cria, por conta própria, um índice na chave estrangeira do autor e um índice de busca por prefixo no nome de usuário único, e os dois ficam | 200 avisos é pouco, e índice sem medição é suposição. O RNF-01 foi medido em 350 ms (`ITERACOES.md`) | Se o RNF-01 falhar com a hospedagem, o primeiro reparo é um índice em `situacao` e `publicado_em` |
| DP-08 | As regras de publicar, ler e arquivar ficam na conta e no aviso, e nenhuma na tela | RNF-07 pede cada regra em um lugar só, e RN-01 tem prazo (D2) | A tela pergunta ao aviso e à conta em vez de conferir sozinha |
| DP-09 | O limite de 500 caracteres fica no aviso e é repetido como restrição do banco | A restrição é a segunda barreira contra gravação que não passe pela tela | Mudar o limite toca dois lugares, no mesmo pull request |
| DP-10 | O registro atribui o instante da publicação | CA-03.1 pede a hora da publicação, e o relógio do aparelho de quem publica não é confiável | A tela mostra a hora que o registro devolveu |

## Protótipo

Protótipo navegável do fluxo principal em [`prototipo/`](prototipo/), com as
recusas previstas. O [`prototipo/README.md`](prototipo/README.md) diz por onde
começar.

### Sequência de telas

Cada passo do UC-01 em que a pessoa decide ou fornece alguma coisa tem tela; o
passo em que só o sistema trabalha vira mensagem quando o fluxo alternativo
acontece.

| Passo do UC-01 | Tela ou mensagem | Critério |
|---|---|---|
| Pré-condição: entrar | Entrar; criar conta | HU-01, HU-02, CA-01.1 |
| 1. Abrir o mural e escolher publicar | Mural | CA-04.1 |
| 2 e 3. Escrever e confirmar | Publicar aviso, com o contador de caracteres | CA-03.3 |
| 4. Registrar e mostrar | Mural com o aviso no topo | CA-03.1 |
| 1a. Não entrou | Entrar | CA-02.3 |
| 4a. Texto vazio | Publicar aviso, com a recusa | CA-03.2 |
| 4b. Acima do limite | Publicar aviso, com a recusa e o texto mantido | CA-03.3 |
| 4c. Saiu da conta em outra aba | Entrar, com a recusa | CA-02.4 |
| 4d. Recarregar a página | Nenhuma: nada acontece (RNF-03) | RNF-03 |
| 4e. Falha ao gravar | Publicar aviso, com a mensagem e o texto mantido | Sem critério ainda |

Fora do fluxo principal, a recusa do nome para exibição em uso (CA-01.6) também
tem tela, porque é a defesa que o #53 acrescentou contra R9.

### Forma

O capítulo 6 recomenda um arquivo de apresentação com ligações entre slides. A
equipe usou uma página HTML estática, com uma tela por seção e ligações entre
elas, porque ela abre em qualquer navegador sem ferramenta paga, é texto e pode
ser revisada em pull request como os diagramas. A aparência é de rascunho de
propósito: sem cor nem marca, para o comentário ficar no fluxo.

O protótipo cobre a fatia do MVP. As telas de HU-05 a HU-07, tipo do aviso e
arquivamento, entram no planejamento da iteração em que essas histórias
entrarem.

## Conferência cruzada

Em 2026-10-24, Davi, que desenhou o modelo, leu o protótipo, e Carla, que
montou o protótipo, leu o modelo, com as seis perguntas da tabela de
conferência do capítulo 6. O registro completo está na #60.

| Achado | Correção |
|---|---|
| CA-07.1 a CA-07.5 entraram depois do modelo de dados e não tinham linha em "O dado que cada critério exige" | Três linhas acrescentadas; o dado já existia |
| O protótipo dizia "conta fechada", que pelo glossário sugere conta apagada | A recusa 4c e a primeira tela passam a dizer "saiu da conta em outra aba", como o UC-01 |

Ficaram como estão, com motivo: `tipo` e `arquivado_em` sem tela no protótipo,
porque HU-05 e HU-07 estão fora da fatia do MVP, e a alternativa 4d sem tela,
porque nela nada acontece.

## Histórico de revisão

- 2026-10-24: esqueleto e modelo de domínio (#55).
- 2026-10-24: modelo de dados e decisões de armazenamento (#56).
- 2026-10-24: diagrama de estados do aviso (#57).
- 2026-10-24: sequência, atividade, responsabilidades e teste de Parnas (#58).
- 2026-10-24: protótipo navegável do fluxo principal (#59).
- 2026-10-24: conferência cruzada e correções (#60).
- 2026-10-24: conferência contra o código antes da review parcial (#97): índices que o framework cria (DP-07) e onde mora a regra do texto.
