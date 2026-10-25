# Iterações

Este documento diz o que a equipe planejou em cada iteração, o que concluiu e o
que aprendeu. O `PROCESSO.md` diz como a equipe trabalha; aqui ficam os números
de cada ciclo e de onde cada um saiu. A iteração mais recente vem primeiro.

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
