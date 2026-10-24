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

**Critérios de aceitação**

- **CA-01.1 Conta criada.** Dado que não existe conta com o nome de usuário
  "livia.m", quando a pessoa cria a conta com esse nome e uma senha de 12
  caracteres, então o sistema cria a conta e a pessoa já fica dentro dela.
- **CA-01.2 Nome em uso.** Dado que já existe a conta "livia.m", quando outra
  pessoa tenta criar a conta "Livia.M", então o sistema recusa, informa que o
  nome já está em uso e mantém o que ela preencheu, menos a senha.
- **CA-01.3 Senha fraca.** Dado que a pessoa está criando uma conta, quando ela
  escolhe a senha "1234567", com 7 caracteres, ou "12345678", só com números,
  então o sistema recusa e informa a regra: pelo menos 8 caracteres, e não só
  números.
- **CA-01.4 A conta continua.** Dado que a pessoa criou a conta "livia.m" e
  saiu, quando ela entra no dia seguinte com o mesmo nome e a mesma senha,
  então o sistema a reconhece.

### HU-02 Entrar e sair

Como pessoa com conta,
quero entrar com o meu nome de usuário e a minha senha, e sair quando terminar,
para que só eu publique com o meu nome.

[Origem: N7, E2]

**Critérios de aceitação**

- **CA-02.1 Entrar.** Dado que existe a conta "paula.sec", quando ela entra com
  o nome e a senha certos, então o sistema a leva ao mural e mostra quem
  entrou.
- **CA-02.2 Senha errada.** Dado que existe a conta "paula.sec", quando alguém
  tenta entrar com a senha errada, então o sistema recusa e informa que nome ou
  senha não conferem, sem dizer qual dos dois.
- **CA-02.3 Mural sem conta.** Dado que a pessoa não entrou, quando ela abre o
  endereço do mural, então o sistema a leva à tela de entrar e, depois que ela
  entra, de volta ao mural.
- **CA-02.4 Depois de sair.** Dado que a pessoa entrou e depois saiu, quando ela
  tenta publicar pela mesma aba do navegador, então o sistema pede que ela
  entre de novo, e nada é publicado.

### HU-03 Publicar aviso curto

Como servidora da secretaria (persona Paula),
quero publicar um aviso curto direto no mural,
para que a turma saiba da troca de sala sem depender do repasse por e-mail e
pelo representante.

[Origem: N1 e N7, confirmadas em E1, E2 e E3; cenário atual, passos 1 a 3]

**Critérios de aceitação**

- **CA-03.1 Publicar.** Dado que Paula entrou com a conta "paula.sec", quando
  ela publica "A aula de Engenharia de Software de amanhã muda para a sala 12
  do bloco B.", então o aviso aparece no topo do mural, com o autor, a data e
  a hora da publicação.
- **CA-03.2 Texto vazio.** Dado que Paula entrou, quando ela publica um texto
  vazio ou só com espaços e quebras de linha, então o sistema recusa, informa
  que o aviso precisa de texto e não publica nada.
- **CA-03.3 Acima do limite.** Dado que Paula entrou, quando ela publica um
  texto de 281 caracteres, então o sistema recusa, informa o limite de 280 e
  quantos caracteres passaram, e mantém o texto para ela cortar.
- **CA-03.4 No limite, com acento.** Dado que Paula entrou, quando ela publica
  um texto de 280 caracteres, todos acentuados, então o aviso é publicado. O
  limite conta caracteres, e não bytes.
- **CA-03.5 O aviso continua.** Dado que Paula publicou um aviso às 10h15,
  quando outra pessoa com conta abre o mural no dia seguinte, então o aviso
  continua lá, com o mesmo texto, autor, data e hora.

### HU-04 Ver o mural

Como aluna (persona Lívia),
quero ver pelo celular os avisos publicados, os mais recentes primeiro, com
autor, data e hora,
para saber o que vale agora sem perguntar no balcão.

[Origem: N2 e N7, confirmadas em E4, E5 e O1]

**Critérios de aceitação**

- **CA-04.1 Ordem do mural.** Dado que há três avisos publicados às 8h, às 9h
  e às 10h do mesmo dia, quando Lívia abre o mural, então os três aparecem na
  ordem 10h, 9h, 8h, cada um com autor, data e hora.
- **CA-04.2 Mural vazio.** Dado que nenhum aviso foi publicado, quando Lívia
  abre o mural, então o sistema informa que ainda não há avisos.
- **CA-04.3 Hora local.** Dado que um aviso foi publicado às 14h02 no horário
  de Palmas (UTC-3), quando Lívia abre o mural em qualquer dia depois, então a
  hora mostrada é 14h02, e não a hora de outro fuso.

Os critérios das histórias importantes, HU-05 a HU-07, são escritos no
planejamento da iteração em que elas entram, no capítulo 8.

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

A equipe percorreu as nove características de qualidade da ISO/IEC 25010. Valor
sem fonte está marcado como valor da equipe e é conferido na validação indicada.

| Característica | Exigência nesta versão |
|---|---|
| Adequação funcional | Coberta pelas histórias e pelos critérios de aceitação |
| Eficiência de desempenho | RNF-01 |
| Compatibilidade | Sem exigência: o Mini Mural não troca dados com outro sistema, e o e-mail e a conta institucional estão fora desta versão (HU-10, HU-12) |
| Capacidade de interação | RNF-02 |
| Confiabilidade | RNF-03 |
| Segurança | RNF-04, RNF-05, RNF-06 |
| Manutenibilidade | RNF-07 |
| Flexibilidade | RNF-08 |
| Segurança física e de operação | Sem exigência: o mural não controla equipamento nem decide sobre pessoas, e uma falha atrasa um aviso, como acontece hoje |

### RNF-01 Tempo de apresentação do mural

- **Grandeza:** tempo entre pedir o mural e vê-lo completo no navegador.
- **Condição:** 200 avisos publicados, um semestre na estimativa da equipe, e
  celular em rede móvel, que é o uso descrito em E4 e E5.
- **Aceitável:** até 3 segundos.
- **Pretendido:** até 1 segundo.
- **Como verificar:** base de teste com 200 avisos, ferramentas do navegador
  com a rede limitada ao perfil "Fast 4G", três execuções; vale o maior valor.
- **Valor:** da equipe, conferido na review parcial.

### RNF-02 Publicar sem ajuda

- **Grandeza:** tempo que uma pessoa que nunca usou o Mini Mural leva para
  publicar um aviso, contado a partir do mural, com a conta já aberta.
- **Condição:** pessoa do perfil da persona Paula ou professor, sem explicação
  da tela.
- **Aceitável:** até 2 minutos, sem pedir ajuda.
- **Como verificar:** cronometragem por quem observa, na sessão de validação
  com o protótipo e, depois, na demonstração do encontro 9.
- **Valor:** da equipe.

### RNF-03 Recarregar a página não publica de novo

- **Grandeza:** avisos gravados para cada publicação confirmada.
- **Condição:** a pessoa recarrega a página logo depois de publicar, como
  acontece no celular quando a rede oscila.
- **Aceitável:** exatamente um aviso.
- **Como verificar:** publicar, recarregar a página três vezes e contar no banco
  os avisos com aquele texto.

### RNF-04 Senha guardada de forma irrecuperável

- **Grandeza:** senhas que podem ser lidas no banco.
- **Condição:** qualquer conta criada pelo sistema.
- **Aceitável:** nenhuma. O banco guarda só um valor derivado da senha, do qual
  a senha não pode ser recuperada.
- **Como verificar:** criar uma conta com senha conhecida e procurar essa senha
  na tabela de contas.

### RNF-05 Texto do aviso mostrado como texto

- **Grandeza:** marcação do aviso interpretada pelo navegador.
- **Condição:** aviso que contém marcação, como `<script>alert(1)</script>`.
- **Aceitável:** nenhuma. O mural mostra os caracteres como foram escritos.
- **Como verificar:** publicar o aviso e conferir a tela e o console do
  navegador.

### RNF-06 Aviso interno fora do alcance de quem não entrou

- **Grandeza:** respostas a pedidos sem conta que contêm o texto de um aviso
  interno.
- **Condição:** pedido sem sessão ao mural e ao endereço direto de um aviso
  interno. Vale a partir de HU-05.
- **Aceitável:** nenhuma.
- **Como verificar:** pedido com `curl`, sem cookie de sessão, e busca do texto
  do aviso na resposta.

### RNF-07 Regras de acesso em um lugar só

- **Grandeza:** lugares do código que decidem quem publica (RN-01), quem lê o
  aviso interno e quem arquiva (RN-02).
- **Condição:** mudança em qualquer uma dessas regras. RN-01 vale até a
  demonstração do encontro 9, e a coordenação vai revê-la (D2).
- **Aceitável:** cada regra decidida em um lugar só, com teste automatizado.
- **Como verificar:** revisão de código com a lista do capítulo 10 e a suíte
  automatizada do capítulo 12.

### RNF-08 Legível no celular

- **Grandeza:** rolagem horizontal e tamanho do texto do aviso.
- **Condição:** tela de 360 pixels de largura, nas telas do mural, de publicar,
  de entrar e de criar conta. A leitura pelo celular vem de E4, E5 e O1.
- **Aceitável:** nenhuma rolagem horizontal, e texto do aviso com pelo menos
  16 pixels.
- **Como verificar:** modo de dispositivo das ferramentas do navegador, em
  360 por 640 pixels.
- **Valor:** da equipe; 360 pixels é a largura dos celulares de entrada.

## Restrições e regras de negócio

As restrições e as regras de negócio vêm de fora da equipe, e só quem as
definiu pode mudá-las.

- **RE-01** O Mini Mural deve usar contas próprias, criadas nele mesmo. A conta
  institucional fica fora desta versão. [Origem: R2, N11]
- **RE-02** O cadastro deve pedir só o necessário para entrar e publicar: nome
  de usuário e senha. [Origem: LGPD, Lei n.º 13.709, de 2018, art. 6.º, III,
  princípio da necessidade]
- **RE-03** O sistema deve estar em uso na demonstração do encontro 9 e
  completo na review final do encontro 16. [Origem: plano da disciplina;
  `PROCESSO.md`]
- **RN-01** Qualquer pessoa com conta pode publicar aviso, e todo aviso mostra
  o autor. [Origem: D2, posição da coordenação sobre C2, válida até a
  demonstração do encontro 9]
- **RN-02** Só o autor pode arquivar o próprio aviso. [Origem: D2, decisão da
  coordenação sobre C3]

## Rastreabilidade

A cadeia vai da fonte ao teste. A coluna de teste é preenchida nos capítulos 11
e 12; até lá, cada critério é o caso de teste escrito em português.

| Fonte | Necessidade | História | Critérios | Teste |
|---|---|---|---|---|
| E1, E2, E3 | N1 | HU-01, HU-03, RN-01 | CA-01.1 a CA-01.4, CA-03.1 a CA-03.5 | A escrever |
| E4, E5, O1 | N2 | HU-04 | CA-04.1 a CA-04.3 | A escrever |
| E3, E4 | N3 | HU-06 | No planejamento da iteração | A escrever |
| E1, E2 | N4 | HU-01, HU-05 | CA-01.1 a CA-01.4; HU-05 no planejamento | A escrever |
| E1, E2, E4, O1 | N5 | HU-07 | No planejamento da iteração | A escrever |
| E2, D2 | N6 | HU-07, RN-02 | No planejamento da iteração | A escrever |
| E2, E5, O1 | N7 | HU-02, HU-03, HU-04 | CA-02.1 a CA-02.4, CA-03.1, CA-04.1 | A escrever |
| E4 | N8 | HU-10 | Fora desta versão | — |
| E1 | N9 | HU-09 | Fora desta versão | — |
| E2 | N10 | HU-11 | Fora desta versão | — |
| E1, E4 | N11 | HU-12 | Fora desta versão | — |
| E1, O1 | N12 | HU-08 | Fora desta versão | — |

Para avaliar o impacto de uma mudança, leia a tabela a partir da linha da
necessidade que mudou: as histórias e os critérios da mesma linha são o que
precisa ser revisto.

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
- 2026-10-24: critérios de aceitação das histórias obrigatórias e rastreabilidade (#36).
- 2026-10-24: requisitos não funcionais, restrições e regras de negócio (#37).
