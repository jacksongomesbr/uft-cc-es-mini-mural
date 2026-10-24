# Requisitos

Este documento diz o que o Mini Mural vai fazer. O `DESCOBERTA.md` diz de onde
cada necessidade veio, e o `PROCESSO.md` diz como a equipe trabalha. Cada item
daqui aponta para uma origem no `DESCOBERTA.md`, ou para um documento externo
no caso das regras de negócio e das restrições.

O estado deste arquivo no `main` na tag `v0.4.0` é a linha de base do primeiro
marco. Depois dela, toda mudança de requisito passa por pull request, com a
análise de impacto feita pela tabela de rastreabilidade e uma linha no
histórico.

## Glossário do domínio

| Termo | Definição | Fonte |
|---|---|---|
| Arquivar | Tirar o aviso do mural sem apagá-lo. As fontes dizem também "tirar do mural" e "retirar"; o projeto usa só "arquivar" | N5, E1, E2 |
| Autor | A conta que publicou o aviso. O mural mostra o nome de usuário dessa conta | N7, E2, E5 |
| Aviso | Mensagem de texto publicada no mural, com autor, data e hora de publicação | N1, E1, E2 |
| Aviso aberto | Aviso que qualquer pessoa lê, com conta ou sem conta | N3, C1 |
| Aviso arquivado | Aviso que saiu do mural e continua guardado, com a data e a hora em que foi arquivado, para quem precisar saber o que já foi avisado | N5, E1 |
| Aviso curto | Aviso de até 280 caracteres, contados depois de tirar os espaços das pontas. O valor é da equipe, sem fonte, e vai à validação V1 | N1 |
| Aviso interno | Aviso que só quem entrou com uma conta lê. É o tipo padrão ao publicar | N4, C1 |
| Aviso publicado | Aviso que está no mural. Todo aviso nasce publicado | N1 |
| Aviso vencido | Aviso cujo assunto já passou, como evento realizado ou prazo encerrado, e que continua no mural | O1, D1 |
| Avisos que valem agora | Nesta versão, os avisos publicados. O sistema não conhece a data em que o assunto de um aviso passa, e quem tira o aviso vencido do mural é o autor | N2, E4, D2 |
| Comunicado oficial | Aviso com edital anexo ou com prazo da coordenação. Continua no e-mail institucional, fora do mural | D2 |
| Conta | Nome de usuário e senha criados no próprio Mini Mural. Não é a conta institucional da universidade | N11, R2 |
| Mural | A lista dos avisos publicados, os mais recentes primeiro | N2, D1 |
| Visitante | Pessoa que lê o mural sem entrar com uma conta | N3 |

## Backlog ordenado

| Ordem | Item | Origem | MoSCoW | Risco técnico | Depende de |
|---:|---|---|---|---|---|
| 1 | HU-01 Criar conta | N1, N4, N7 | Obrigatório | Alto: contas de usuário em Django, que ninguém na equipe conhece (R3) | — |
| 2 | HU-02 Entrar e sair | N7 | Obrigatório | Alto: sessão e senha, pela mesma razão | HU-01 |
| 3 | HU-03 Publicar aviso curto | N1, N7 | Obrigatório | Alto: a primeira gravação no banco (R3) | HU-02 |
| 4 | HU-04 Ver o mural | N2, N7 | Obrigatório | Médio: legibilidade no celular | HU-03 |
| 5 | HU-05 Marcar o aviso como aberto ou interno | N4 | Importante | Médio: a regra de acesso é conferida em toda leitura | HU-03 |
| 6 | HU-06 Ler aviso aberto sem conta | N3 | Importante | Baixo | HU-05 |
| 7 | HU-07 Arquivar o próprio aviso | N5, N6 | Importante | Médio: a regra de quem arquiva é conferida no servidor | HU-03 |
| 8 | HU-08 Arquivar o aviso vencido de outra pessoa | N12 | Fora desta versão | Baixo | HU-07 |
| 9 | HU-09 Anexar arquivo ao aviso | N9 | Fora desta versão | Alto: armazenamento de arquivo | HU-03 |
| 10 | HU-10 E-mail quando sair aviso novo | N8 | Fora desta versão | Médio: servidor de e-mail | HU-03 |
| 11 | HU-11 Aviso para uma turma | N10 | Fora desta versão | Médio: cadastro de turmas | HU-05 |
| 12 | HU-12 Entrar com a conta institucional | N11 | Fora desta versão | Alto: integração com sistema externo | — |

Ana ordenou o backlog, como diz o `PROCESSO.md`, com os três passos do capítulo
5: classificação em MoSCoW, ordem por risco técnico dentro de cada grupo e
ajuste por dependência.

- **Obrigatórios:** são as quatro histórias da fatia do produto mínimo viável
  do `DESCOBERTA.md`. A ordem por dependência coincide com a ordem por risco: as
  três primeiras atravessam contas de usuário e banco, que é o que a equipe
  menos conhece (R3), e saem na frente para o problema aparecer cedo.
- **Importantes:** são as necessidades que o `DESCOBERTA.md` prevê até a review
  final (N3 a N6). HU-05 vem antes de HU-06 por dependência, porque sem o tipo
  aberto não há aviso para o visitante ler. As duas resolvem C1 juntas. HU-07
  não depende delas e pode trocar de lugar com o par; a review parcial decide.
- **Fora desta versão:** cada item continua registrado, com o motivo.
  - HU-08: a coordenação decidiu que só o autor arquiva (D2).
  - HU-09: uma fonte só, e o comunicado com anexo continua no e-mail (D2).
  - HU-10: uma fonte só, e depende de servidor de e-mail.
  - HU-11: uma fonte só, e exigiria cadastrar as turmas.
  - HU-12: depende de autorização de terceiro (R2).

### Esforço até a review parcial

A estimativa é grossa, em horas, e será refinada no `ITERACOES.md` do capítulo
8. A equipe combinou 5 horas por semana por pessoa fora da aula. Antes da review
parcial há uma iteração de código, a 3 (encontros 7 a 9): 5 pessoas, 5 horas,
2 semanas, 50 horas.

| Item | Estimativa |
|---|---:|
| HU-01 Criar conta | 6 h |
| HU-02 Entrar e sair | 4 h |
| HU-03 Publicar aviso curto | 10 h |
| HU-04 Ver o mural | 8 h |
| **Obrigatórios** | **28 h, 56% de 50 h** |

As 22 horas que sobram absorvem o aprendizado de Django (R3) e o que a equipe
não previu. Os importantes ficam para as iterações 4 a 6, depois da review
parcial.

## Histórias de usuário e critérios de aceitação

### HU-01 Criar conta

Como pessoa do curso, seja aluno, professor ou servidor,
quero criar uma conta no próprio Mini Mural,
para publicar avisos com o meu nome e ler os avisos internos.

[Origem: N1, N4, N7; RE-01]

### HU-02 Entrar e sair

Como pessoa com conta,
quero entrar com o meu nome de usuário e a minha senha, e sair quando terminar,
para que só eu publique com o meu nome.

[Origem: N7, E2]

### HU-03 Publicar aviso curto

Como servidora da secretaria (persona Paula),
quero publicar um aviso curto direto no mural,
para que a turma saiba da troca de sala sem depender do repasse por e-mail e
pelo representante.

[Origem: N1 e N7, confirmadas em E1, E2 e E3; cenário atual, passos 1 a 3]

### HU-04 Ver o mural

Como aluna (persona Lívia),
quero ver pelo celular os avisos publicados, os mais recentes primeiro, com
autor, data e hora,
para saber o que vale agora sem perguntar no balcão.

[Origem: N2 e N7, confirmadas em E4, E5 e O1]

### HU-05 Marcar o aviso como aberto ou interno

Como professor,
quero marcar, ao publicar, se o aviso é aberto ou interno, com interno como
padrão,
para que só quem é do curso leia o aviso interno.

[Origem: N4, E1, E2; C1]

### HU-06 Ler aviso aberto sem conta

Como visitante, ou aluno que não quer criar conta,
quero ler os avisos abertos sem entrar,
para saber dos eventos do centro acadêmico sem criar mais uma conta.

[Origem: N3, E3, E4; C1]

### HU-07 Arquivar o próprio aviso

Como professor,
quero arquivar o aviso que publiquei quando ele deixar de valer,
para que o aluno não confunda o aviso velho com o que vale.

[Origem: N5 e N6, E2, O1; RN-02]

### Fora desta versão

- **HU-08 Arquivar o aviso vencido de outra pessoa.** Como servidora da
  secretaria, quero arquivar o aviso vencido de outra pessoa, para que o mural
  fique sem aviso vencido mesmo quando o autor esquece. [Origem: N12, E1, O1]
- **HU-09 Anexar arquivo ao aviso.** Como servidora da secretaria, quero anexar
  o edital em PDF ao aviso, para não mandar o mesmo aviso também por e-mail.
  [Origem: N9, E1]
- **HU-10 E-mail quando sair aviso novo.** Como aluno, quero receber um e-mail
  quando sair aviso novo, para não abrir o mural só para saber se há novidade.
  [Origem: N8, E4]
- **HU-11 Aviso para uma turma.** Como professor, quero restringir o aviso a uma
  turma, para não avisar o curso inteiro do que vale para uma turma só.
  [Origem: N10, E2]
- **HU-12 Entrar com a conta institucional.** Como aluno, quero entrar com a
  conta institucional, para não criar mais uma conta. [Origem: N11, E1, E4]

## Caso de uso

Preenchido na issue #38.

## Requisitos não funcionais

Preenchidos na issue #37.

## Restrições e regras de negócio

Preenchidas na issue #37.

## Rastreabilidade

Preenchida na issue #36.

## Lista de verificação da revisão

Para cada história:

- [ ] Tem origem declarada, e a origem existe no `DESCOBERTA.md`.
- [ ] O benefício declarado nomeia quem se beneficia.
- [ ] Tem critério para o caminho principal, para a recusa e para o efeito que
      persiste.
- [ ] Nenhum critério descreve a tela em vez do comportamento.
- [ ] Cabe em uma iteração, na avaliação de quem vai construir.

Para o conjunto:

- [ ] Nenhum par de requisitos se contradiz, e todo termo do domínio usado está
      no glossário.
- [ ] As nove características da ISO/IEC 25010 foram percorridas.
- [ ] Toda necessidade confirmada do `DESCOBERTA.md` tem item correspondente, ou
      motivo registrado para ficar de fora.
- [ ] Todo item tem posição na ordem, com critério declarado, e o que ficou fora
      desta versão continua registrado, com motivo.
- [ ] Os itens obrigatórios não passam de 60% do esforço previsto até a review
      parcial.

## Validações realizadas

Preenchidas na issue #40.

## Histórico de revisão

- 2026-10-24: esqueleto e glossário (#33).
- 2026-10-24: backlog ordenado e histórias de usuário (#35).
