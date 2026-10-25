# Iterações

Este documento diz o que a equipe planejou em cada iteração, o que concluiu e o
que aprendeu. O `PROCESSO.md` diz como a equipe trabalha; aqui ficam os números
de cada ciclo e de onde cada um saiu. A iteração mais recente vem primeiro.

## Review parcial (encontro 9)

### Preparação

**Código demonstrado:** o da tag `v0.7.0`. Depois dela entraram só documentos
e o script de restauração; `git diff v0.7.0 -- '*.py' templates static` não
devolve nada. Nenhum código entrou nas vinte e quatro horas antes da
apresentação.

**Ambiente:** o notebook de Bruno, com o banco `mini_mural_demo`, separado do
banco de desenvolvimento. `scripts/restaurar_demonstracao.sh SENHA` devolve o
banco ao passo 1 e recusa qualquer banco cujo nome não termine em `_demo`. O
notebook de Davi fica no mesmo commit, com o mesmo script.

**Papéis**, pela rotação do `PROCESSO.md`: Bruno demonstra, Carla narra, Davi
anota as observações nos três campos, Ana responde pelo backlog e Eva conduz a
tarefa com a servidora da secretaria.

**Declarado antes do passo 1:**

| Elemento | O que é | Como declarar |
|---|---|---|
| Contas | Do próprio Mini Mural, e não a conta institucional (RE-01, HU-12) | Antes do passo 1, em uma frase |
| Dados | Três contas e dois avisos fictícios; a conta da secretaria é criada na hora, com o nome para exibição "Secretaria do curso", sem nome de pessoa | Na abertura do passo 1 |
| Ambiente | Local, no notebook, sem hospedagem (A-11, R4) | No bloco de limites |
| Fora desta demonstração | Aviso aberto e interno (HU-05, HU-06), arquivar (HU-07), banco sem resposta (HU-03.2) e data de validade (HU-13), no backlog | No bloco de limites, com o item |
| Defeito conhecido | Depois de uma recusa, abrir de novo o endereço `/avisos/` mostra página vazia (#97, achado 5) | No bloco de limites |

**Roteiro.** As tarefas da secretaria são situadas, como na V1, sem explicar a
tela.

| Passo | Ação | O que o público vê | Critério |
|---:|---|---|---|
| 1 | Abrir o mural sem conta | A página de entrar, com o caminho de volta | CA-02.3 |
| 2 | A servidora cria a conta e escolhe "prof. de cálculo" como nome para exibição | A recusa, porque o nome já existe | CA-01.6 |
| 3 | Ela troca para "Secretaria do curso" | O mural, já com o nome dela no topo | CA-01.1, CA-02.1 |
| 4 | "Avise a turma de que a aula de amanhã mudou para a sala 12" | O aviso no topo, com os dois nomes, a data e a hora | CA-03.1, CA-04.1, CA-04.3 |
| 5 | Colar o texto preparado de 567 caracteres (`scripts/texto-longo-da-demonstracao.txt`) | A recusa com a contagem, e o texto mantido | CA-03.3 |
| 6 | Recarregar o mural | O mesmo número de avisos | RNF-03 |
| 7 | Sair; um integrante entra como `aluno.demo` pelo celular | O aviso da secretaria no mural do aluno | CA-02.4, CA-03.5 |

**Ordem e tempo**, para os 15 minutos combinados com o professor: problema e
usuário, 1 min 30 s (Lívia e Paula, `DESCOBERTA.md`); especificação, 2 min
(backlog e MVP); modelagem e arquitetura, 2 min (modelo de domínio e A-01);
demonstração, 7 min; limites e próximos passos, 2 min 30 s. Se o tempo
apertar, o corte começa pelo problema e pela especificação; os limites nunca
saem.

**Decisões a defender**, com a linha de cada uma:

- **A-01**, uma aplicação só no lugar do frontend separado com API que o livro
  recomenda. "E se vier um aplicativo?": a API é escrita depois, sobre o mesmo
  domínio, e é a consequência aceita na linha.
- **A-04**, conta própria só com os campos do `PROJETO.md`. "E se a
  coordenação quiser desativar uma conta?": pelo terminal, com
  `desativar()`, como diz a linha.
- **DP-04**, arquivar é o apagamento do aviso.
- **R9**, nome que imita outra pessoa: CA-01.6 e o nome de usuário no mural, e
  o risco que sobra vai à revisão de C2.

**Plano da falha:** reiniciar o servidor e restaurar o banco com o script;
se falhar de novo, o notebook de Davi; por último, a gravação do ensaio,
declarada como gravação, se o professor a aceitar como evidência.

**Ensaio.** O roteiro foi percorrido no banco da demonstração, do passo 1 ao 7,
e o banco foi restaurado pelo script depois. O ensaio achou um problema do
roteiro: o texto longo, escrito na hora, tinha menos de 500 caracteres e foi
publicado em vez de recusado. O passo 5 passou a usar um texto preparado, com
a contagem conferida, guardado em `scripts/`.

### O que aconteceu

> Registro simulado. Este repositório é o projeto exemplo do livro, com equipe e
> usuários simulados (ver `ROTEIRO.md`). A review abaixo ilustra o que uma
> apresentação real produziria; em um projeto da disciplina, cada linha teria
> uma pessoa de verdade por trás.

A demonstração seguiu o roteiro do passo 1 ao 7, sem falha, em 14 minutos. A
servidora da secretaria fez os passos 2 a 5. Davi anotou as observações nos
três campos, e cada uma ganhou tipo e destino depois da aula.

### Observações

| Quem | O que foi dito | Evidência vista | Tipo | Destino |
|---|---|---|---|---|
| Professor | "Por que não um frontend separado, com API, como o capítulo 7 recomenda?" E depois: "E se vier um aplicativo?" | Visão geral e A-01 | Dúvida sobre decisão | Respondida pela linha A-01, com a consequência aceita; sem item |
| Servidora da secretaria | Depois de publicar, perguntou como corrigir um erro de digitação no aviso | Passo 4 | Necessidade já registrada, com segunda fonte | N15 e HU-15 revistas (#100) |
| Equipe colega | "O aluno precisa criar conta para ver qualquer aviso? Muitos não vão criar." | Passos 1 e 7 | Necessidade já registrada (N3, HU-06) | Ordem do backlog revista (#100) |
| Professor | "O que acontece se o banco cair no meio da publicação?" A equipe respondeu: hoje, a página de erro do framework; HU-03.2 está no backlog, sem critério | Bloco de limites | Dúvida com resposta incompleta | Critério para HU-03.2 (#100) |
| Davi, ao cronometrar | A servidora publicou no passo 4 em 1 minuto e 35 segundos, sem pedir ajuda | Passo 4 | Medição do RNF-02 | Autoavaliação |
| Equipe, no bloco de limites | Abrir de novo `/avisos/` depois de uma recusa mostra página vazia | Declarado; achado 5 da #97 | Defeito | Item novo (#100) |

### Autoavaliação

Status na data da review, com a regra do capítulo 9: atendido quer dizer
integrado ao `main` e verificado por quem não escreveu o código.

| Critério ou requisito | Status | Evidência |
|---|---|---|
| CA-01.1 a CA-01.6 | Atendido | #91, com a lista de critérios de Bruno; passos 2 e 3 |
| CA-02.1 a CA-02.3 | Atendido | #92, com a lista de Ana; passos 1 e 3 |
| CA-02.4 | Atendido | #92 e #94; passo 7 |
| CA-03.1 a CA-03.5 | Atendido | #94, com a lista de Eva; passos 4 e 5 |
| CA-04.1 a CA-04.3 | Atendido | #93, com a lista de Carla; passos 4 e 7 |
| RNF-01 | Atendido | Medido na #95: 350 ms, no notebook; repetir com a hospedagem |
| RNF-02 | Atendido, como indício | Uma pessoa, na review: 1 min 35 s, sem ajuda |
| RNF-03 | Atendido | Teste na #94; passo 6 |
| RNF-04 | Atendido | Teste da senha guardada como valor derivado, desde a #80 |
| RNF-05 | Atendido | Teste na #93 |
| RNF-06 | Não iniciado | Depende de HU-05 |
| RNF-07 | Não iniciado, em parte | RN-01 está só em `pode_publicar`; as regras de ler e arquivar ainda não existem |
| RNF-08 | Atendido | Conferido em 360 por 640 nas quatro páginas |
| UC-01, 4e | Não iniciado | HU-03.2, sem critério na data da review |
| HU-05, HU-06, HU-07, HU-13 | Não iniciado | Declarados no bloco de limites |

## Iteração 3 (encontros 7 a 9)

A primeira iteração de código, e a que chega à review parcial.

**Meta:** no encontro 9, uma pessoa da secretaria cria uma conta e publica um
aviso, e um aluno com conta o vê no topo do mural, com o nome de quem publicou,
a data e a hora, no ambiente da demonstração.

### Capacidade

A equipe ainda não tem velocidade: as iterações 1 e 2 produziram documentos, e
documento não foi estimado em pontos. As cinco pessoas estão disponíveis em
tempo integral nesta iteração. A previsão é de 14 pontos, a soma dos itens
abaixo, e ela se apoia em uma suposição declarada: esses itens são os que o
capítulo 5 estimou em 28 das 50 horas da iteração (`REQUISITOS.md`, "Esforço
até a review parcial"). Os pontos concluídos ao fim desta iteração serão a
primeira velocidade observada, e uma observação ainda não diz a variação.

### Estimativa

A escala é 1, 2, 3, 5, 8 e 13, e o item de referência é HU-02, entrar e sair,
com 2 pontos. Cada integrante escolheu a carta em privado, e as cartas foram
reveladas juntas. A rodada que mais divergiu foi a de HU-03:

| Pessoa | 1ª rodada | O que disse | 2ª rodada |
|---|---:|---|---:|
| Ana | 3 | Um formulário e uma gravação | 5 |
| Bruno | 5 | O texto tem quatro recusas no contrato | 5 |
| Carla | 8 | A alternativa 4e pede tratar a falha do banco e manter o texto, e há o contador | 5 |
| Davi | 5 | Igual ao Bruno | 5 |
| Eva | 5 | Igual ao Bruno | 5 |

A divergência de 3 a 8 mostrou que a história juntava duas coisas, e a equipe
não fez a média. HU-03 foi dividida: HU-03.1, publicar com as recusas de texto
e de sessão, com 5 pontos na segunda rodada; e HU-03.2, recusar quando o banco
não responde (UC-01, 4e), com 2 pontos, como item importante, porque a
alternativa ainda não tem critério e não é necessária para a demonstração.

| Item | MoSCoW | Pontos |
|---|---|---:|
| HU-01 Criar conta | Obrigatório | 3 |
| HU-02 Entrar e sair | Obrigatório | 2 |
| HU-03.1 Publicar aviso curto | Obrigatório | 5 |
| HU-04 Ver o mural | Obrigatório | 3 |
| HU-05 Marcar o aviso como aberto ou interno | Importante | 3 |
| HU-06 Ler aviso aberto sem conta | Importante | 2 |
| HU-07 Arquivar o próprio aviso | Importante | 3 |
| HU-03.2 Recusar a publicação quando o banco não responde | Importante | 2 |
| HU-13 Informar até quando o aviso vale | Desejável | 2 |

Os obrigatórios somam 13 pontos de 25, 52%, abaixo dos 60% da regra do MoSCoW.
Os itens fora desta versão não foram estimados.

### Plano

| Ordem | Item | Pontos | Necessário para a demonstração | Responsável |
|---:|---|---:|---|---|
| 1 | HU-01 Criar conta (#84) | 3 | Sim | Ana |
| 2 | HU-02 Entrar e sair (#85) | 2 | Sim | Eva |
| 3 | HU-04 Ver o mural (#86) | 3 | Sim | Davi |
| 4 | HU-03.1 Publicar aviso curto (#87) | 5 | Sim | Carla e Bruno, em par |
| 5 | Preparar a demonstração do encontro 9 (#88) | 1 | Sim | Eva |
| | Total | 14 | | |

HU-04 vem antes de HU-03.1, invertendo a ordem do backlog. O critério CA-03.1
só se verifica vendo o aviso no topo do mural, e o modelo do aviso, que as duas
usam, entra com o mural. A dependência registrada no backlog, de HU-04 sobre
HU-03, é de dado; com o modelo pronto, a ordem técnica se inverte.

A preparação da demonstração é trabalho que não é história, e entra no plano
com 1 ponto: dados de demonstração, roteiro, confirmação da presença da
secretaria (R1), medição do RNF-01 e um ensaio. Nesta iteração não há reserva
para trabalho técnico; a partir da iteração 4, os capítulos 12 a 14 pedem testes
automatizados na integração contínua, segurança e implantação, e a equipe
reserva 2 pontos por iteração para eles.

**Corte da review.** Tudo o que a demonstração usa está integrado ao `main` na
véspera do encontro 9, e nada é integrado nas últimas vinte e quatro horas
antes da apresentação. O que não estiver integrado não aparece na review.

### Quadro

O quadro é a lista de issues do milestone `v0.7.0`, com etiquetas no lugar das
colunas. O token da equipe não tem a permissão que o GitHub Projects exige, e a
etiqueta faz o mesmo papel com o que já existe:

| Coluna | Como aparece | Ligação com a definição de pronto |
|---|---|---|
| Backlog | Issue aberta sem etiqueta de estado | Nenhuma ainda |
| Em andamento | Etiqueta `estado:em-andamento`, no máximo 2 | Nenhuma |
| Em revisão | Etiqueta `estado:em-revisao`, no máximo 2 | Revisão por outra pessoa |
| Bloqueado | Etiqueta `estado:bloqueado`, com o nome de quem foi acionado | Nenhuma |
| Pronto | Issue fechada pelo pull request integrado, com os critérios verificados no comentário de revisão | Todos os pontos |

Com o limite de dois itens em revisão, quem termina o próprio item revisa o de
alguém antes de abrir o seu.

### Preparação da demonstração

Registro da #88, feita com tudo integrado ao `main`.

- **Dados.** `python manage.py carregar_demonstracao --senha VALOR` cria três
  contas de demonstração e dois avisos, sem dado de pessoa real. A senha vem do
  argumento; o código não guarda senha. Com `--avisos 200`, o mural fica na condição do
  RNF-01.
- **Roteiro.** Duas tarefas, situadas como na validação V1, sem explicar a
  tela. A servidora da secretaria: "Avise a turma de que a aula de amanhã mudou
  de sala", começando pela página de criar conta. Um integrante, com a conta
  `aluno.demo` no celular: "Veja se há aviso novo". A equipe observa e anota o
  que a pessoa procurou, como na V1.
- **R1.** A secretaria confirmou que uma servidora vai ao encontro 9 (registro
  simulado, como o D2).
- **RNF-01.** Medido no notebook da demonstração, com 200 avisos, no navegador
  com a rede limitada ao perfil "Fast 4G" e a tela de 360 por 640: 350, 345 e
  348 milissegundos até o fim da carga, 53 kB transferidos. Vale o maior, 350
  milissegundos, dentro do aceitável (3 segundos) e do pretendido (1 segundo).
  O servidor estava na mesma máquina; com hospedagem, a medição se repete
  (capítulo 14).
- **RNF-08.** Criar conta, entrar, mural e publicar conferidos em 360 por 640,
  sem rolagem horizontal e com texto de 16 pixels.
- **Ensaio.** O roteiro foi percorrido uma vez: criar conta, publicar, sair,
  entrar com `aluno.demo` e ver o aviso no topo. Nenhum ajuste no código.

### Situação na véspera do encontro 9

Integrado ao `main`: HU-01 (#91), HU-02 (#92), HU-04 (#93), HU-03.1 (#94) e a
preparação da demonstração (#95), 14 dos 14 pontos planejados. HU-04 só fechou
depois da medição do RNF-01, porque o ponto 4 da definição de pronto pede os
requisitos não funcionais conferidos. A velocidade da iteração é registrada no
fim dela, depois da demonstração e com a observação de quem usou, no capítulo
9.

As duas decisões da retrospectiva já podem ser conferidas. `contas/` tem quatro
autores, e `avisos/` também. Os quatro pull requests de história (#91 a #94)
têm o comentário com a lista dos critérios verificados por quem não escreveu o
código.

## Iterações 1 e 2 (encontros 3 a 7)

A iteração 1 produziu o `PROCESSO.md`, o `DESCOBERTA.md` e o `REQUISITOS.md`
(versões 0.2.0 a 0.4.0). A iteração 2 produziu o `PROJETO.md`, o
`ARQUITETURA.md` e o esqueleto do código (versões 0.5.0 e 0.6.0). As duas
fecharam o que planejaram. Esta é a primeira retrospectiva com evidência, e
cobre as duas juntas.

### Evidências

| Evidência | Valor | Fonte |
|---|---|---|
| Issues planejadas e fechadas | Iteração 1: 20 e 20. Iteração 2: 15 e 15 | Milestones `v0.2.0` a `v0.6.0` |
| Pull requests integrados | Iteração 1: 21. Iteração 2: 15 | `gh pr list --state merged` |
| Tempo entre abrir e integrar um pull request | Média de 12 a 33 segundos por versão | `gh pr list`, com a diferença entre as datas |
| Integrações por dia no `main` | 7 em 2026-10-23 e 36 em 2026-10-24, em todo o histórico | `git log --first-parent origin/main`, contado por data |
| Pull requests com pedido de mudança na revisão | 6: #46, #47, #63, #64, #77 e #80 | Comentários de revisão com a palavra "pedido" |
| Achados das revisões com roteiro | 14: lista de verificação (5, #39), validação V1 (4, #40), conferência cruzada (2, #60) e duplas trocadas (3, #74) | Issues e registros |
| Mudanças de requisito depois da linha de base | 3: #53, #63 e #57 | Histórico do `REQUISITOS.md` |
| Autoria do código | `contas/`, `avisos/` e `config/`: só Bruno | `git shortlog -sn HEAD -- pasta` |

### Leitura

Os números de tempo e de integração por dia não medem a equipe. O projeto é
simulado, e o histórico foi produzido em dois dias; a média de segundos entre
abrir e integrar um pull request mede a simulação, e com ela a equipe não
consegue julgar se integra com frequência. A conclusão honesta é que esses dois
números ficam sem leitura até a iteração 3, a primeira com trabalho distribuído
no tempo.

Os outros números dizem mais. A revisão comum pediu mudança em 6 de 36 pull
requests das duas iterações, e a contagem pela palavra "pedido" pode ter
perdido algum escrito de outro jeito, como a redução do MVP no #29. As quatro
revisões com roteiro encontraram 14 achados, e cada uma encontrou pelo menos
dois. A diferença sugere que o roteiro pesa mais do que a simples presença de
uma segunda pessoa. Com quatro sessões, isso é indício, ainda sem valor de
medida.

O código tem um autor só, e a iteração 3 é a primeira em que todos escrevem
código. Se só uma pessoa conhecer `contas/`, a review parcial depende dela.

### Decisões

| Mudança | Dono | Como conferir | Quando conferir |
|---|---|---|---|
| Quem implementa uma história em um módulo não é quem o criou; nesta iteração, HU-01 e HU-02, em `contas/`, ficam com Ana e Eva | Ana | `git shortlog -sn HEAD -- contas avisos`: cada módulo com pelo menos dois autores | Retrospectiva da iteração 3, no encontro 9 |
| Quem revisa uma história verifica os critérios no pull request, um por um, com o teste ou o passo manual de cada um, que é o ponto 1 da definição de pronto aplicado pela primeira vez a código | Davi | Todo pull request de história da iteração 3 tem o comentário com a lista dos critérios | Retrospectiva da iteração 3 |

### Práticas de Extreme Programming

| Prática | O que o histórico respondeu | Decisão |
|---|---|---|
| Integração frequente | Nada: o tempo dos pull requests mede a simulação | Um pull request por história, revisado no mesmo dia; os números voltam na retrospectiva da iteração 3 |
| Programação em par | O tempo dos pull requests não serve de dado | HU-03.1 em par, Carla e Bruno, porque é a fatia que atravessa página, regra e banco, e é onde R3 pesa mais |
| Propriedade coletiva | O código tem um autor só | A primeira decisão da retrospectiva |

### Riscos revisados

- **R1**, secretaria indisponível: a demonstração depende de alguém da
  secretaria no encontro 9. Eva confirma a presença na preparação (#88).
- **R3**, ninguém conhece framework web, contas e banco: está acontecendo nesta
  iteração. A resposta é a ordem do plano, contas e banco primeiro, e o par em
  HU-03.1.
- **R4**, hospedagem: a demonstração roda no notebook de um integrante, como
  diz o `ARQUITETURA.md`; as opções continuam com prazo no encontro 12.
- **R9**, nome que imita outra pessoa: CA-01.6 entra nesta iteração, com HU-01.
- **R6** está encerrado; **R7** e **R8** seguem aceitos, sem ocorrência.
