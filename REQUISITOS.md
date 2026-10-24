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
| Autor | A conta que publicou o aviso. O mural mostra o nome para exibição dessa conta, seguido do nome de usuário | N7, E2, E5, V1, R9 |
| Aviso | Mensagem de texto publicada no mural, com autor, data e hora de publicação | N1, E1, E2 |
| Aviso aberto | Aviso que qualquer pessoa lê, com conta ou sem conta | N3, C1 |
| Aviso arquivado | Aviso que saiu do mural e continua guardado, com a data e a hora em que foi arquivado. Só o autor o consulta (CA-07.4) | N5, O1, E4 |
| Aviso curto | Aviso de até 500 caracteres, contados depois de tirar os espaços das pontas. O valor é da equipe; era 280 e mudou na V1, quando o aviso de um evento precisou de 341 | N1, V1 |
| Aviso interno | Aviso que só quem entrou com uma conta lê. É o tipo padrão ao publicar. Ter conta não comprova ser do curso: o cadastro é aberto (RE-01), e conferir o vínculo dependeria da conta institucional (HU-12) | N4, C1, R8 |
| Aviso publicado | Aviso que está no mural. Todo aviso nasce publicado | N1 |
| Aviso vencido | Aviso cujo assunto já passou, como evento realizado ou prazo encerrado, e que continua no mural | O1, D1 |
| Avisos que valem agora | Nesta versão, os avisos publicados. O sistema não conhece a data em que o assunto de um aviso passa, e quem tira o aviso vencido do mural é o autor | N2, E4, D2 |
| Comunicado oficial | Aviso com edital anexo ou com prazo da coordenação. Continua no e-mail institucional, fora do mural | D2 |
| Conta | Nome de usuário, nome para exibição e senha criados no próprio Mini Mural. Não é a conta institucional da universidade | N11, R2 |
| Data de validade | Data, informada por quem publica, até a qual o assunto do aviso vale. Nesta versão, ela só é mostrada; o aviso continua no mural depois dela (HU-13) | N13, O1, V1 |
| Mural | A lista dos avisos publicados, os mais recentes primeiro | N2, D1 |
| Nome para exibição | Nome que a pessoa escolhe ao criar a conta e que o mural mostra como autor, como "Secretaria do curso". Não repete o de outra conta, sem diferenciar maiúsculas | N7, V1, R9 |
| Visitante | Pessoa que lê o mural sem entrar com uma conta | N3 |

## Backlog ordenado

| Ordem | Item | Origem | MoSCoW | Risco técnico | Depende de |
|---:|---|---|---|---|---|
| 1 | HU-01 Criar conta | N1, N4, N7 | Obrigatório | Alto: contas de usuário em Django, que ninguém na equipe conhece (R3) | Nenhuma |
| 2 | HU-02 Entrar e sair | N7 | Obrigatório | Alto: sessão e senha, pela mesma razão | HU-01 |
| 3 | HU-03 Publicar aviso curto | N1, N7 | Obrigatório | Alto: a primeira gravação no banco (R3) | HU-02 |
| 4 | HU-04 Ver o mural | N2, N7 | Obrigatório | Médio: legibilidade no celular | HU-03 |
| 5 | HU-05 Marcar o aviso como aberto ou interno | N4 | Importante | Médio: a regra de acesso é conferida em toda leitura | HU-03 |
| 6 | HU-06 Ler aviso aberto sem conta | N3 | Importante | Baixo | HU-05 |
| 7 | HU-07 Arquivar o próprio aviso | N5, N6 | Importante | Médio: a regra de quem arquiva é conferida no servidor | HU-03 |
| 8 | HU-13 Informar até quando o aviso vale | N13 | Desejável | Baixo | HU-03 |
| 9 | HU-08 Arquivar o aviso vencido de outra pessoa | N12 | Fora desta versão | Baixo | HU-07 |
| 10 | HU-09 Anexar arquivo ao aviso | N9 | Fora desta versão | Alto: armazenamento de arquivo | HU-03 |
| 11 | HU-10 E-mail quando sair aviso novo | N8 | Fora desta versão | Médio: servidor de e-mail | HU-03 |
| 12 | HU-11 Aviso para uma turma | N10 | Fora desta versão | Médio: cadastro de turmas | HU-05 |
| 13 | HU-12 Entrar com a conta institucional | N11 | Fora desta versão | Alto: integração com sistema externo | Nenhuma |
| 14 | HU-14 Saber quem viu o aviso | N14 | Fora desta versão | Médio: registro de leitura por conta | HU-04 |
| 15 | HU-15 Corrigir o próprio aviso depois de publicado | N15 | Fora desta versão | Baixo | HU-03 |

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
- **Desejável:** HU-13 entrou pela validação V1. Fica depois dos importantes
  porque mostrar a data não tira o aviso vencido do mural; ela só ajuda o aluno
  a reconhecê-lo.
- **Fora desta versão:** cada item continua registrado, com o motivo.
  - HU-08: a coordenação decidiu que só o autor arquiva (D2).
  - HU-09: uma fonte só, e o comunicado com anexo continua no e-mail (D2).
  - HU-10: uma fonte só, e depende de servidor de e-mail.
  - HU-11: uma fonte só, e exigiria cadastrar as turmas.
  - HU-12: depende de autorização de terceiro (R2).
  - HU-14: exige registrar o que cada conta leu, o que muda o modelo de dados e
    trata um dado pessoal que RE-02 manda evitar sem necessidade. Volta na
    review parcial, com a coordenação.
  - HU-15: uma fonte só (E2); enquanto não houver correção, quem errou
    arquiva o aviso e publica outro.

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
parcial, e o desejável HU-13 vem depois deles. As mudanças da V1 em HU-01 e
HU-04 cabem nas estimativas: são um campo a mais no cadastro e no mural. A
mudança do #53 acrescenta um critério a HU-01 e o nome de usuário ao mural, e
também cabe: as estimativas continuam as mesmas, e os obrigatórios ficam em
56%.

## Histórias de usuário e critérios de aceitação

### HU-01 Criar conta

Como pessoa do curso, seja aluno, professor ou servidor,
quero criar uma conta no próprio Mini Mural, com um nome para exibição,
para publicar avisos com um nome que os alunos reconheçam e ler os avisos
internos.

[Origem: N1, N4, N7; RE-01]

**Critérios de aceitação**

- **CA-01.1 Conta criada (alterado na V1).** Dado que não existe conta com o
  nome de usuário "livia.m", quando a pessoa cria a conta com esse nome, o nome
  para exibição "Lívia Martins" e uma senha de 12 caracteres, então o sistema
  cria a conta e a pessoa já entra com ela.
- **CA-01.2 Nome em uso.** Dado que já existe a conta "livia.m", quando outra
  pessoa tenta criar a conta "Livia.M", então o sistema recusa, informa que o
  nome já está em uso e mantém o que ela preencheu, menos a senha.
- **CA-01.3 Senha fraca.** Dado que a pessoa está criando uma conta, quando ela
  escolhe a senha "1234567", com 7 caracteres, ou "12345678", só com números,
  então o sistema recusa e informa a regra: pelo menos 8 caracteres, com algo
  além de números.
- **CA-01.4 A conta continua.** Dado que a pessoa criou a conta "livia.m" e
  saiu, quando ela entra no dia seguinte com o mesmo nome e a mesma senha,
  então o sistema a reconhece.
- **CA-01.5 Nome para exibição obrigatório (acrescentado na V1).** Dado que a
  pessoa está criando uma conta, quando ela deixa o nome para exibição vazio,
  então o sistema recusa e informa que o nome aparece como autor dos avisos.
- **CA-01.6 Nome para exibição em uso (acrescentado no #53, alterado no #63).**
  Dado que já existe uma conta com o nome para exibição "Secretaria do curso",
  quando outra pessoa tenta criar uma conta com "secretaria  do curso ", com
  espaço repetido e espaço no fim, então o sistema recusa e informa que esse
  nome já está em uso. A comparação tira os espaços das pontas, junta os
  repetidos e não diferencia maiúsculas.

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
- **CA-03.3 Acima do limite (alterado na V1).** Dado que Paula entrou, quando
  ela publica um texto de 501 caracteres, então o sistema recusa, informa o
  limite de 500 e quantos caracteres passaram, e mantém o texto para ela
  cortar.
- **CA-03.4 No limite, com acento (alterado na V1).** Dado que Paula entrou,
  quando ela publica um texto de 500 caracteres, todos acentuados, então o
  aviso é publicado. O limite conta caracteres, e um caractere acentuado vale
  um.
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

- **CA-04.1 Ordem do mural (alterado na V1 e no #53).** Dado que há três avisos publicados às 8h, às 9h
  e às 10h do mesmo dia, quando Lívia abre o mural, então os três aparecem na
  ordem 10h, 9h, 8h, cada um com o nome para exibição e o nome de usuário do
  autor, a data e a hora.
- **CA-04.2 Mural vazio.** Dado que nenhum aviso foi publicado, quando Lívia
  abre o mural, então o sistema informa que ainda não há avisos.
- **CA-04.3 Hora local.** Dado que um aviso foi publicado às 14h02 no horário
  de Palmas (UTC-3), quando Lívia abre o mural em qualquer dia depois, então a
  hora mostrada é 14h02.

Mostrar o nome de usuário no mural expõe a quem lê um dado a mais da conta. A
equipe aceita a exposição porque o nome é escolhido pela própria pessoa ao
criar a conta, já está entre os dados que RE-02 considera necessários, e é o
que distingue duas contas com nomes para exibição parecidos (R9).

O efeito que persiste em HU-04 é o de CA-03.5, visto do lado de quem lê. Ver o
mural não muda nada no sistema, e por isso a história não tem critério próprio
desse tipo.

Os critérios de HU-05 e HU-06 são escritos no planejamento da iteração em que
elas entram, no capítulo 8. HU-07 ganhou critérios antes, no #57, porque o
diagrama de estados do `PROJETO.md` exige um critério para cada transição.

### HU-05 Marcar o aviso como aberto ou interno

Como professor,
quero marcar, ao publicar, se o aviso é aberto ou interno, com interno como
padrão,
para que o aviso interno só seja lido por quem entrou com uma conta.

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

**Critérios de aceitação (acrescentados no #57)**

- **CA-07.1 Arquivar o próprio aviso.** Dado que "prof.calculo" publicou um
  aviso, quando ele o arquiva, então o aviso sai do mural, e o sistema registra
  a data e a hora do arquivamento.
- **CA-07.2 Aviso de outra pessoa.** Dado que "paula.sec" publicou um aviso,
  quando "prof.calculo" tenta arquivá-lo, então o sistema recusa, informa que
  só o autor arquiva, e o aviso continua no mural.
- **CA-07.3 Arquivar de novo.** Dado que o autor arquivou um aviso às 10h,
  quando ele pede para arquivá-lo outra vez às 11h, então nada muda, e a data
  registrada continua 10h.
- **CA-07.4 Quem vê o arquivado.** Dado que "paula.sec" arquivou um aviso,
  quando outra pessoa com conta pede o endereço desse aviso, então o sistema
  responde como se ele não existisse; quando "paula.sec" pede o mesmo
  endereço, então vê o aviso, com a data do arquivamento.

O arquivamento não se desfaz nesta versão: quem arquivou por engano publica o
aviso de novo. Nenhuma fonte pediu para desfazer, e mostrar o arquivado a
outras pessoas traria de volta o aviso velho que O1 e E4 descrevem. As duas
decisões são da equipe e vão à demonstração do encontro 9.

### HU-13 Informar até quando o aviso vale

Como servidora da secretaria (persona Paula),
quero informar, ao publicar, a data até a qual o aviso vale,
para que o aluno reconheça o aviso vencido sem perguntar no balcão.

[Origem: N13, O1, V1]

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
- **HU-14 Saber quem viu o aviso.** Como professor, quero saber quantas
  pessoas da turma viram o meu aviso, para avisar de outro jeito quem não viu.
  [Origem: N14, E1, E2, V1]

## Caso de uso

O caso de uso cobre o fluxo principal do sistema, publicar aviso, que é onde as
exceções se concentram. As histórias dizem quem quer o quê; o caso de uso diz o
que acontece quando o caminho normal não acontece.

### UC-01 Publicar aviso

- **Ator principal:** pessoa com conta (RN-01). Nas fontes, quem publica é a
  secretaria, o professor e o centro acadêmico.
- **Pré-condição:** a pessoa entrou com a conta (HU-02).
- **Garantia de sucesso:** o aviso fica registrado, com o texto, o autor, a
  data e a hora, e aparece no topo do mural.

**Fluxo principal**

1. A pessoa abre o mural e escolhe publicar um aviso.
2. O sistema apresenta o campo do aviso, com o limite de caracteres. A partir de
   HU-05, apresenta também a escolha entre aberto e interno, com interno
   marcado.
3. A pessoa escreve o aviso e confirma.
4. O sistema confere o texto, registra o aviso com autor, data e hora e
   apresenta o mural com o aviso no topo. [CA-03.1]

**Fluxos alternativos**

- **1a. A pessoa não entrou:** o sistema a leva à tela de entrar e, depois que
  ela entra, de volta ao mural. [CA-02.3]
- **4a. Texto vazio ou só com espaços:** o sistema recusa, informa que o aviso
  precisa de texto e não registra nada. [CA-03.2]
- **4b. Texto acima do limite:** o sistema recusa, informa o limite e quantos
  caracteres passaram, e mantém o texto para a pessoa cortar. [CA-03.3]
- **4c. A pessoa saiu da conta em outra aba entre os passos 1 e 3:** o sistema
  não registra o aviso e pede que ela entre de novo. [CA-02.4]
- **4d. A pessoa recarrega a página depois do passo 4:** o sistema não registra
  o aviso outra vez. [RNF-03]
- **4e. O banco não responde no passo 4:** o sistema informa que o aviso não foi
  publicado e nada fica registrado pela metade. Esta alternativa apareceu ao
  percorrer o fluxo e ainda não tem critério; ela entra nos casos de teste do
  capítulo 11.

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
- **Condição:** a pessoa recarrega a página logo depois de publicar. Nenhuma
  fonte descreveu esse gesto; a equipe o considera porque todo navegador o
  oferece.
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
  de usuário, nome para exibição e senha. [Origem: LGPD, Lei n.º 13.709, de 2018, art. 6.º, III,
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
| E1, E2, E3 | N1 | HU-01, HU-03, RN-01 | CA-01.1 a CA-01.6, CA-03.1 a CA-03.5 | A escrever |
| E4, E5, O1 | N2 | HU-04 | CA-04.1 a CA-04.3 | A escrever |
| E3, E4 | N3 | HU-06 | No planejamento da iteração | A escrever |
| E1, E2 | N4 | HU-01, HU-05 | CA-01.1 a CA-01.6; HU-05 no planejamento | A escrever |
| E1, E2, E4, O1 | N5 | HU-07 | CA-07.1, CA-07.3, CA-07.4 | A escrever |
| E2, D2 | N6 | HU-07, RN-02 | CA-07.2 | A escrever |
| E2, E5, O1 | N7 | HU-01, HU-02, HU-03, HU-04 | CA-01.6, CA-02.1 a CA-02.4, CA-03.1, CA-04.1 | A escrever |
| E4 | N8 | HU-10 | Fora desta versão | Não se aplica |
| E1 | N9 | HU-09 | Fora desta versão | Não se aplica |
| E2 | N10 | HU-11 | Fora desta versão | Não se aplica |
| E1, E4 | N11 | HU-12 | Fora desta versão | Não se aplica |
| E1, O1 | N12 | HU-08 | Fora desta versão | Não se aplica |
| O1, V1 | N13 | HU-13 | No planejamento da iteração | A escrever |
| E1, E2, V1 | N14 | HU-14 | Fora desta versão | Não se aplica |
| E2 | N15 | HU-15 | Fora desta versão | Não se aplica |

Para avaliar o impacto de uma mudança, leia a tabela a partir da linha da
necessidade que mudou: as histórias e os critérios da mesma linha são o que
precisa ser revisto.

## Lista de verificação da revisão

Revisão de 2026-10-24, por Eva e Carla, registrada na #39. Os achados 1, 2, 3
e 5 mudaram o documento; o 4 ficou como está, com o motivo escrito em HU-04.

Para cada história:

- [x] Tem origem declarada, e a origem existe no `DESCOBERTA.md`.
- [x] O benefício declarado nomeia quem se beneficia.
- [x] Tem critério para o caminho principal, para a recusa e para o efeito que
      persiste.
- [x] Nenhum critério descreve a tela em vez do comportamento.
- [x] Cabe em uma iteração, na avaliação de quem vai construir.

Para o conjunto:

- [x] Nenhum par de requisitos se contradiz, e todo termo do domínio usado está
      no glossário.
- [x] As nove características da ISO/IEC 25010 foram percorridas.
- [x] Toda necessidade confirmada do `DESCOBERTA.md` tem item correspondente, ou
      motivo registrado para ficar de fora.
- [x] Todo item tem posição na ordem, com critério declarado, e o que ficou fora
      desta versão continua registrado, com motivo.
- [x] Os itens obrigatórios não passam de 60% do esforço previsto até a review
      parcial.

## Validações realizadas

### V1, 2026-10-24, com servidora da secretaria (perfil da persona Paula)

Sessão com o [protótipo](validacao/prototipo-mvp.md) do fluxo do MVP,
conduzida por Eva e anotada por Bruno. Registro completo em
[`validacao/V1-secretaria.md`](validacao/V1-secretaria.md).

| Achado | Efeito | Item alterado |
|---|---|---|
| O aviso da palestra, com local, horário e inscrição, teve 341 caracteres | O limite de 280 não cabe no aviso de evento, que é aviso do dia a dia (D2) | Glossário, "aviso curto", e CA-03.3 e CA-03.4, de 280 para 500 |
| Procurou onde dizer que o aviso valia "até quinta" | A data de validade faltava, e o mural de papel já mostrava o custo disso (O1) | N13 no `DESCOBERTA.md`; HU-13 criada, desejável; glossário, "data de validade" |
| Disse que o aluno não reconhece "paula.sec" como a secretaria | O autor precisa de um nome que o aluno reconheça | HU-01, CA-01.1, CA-01.5 acrescentado, CA-04.1, RE-02 e glossário, "autor" e "nome para exibição" |
| Perguntou como saberia se os alunos viram o aviso | E1 e E2 já tinham relatado essa dificuldade, e ela não tinha virado necessidade | N14 no `DESCOBERTA.md`; HU-14 criada, fora desta versão |

A sessão teve uma pessoa só, do lado de quem publica. O lado de quem lê, HU-04,
é validado com aluno na demonstração do encontro 9. A primeira tarefa levou
cerca de 1 minuto e 10 segundos, sem ajuda: dentro do RNF-02, como indício,
porque o protótipo de papel não mede o sistema real.

## Histórico de revisão

- 2026-10-24: esqueleto e glossário (#33).
- 2026-10-24: backlog ordenado e histórias de usuário (#35).
- 2026-10-24: critérios de aceitação das histórias obrigatórias e rastreabilidade (#36).
- 2026-10-24: requisitos não funcionais, restrições e regras de negócio (#37).
- 2026-10-24: caso de uso UC-01, publicar aviso (#38).
- 2026-10-24: achados da revisão com a lista de verificação (#39): HU-05 e o
  glossário alinhados a RE-01, ator do UC-01 alinhado a RN-01, aviso arquivado
  sem promessa de consulta.
- 2026-10-24: validação V1 (#40): limite do aviso de 280 para 500 caracteres,
  nome para exibição, HU-13 e HU-14 criadas.
- 2026-10-24: linha de base do primeiro marco, na tag `v0.4.0` (#42).
- 2026-10-24: primeira mudança depois da linha de base (#53). Motivo: o nome
  para exibição livre, vindo da V1, deixava uma conta publicar com o nome de
  outra pessoa, e o autor visível era a condição da coordenação para C2 (D2).
  Impacto pela rastreabilidade, linhas de N1, N4 e N7: CA-01.6 acrescentado,
  CA-04.1 e glossário alterados, estimativas mantidas. O risco que sobra está
  em R9.
- 2026-10-24: CA-01.6 passa a comparar o nome sem os espaços das pontas e sem
  espaços repetidos (#63). Motivo: a revisão do modelo de dados mostrou que um
  espaço a mais repetia o problema do #53. Impacto: só o CA-01.6.
- 2026-10-24: lacunas do diagrama de estados do aviso (#57). Motivo: a
  transição de publicado para arquivado não tinha critério, o estado arquivado
  não dizia se tinha saída, e uma transição de publicado para publicado, a
  correção do texto, estava em E2 sem ter virado necessidade. Impacto: CA-07.1 a
  CA-07.4 acrescentados, glossário "aviso arquivado" alterado, N15 e HU-15
  registradas, fora desta versão; estimativas dos obrigatórios mantidas.
