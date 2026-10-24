# Processo de desenvolvimento

Decisão da equipe no encontro 3. Este arquivo muda por pull request, como
qualquer outro, e cada mudança entra no histórico ao final.

## Escolha e justificativa

Iterativo e incremental, com iterações de duas semanas e pontos de controle
escritos a cada marco da disciplina.

A equipe avaliou os cinco fatores de Boehm e Turner. Cada integrante fez a
própria avaliação antes da aula, registrada na #12, e as divergências foram
resolvidas na discussão.

| Fator | Puxa para | Justificativa |
|---|---|---|
| Tamanho | Ágil | Cinco pessoas, na mesma turma e em contato direto. |
| Criticidade | Ágil | Um aviso fora do ar incomoda e se corrige; o sistema não guarda dado pessoal sensível. |
| Dinamismo | Ágil | As regras do `PROBLEMA.md` são hipóteses, e ninguém conversou ainda com a secretaria. |
| Pessoal | Plano-dirigido | É a primeira vez que a equipe constrói um sistema junto, e ninguém decidiu arquitetura antes. |
| Cultura | Ágil | A disciplina aceita ajuste, desde que registrado. |

Duas divergências apareceram:

- **Dinamismo.** O Bruno avaliou como baixo, porque as regras já estavam
  escritas. A equipe concluiu que regra escrita pela própria equipe, sem
  conversa com o usuário, é hipótese, e que o dinamismo é alto.
- **Pessoal.** A Carla avaliou como ágil, contando com a experiência do Davi em
  Django. O Davi esclareceu que fez só um tutorial, e o fator ficou em
  plano-dirigido.

## Compensação para o fator pessoal

O único fator que puxou para plano-dirigido foi o pessoal. A equipe compensa
com três práticas:

- **Verificação frequente:** um artefato escrito a cada marco e revisão de
  outra pessoa em toda contribuição, como já exige o `CONTRIBUTING.md`.
- **Primeira decisão em par:** toda decisão técnica que a equipe toma pela
  primeira vez, como a estrutura do projeto Django ou o modelo do banco, é feita
  por duas pessoas e registrada com a alternativa descartada. A partir do
  capítulo 7, o registro vai para o `ARQUITETURA.md`.
- **Dúvida não espera:** uma dúvida técnica que trave uma tarefa por mais de um
  dia vira comentário na issue e pergunta ao professor no encontro seguinte.

## Iteração

- **Duração:** duas semanas, começando no dia do encontro.
- **Planejamento:** 30 minutos, no início do encontro que abre a iteração.
- **Acompanhamento:** um comentário curto por dia na issue em andamento, com o
  que foi feito e o que trava. A equipe é simulada e não tem um canal de
  mensagens; o comentário na issue deixa o registro junto do trabalho.
- **Demonstração:** no encontro que fecha a iteração, com o usuário quando ele
  puder estar presente.
- **Retrospectiva:** 15 minutos, logo depois da demonstração, com três
  perguntas: o que funcionou, o que atrapalhou e o que muda na próxima. Até o
  capítulo 8, o registro fica na issue da iteração; depois, no `ITERACOES.md`.

### Iterações até cada marco

Os encontros são semanais, então o número do encontro também conta as semanas.

| Iteração | Encontros | Duração | Termina no marco |
|---|---|---|---|
| 1 | 3 a 5 | 2 semanas | Encontro 5: requisitos |
| 2 | 5 a 7 | 2 semanas | |
| 3 | 7 a 9 | 2 semanas | Encontro 9: review parcial |
| 4 | 9 a 11 | 2 semanas | |
| 5 | 11 a 12 | 1 semana | Encontro 12: qualidade |
| 6 | 12 a 14 | 2 semanas | |
| 7 | 14 a 16 | 2 semanas | Encontro 16: review final |

Cabem uma iteração até o marco do encontro 5, três até o do 9, cinco até o do
12 e sete até o do 16. Do encontro 3 ao 12 são nove semanas, que não fecham em
iterações de duas; a iteração 5 tem uma semana só, para que o marco do
encontro 12 coincida com o fim de uma iteração.

## Quando o processo oposto seria o certo

Um processo dirigido por plano, com requisitos fechados antes da construção,
seria a decisão correta se o mural publicasse avisos oficiais com prazo e forma
definidos em norma da universidade. Nesse caso o requisito viria pronto e
estável, um aviso perdido poderia causar prejuízo a um aluno, e a
previsibilidade valeria mais que a capacidade de mudar. Nada disso vale hoje:
o mural complementa os canais existentes, e as regras ainda vão ser
descobertas com os usuários.

## Papéis

- **Prioriza o backlog:** Ana. Ela também decide quando uma divergência técnica
  não se resolve em dois turnos de comentário, como diz o `CONTRIBUTING.md`.
- **Conduz a demonstração:** rodízio, nesta ordem: Bruno, Carla, Davi, Eva e
  Ana, recomeçando pelo Bruno.
- **Conversa com cada grupo de usuários:** como no `PROBLEMA.md`: Eva com a
  secretaria, Davi com os professores, Carla com o centro acadêmico, Ana e
  Bruno com os colegas de turma.
- **Demais decisões técnicas:** quem estiver na tarefa, seguindo o
  `CONTRIBUTING.md` e a compensação acima.

## Definição de pronto

Um item está pronto quando:

1. Todos os critérios de aceitação foram verificados por alguém que não
   escreveu o código do item.
2. O código está integrado ao `main` por pull request revisado, com o
   comentário de aprovação registrado.
3. A funcionalidade está acessível no ambiente que a equipe usa para
   demonstrar, que o `ARQUITETURA.md` define no capítulo 7.
4. Os requisitos não funcionais que se aplicam ao item foram conferidos, como
   diz o "Como verificar" de cada um no `REQUISITOS.md`.
5. A issue fechada referencia a história, e a história tem a origem registrada
   no `REQUISITOS.md`.

Para documento, como os deste repositório até o capítulo 6, valem os pontos 2
e 5: pull request revisado e issue fechada, ligada ao item de origem.

O critério de aceitação vale para um item e diz como ele se comporta; esta
definição vale para todos e diz o padrão de trabalho da equipe. Item que atende
a quatro dos cinco pontos na véspera da review continua não pronto.

A lista cresce nos capítulos 11 e 12, com teste automatizado e verificação na
integração contínua.

## Histórico de revisão do processo

- 2026-10-24: versão inicial (#13).
- 2026-10-24: definição de pronto com os cinco pontos do capítulo 5 (#41).
