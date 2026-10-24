# Arquitetura

Este documento diz onde cada parte do Mini Mural roda e como as partes
conversam. O `PROJETO.md` diz de que o sistema é feito, com nomes que não
dependem de tecnologia; aqui esses nomes ganham lugar. As decisões caras de
desfazer ficam na tabela de decisões, com a alternativa descartada.

## Visão geral

Fonte: [`diagrams/arquitetura.mmd`](diagrams/arquitetura.mmd).

O Mini Mural é uma aplicação só, que monta as páginas no servidor e as entrega
prontas ao navegador (A-01). Dentro da aplicação, as dependências seguem um
sentido: a borda chama o domínio, e o domínio usa a persistência. O domínio não
conhece requisição nem página.

## Responsabilidades

| Parte | Sabe | Faz |
|---|---|---|
| Navegador | Como mostrar a página que recebeu | Mostra as páginas, envia os formulários, guarda o cookie da sessão e ajuda quem digita a errar menos, com o contador de caracteres e os campos obrigatórios |
| Aplicação: borda | Rotas, formulários e modelos de página | Recebe a requisição, descobre quem pede pela sessão, chama o domínio, escolhe o código de status e monta a página |
| Aplicação: domínio | As regras do `REQUISITOS.md` | Conta e Aviso, com as regras de publicar, ler e arquivar (DP-08) |
| Aplicação: persistência | Como cada objeto vira linha | Grava e recupera pelo ORM do framework |
| Banco | Os dados e a integridade estrutural deles | Guarda, recupera e recusa estados impossíveis: nome repetido, texto acima do limite, conta com avisos apagada |

### Os participantes provisórios do `PROJETO.md`

| Participante | Parte | Por quê |
|---|---|---|
| Tela de publicação | Página montada pela borda e mostrada no navegador | Coleta o texto e mostra a recusa; não decide regra (DP-08) |
| Aviso | Domínio, no módulo `avisos`, como classe de modelo | Conhece texto, tipo, situação e autor, como diz a ficha do `PROJETO.md` |
| Conta | Domínio, no módulo `contas`, como classe de modelo | Conhece os nomes e confere a senha |
| Mural | Borda do módulo `avisos`: uma consulta e uma página | Não guarda dado próprio |
| Registro de avisos | Persistência: ORM e PostgreSQL | Grava, recupera e atribui o instante da publicação (DP-10) |

O `PROJETO.md` deixou para este capítulo o mecanismo da sessão (CA-02.1 a
CA-02.4). A sessão é a do framework: o servidor guarda quem entrou, no banco, e
o navegador guarda só um cookie com o identificador. Sair apaga a sessão no
servidor, e por isso o pedido seguinte da mesma aba já chega sem conta
(CA-02.4).

## Onde cada parte roda

Fonte: [`diagrams/implantacao.mmd`](diagrams/implantacao.mmd).

A aplicação roda em um processo, e o banco fica na mesma máquina na primeira
versão. A hospedagem é decidida no capítulo 14, a partir das opções que R4 pede
levantar até o encontro 12.

**Ambiente da demonstração do encontro 9.** O ponto 3 da definição de pronto
pede a funcionalidade acessível no ambiente de demonstração, e RE-03 pede o
sistema em uso no encontro 9. Até haver hospedagem, a demonstração roda no
notebook de um integrante, com a aplicação e o PostgreSQL locais, e quem
publica usa esse notebook ou um celular na mesma rede. Se a rede do câmpus
bloquear o acesso pelo celular, a publicação é feita no notebook. O servidor de
desenvolvimento do framework serve para isso e para o trabalho diário; ele não
é servidor de produção, e o servidor de produção é decidido junto com a
hospedagem.

## Contrato das rotas

Rotas em [`contrato/operacoes.md`](contrato/operacoes.md). Cada passo do UC-01
pede uma rota:

| Rota | Para quê | Origem |
|---|---|---|
| `GET /entrar/`, `POST /entrar/`, `POST /sair/` | Entrar e sair | HU-02 |
| `GET /cadastro/`, `POST /cadastro/` | Criar conta | HU-01 |
| `GET /` | O mural | HU-04, UC-01 passo 1 |
| `GET /avisos/novo/` | A página de publicar | UC-01 passo 2 |
| `POST /avisos/` | Registrar o aviso | HU-03, UC-01 passos 3 e 4 |

As rotas de HU-05 a HU-07 estão em esboço no mesmo arquivo. O caminho nomeia o
recurso com um substantivo do glossário, e o método diz a intenção: `POST
/avisos/` cria um aviso na coleção de avisos.

### Conferência do contrato

Em 2026-10-24, Ana e Eva, que não escreveram o contrato, o leram como quem vai
escrever as páginas, com a pergunta "o que a página faz em cada resposta?". O
registro completo está na #74.

| Achado | Mudança no contrato |
|---|---|
| A alternativa 4c respondia só "302 para `/entrar/`", e a página de entrar não tinha como mostrar a mensagem do protótipo nem para onde voltar | O redirecionamento leva `next` e `motivo`, e a página de entrar mostra a mensagem quando recebe o motivo |
| O cadastro não dizia se mostra uma mensagem ou várias | Cada campo recusado mostra a sua, e mais de uma pode aparecer |
| O protótipo desenha "sair" como ligação, e o contrato só aceita `POST` | O contrato diz que sair é botão de formulário |

## Verificações

O navegador ajuda, o servidor decide, e o banco recusa o que nunca pode
acontecer, venha de onde vier a gravação.

| Verificação | No navegador | No servidor | No banco |
|---|---|---|---|
| Texto vazio | Campo obrigatório, como ajuda | Decide, depois de tirar os espaços das pontas; 422 (CA-03.2) | Não participa |
| Limite de 500 caracteres | Contador e limite do campo, como ajuda; a contagem do navegador pode diferir na quebra de linha | Decide: conta caracteres depois de juntar as quebras de linha; 422 (CA-03.3, CA-03.4) | Restrição de tamanho em caracteres, a segunda barreira (DP-09) |
| Nome de usuário em uso | Não participa | Decide, sem diferenciar maiúsculas; 422 (CA-01.2) | Unicidade por expressão (DP-03) |
| Nome para exibição em uso | Não participa | Normaliza os espaços e decide, sem diferenciar maiúsculas; 422 (CA-01.6) | Unicidade por expressão sobre o nome já normalizado |
| Senha fraca | Não participa | Validadores de senha do framework; 422 (CA-01.3) | Não participa |
| Autor do aviso | Não participa | Vem da sessão, nunca do formulário (A-08) | Chave estrangeira obrigatória |
| Instante da publicação | Não participa | Não aceita instante vindo do formulário | Valor padrão do banco no momento da gravação (DP-10) |
| Quem pode publicar | Não participa | Regra da conta (RN-01, DP-08) | Não participa |
| Quem pode arquivar | Mostra o botão só ao autor, como ajuda | Decide; 403 (CA-07.2, RN-02) | Não participa |
| Quem vê aviso interno ou arquivado | Não participa | Decide em toda rota que mostra aviso; 302 ou 404 (RNF-06, CA-07.4) | Não participa |
| Apagar conta com avisos | Não participa | Nenhuma rota apaga conta | A chave estrangeira recusa (DP-05) |
| Formulário forjado por outro site | Envia a marca de proteção recebida com a página | O framework confere a marca; 403 | Não participa |

A linha do autor é a defesa do sistema contra R9 do lado de dentro: mesmo quem
altera o formulário no navegador não consegue publicar em nome de outra conta.

## Qualidades e custos

| Qualidade | Requisito | Decisão que o sustenta | Custo aceito |
|---|---|---|---|
| Eficiência de desempenho | RNF-01: mural com 200 avisos em até 3 segundos | Uma consulta com junção traz os avisos e os nomes dos autores; índice só depois de medir (DP-07) | A consulta precisa ser escrita pensando na junção; a medição fica para antes do encontro 9 |
| Capacidade de interação | RNF-02: publicar sem ajuda em até 2 minutos | Uma ação por página, mensagens de recusa que dizem o que fazer (contrato) e o contador de caracteres | O contador usa um script pequeno; a página funciona sem ele, e o servidor continua decidindo |
| Confiabilidade | RNF-03: recarregar não publica de novo | Redirecionamento 303 depois de gravar (A-06) | A confirmação precisa estar na página de destino |
| Segurança | RNF-04: senha irrecuperável | O guardador de senhas do framework, com derivação de chave lenta de propósito | Entrar leva uma fração de segundo a mais, por desenho |
| Segurança | RNF-05: texto do aviso mostrado como texto | Escape automático dos modelos de página; nenhum texto de aviso é marcado como seguro | A quebra de linha do aviso usa um filtro que escapa o texto antes de quebrar |
| Segurança | RNF-06: aviso interno fora do alcance de quem não entrou | A regra de quem vê fica no aviso e é chamada por toda rota que mostra aviso | Toda consulta de aviso passa pela regra, inclusive as que parecem inofensivas |
| Manutenibilidade | RNF-07: cada regra de acesso em um lugar | Regras como métodos de conta e aviso (A-03, A-05, DP-08) | O domínio depende do ORM |
| Flexibilidade | RNF-08: legível em 360 pixels | Uma folha de estilo própria, de uma coluna, sem biblioteca de estilos | O estilo é escrito à mão |

Compatibilidade e segurança física e de operação seguem sem exigência, como no
`REQUISITOS.md`.

### O custo escondido do mural

O mural mostra, em cada aviso, os dois nomes do autor. Escrito do jeito mais
direto, o código pede os avisos e depois, para cada aviso, a conta do autor:
com 200 avisos, são 201 idas ao banco por página. A consulta com junção faz uma
ida só e dá o mesmo trabalho de escrever, e por isso entra desde a primeira
versão, sem esperar a medição do RNF-01. O que espera a medição é o índice.

## Decisões

Os identificadores usam o prefixo `A`, de arquitetura; as decisões de projeto do
`PROJETO.md` usam `DP`. A-01 foi a primeira decisão técnica do projeto e, como
pede o `PROCESSO.md`, foi tomada em par, por Davi e Bruno.

| Id | Decisão | Motivo | Consequência aceita | Situação |
|---|---|---|---|---|
| A-01 | Uma aplicação só, que monta as páginas no servidor. Descartados: frontend separado, no navegador, falando com o backend por uma API, que é a forma que o capítulo 7 recomenda; e serviços separados | Ninguém na equipe conhece framework web, contas e banco juntos (R3), e há uma iteração de código antes do encontro 9 (`DESCOBERTA.md`). RNF-08 se atende com página HTML legível no celular, e nenhuma necessidade pede outro cliente além do navegador: o aplicativo instalável está fora de escopo | Tela e regra ficam no mesmo código e na mesma implantação. Sem contrato de API, tela e servidor não avançam em paralelo por respostas de exemplo. Se um aplicativo vier, a API é escrita depois, sobre o mesmo domínio | Aceita, em par: Davi e Bruno |
| A-02 | Django 5.2 LTS, Python 3.12 e PostgreSQL. Descartado: um microframework, com bibliotecas avulsas para contas, formulários e migrações | O framework traz contas com senha guardada de forma irrecuperável (RNF-04), formulários protegidos contra envio forjado, escape automático nas páginas (RNF-05) e migrações. A versão tem suporte até abril de 2028, depois da review final. O PostgreSQL tem transação e unicidade por expressão, que DP-03 pede | A equipe precisa aprender as decisões do framework antes de escrever regra (R3). Trocar de framework depois é reescrever a borda e a persistência | Aceita |
| A-03 | As regras ficam nas classes de modelo do framework, que juntam domínio e persistência. Descartado: classes de domínio separadas do ORM, com um repositório entre elas | O domínio tem duas classes, e uma camada a mais não resolve problema que a equipe tenha hoje (`PROJETO.md`, padrão antes do problema) | O domínio depende do ORM. A regra é testada com objeto não gravado, sem banco | Aceita |
| A-04 | A conta é um modelo de usuário próprio, só com os campos do `PROJETO.md`, criado já no esqueleto. Descartado: o modelo de usuário padrão do framework | O padrão traz e-mail, nome, sobrenome, data de cadastro, último acesso e marcas de equipe, que RE-02 manda não pedir. O framework exige o modelo de usuário definido antes da primeira migração | Sem o painel administrativo do framework nesta versão, porque ele depende das marcas de equipe. A conta só nasce pelo cadastro (HU-01) ou pelo terminal, e desativar uma conta que se passou por outra pessoa (R9) também só se faz pelo terminal, por um integrante | Aceita |
| A-05 | Dois módulos, `contas` e `avisos`; `avisos` depende de `contas`, nunca o contrário. Descartado: um módulo só | A regra de quem publica (RN-01), a que mais deve mudar (R9, D2), fica na conta e muda sem tocar o aviso | O mural, que mostra o autor, junta as duas tabelas pela chave estrangeira | Aceita |
| A-06 | Depois de gravar, a resposta redireciona com 303 para uma página lida com GET. Descartado: responder a página direto ao envio do formulário | RNF-03: recarregar a página não publica de novo | A confirmação precisa estar na página de destino; no mural, o aviso no topo é a confirmação | Aceita |
| A-07 | Formulário recusado responde 422, com a mesma página, a mensagem e o que foi preenchido, menos a senha. Descartado: responder 200 com a mensagem | O código de status diz ao navegador e aos testes que o pedido foi recusado. CA-01.2 e CA-03.3 pedem o preenchimento mantido | Os testes conferem o código, além do texto | Aceita |
| A-08 | O autor vem da sessão, e o instante vem do banco; nenhum dos dois é campo de formulário. Descartado: campo escondido com o autor | Campo de formulário pode ser alterado por quem envia, e o autor visível é a defesa de N7 e de R9. DP-10 já tirou o instante da tela | Publicar exige sessão válida em toda requisição | Aceita |
| A-09 | Migrações do framework desde o esqueleto. Descartado: esquema escrito à mão, fora do framework | O modelo de conta precisa de migração antes de tudo (A-04), e cada mudança de esquema fica no Git, com o código que a pede | Toda mudança de modelo vem com a migração no mesmo pull request. O `ROTEIRO.md` punha migrações no capítulo 14; lá fica a aplicação delas na implantação | Aceita |
| A-10 | Configuração lida de variáveis de ambiente, com valores de desenvolvimento quando a variável falta | A mesma aplicação roda no notebook de cada integrante e, depois, na hospedagem | A chave secreta de desenvolvimento fica no código e não pode ir para a hospedagem; o tratamento de segredos é do capítulo 13 | Aceita para desenvolvimento |
| A-12 | Contrato das rotas em `contrato/operacoes.md`; no lugar dos exemplos JSON, cada resposta diz a página, a mensagem exata e os campos mantidos. Descartados: exemplos JSON, porque não há API (A-01), e combinar rotas só no código | Quem faz a página e quem faz a regra precisam combinar campos, códigos e mensagens antes de escrever, e os testes do capítulo 12 precisam de onde tirar o esperado | Mudar rota, campo ou mensagem passa por pull request que altera o contrato | Aceita |
| A-11 | Hospedagem e servidor de produção | Dependem das opções que R4 levanta | O servidor de desenvolvimento do framework só serve para trabalhar e para a demonstração do encontro 9 | Proposta, a decidir no capítulo 14 |

## Pontos em aberto

- Hospedagem e servidor de produção: capítulo 14, com as opções de R4 (A-11).
- Segredos fora do código, a começar pela chave secreta: capítulo 13 (A-10).
- Respostas de falta de identificação e de permissão, além das já descritas: capítulo 13.

## Histórico de revisão

- 2026-10-24: esqueleto, participantes, responsabilidades e diagramas (#69).
- 2026-10-24: decisões A-01 a A-11 (#70).
- 2026-10-24: contrato das rotas e A-12 (#71).
- 2026-10-24: verificações, qualidades e custos (#72).
- 2026-10-24: conferência do contrato em duplas trocadas (#74).
