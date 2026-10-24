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

Preenchido na issue #71.

## Verificações

Preenchidas na issue #72.

## Qualidades e custos

Preenchidas na issue #72.

## Decisões

Os identificadores usam o prefixo `A`, de arquitetura; as decisões de projeto do
`PROJETO.md` usam `DP`. A-01 foi a primeira decisão técnica do projeto e, como
pede o `PROCESSO.md`, foi tomada em par, por Davi e Bruno.

| Id | Decisão | Motivo | Consequência aceita | Situação |
|---|---|---|---|---|
| A-01 | Uma aplicação só, que monta as páginas no servidor. Descartados: frontend separado, no navegador, falando com o backend por uma API, que é a forma que o capítulo 7 recomenda; e serviços separados | Ninguém na equipe conhece framework web, contas e banco juntos (R3), e há uma iteração de código antes do encontro 9 (`DESCOBERTA.md`). RNF-08 se atende com página HTML legível no celular, e nenhuma necessidade pede outro cliente além do navegador: o aplicativo instalável está fora de escopo | Tela e regra ficam no mesmo código e na mesma implantação. Sem contrato de API, tela e servidor não avançam em paralelo por respostas de exemplo. Se um aplicativo vier, a API é escrita depois, sobre o mesmo domínio | Aceita, em par: Davi e Bruno |
| A-02 | Django 5.2 LTS, Python 3.12 e PostgreSQL. Descartado: um microframework, com bibliotecas avulsas para contas, formulários e migrações | O framework traz contas com senha guardada de forma irrecuperável (RNF-04), formulários protegidos contra envio forjado, escape automático nas páginas (RNF-05) e migrações. A versão tem suporte até abril de 2028, depois da review final. O PostgreSQL tem transação e unicidade por expressão, que DP-03 pede | A equipe precisa aprender as decisões do framework antes de escrever regra (R3). Trocar de framework depois é reescrever a borda e a persistência | Aceita |
| A-03 | As regras ficam nas classes de modelo do framework, que juntam domínio e persistência. Descartado: classes de domínio separadas do ORM, com um repositório entre elas | O domínio tem duas classes, e uma camada a mais não resolve problema que a equipe tenha hoje (`PROJETO.md`, padrão antes do problema) | O domínio depende do ORM. A regra é testada com objeto não gravado, sem banco | Aceita |
| A-04 | A conta é um modelo de usuário próprio, só com os campos do `PROJETO.md`, criado já no esqueleto. Descartado: o modelo de usuário padrão do framework | O padrão traz e-mail, nome, sobrenome, data de cadastro, último acesso e marcas de equipe, que RE-02 manda não pedir. O framework exige o modelo de usuário definido antes da primeira migração | Sem o painel administrativo do framework nesta versão, porque ele depende das marcas de equipe. A conta só nasce pelo cadastro (HU-01) ou pelo terminal | Aceita |
| A-05 | Dois módulos, `contas` e `avisos`; `avisos` depende de `contas`, nunca o contrário. Descartado: um módulo só | A regra de quem publica (RN-01), a que mais deve mudar (R9, D2), fica na conta e muda sem tocar o aviso | O mural, que mostra o autor, junta as duas tabelas pela chave estrangeira | Aceita |
| A-06 | Depois de gravar, a resposta redireciona com 303 para uma página lida com GET. Descartado: responder a página direto ao envio do formulário | RNF-03: recarregar a página não publica de novo | A confirmação precisa estar na página de destino; no mural, o aviso no topo é a confirmação | Aceita |
| A-07 | Formulário recusado responde 422, com a mesma página, a mensagem e o que foi preenchido, menos a senha. Descartado: responder 200 com a mensagem | O código de status diz ao navegador e aos testes que o pedido foi recusado. CA-01.2 e CA-03.3 pedem o preenchimento mantido | Os testes conferem o código, além do texto | Aceita |
| A-08 | O autor vem da sessão, e o instante vem do banco; nenhum dos dois é campo de formulário. Descartado: campo escondido com o autor | Campo de formulário pode ser alterado por quem envia, e o autor visível é a defesa de N7 e de R9. DP-10 já tirou o instante da tela | Publicar exige sessão válida em toda requisição | Aceita |
| A-09 | Migrações do framework desde o esqueleto. Descartado: esquema escrito à mão, fora do framework | O modelo de conta precisa de migração antes de tudo (A-04), e cada mudança de esquema fica no Git, com o código que a pede | Toda mudança de modelo vem com a migração no mesmo pull request. O `ROTEIRO.md` punha migrações no capítulo 14; lá fica a aplicação delas na implantação | Aceita |
| A-10 | Configuração lida de variáveis de ambiente, com valores de desenvolvimento quando a variável falta | A mesma aplicação roda no notebook de cada integrante e, depois, na hospedagem | A chave secreta de desenvolvimento fica no código e não pode ir para a hospedagem; o tratamento de segredos é do capítulo 13 | Aceita para desenvolvimento |
| A-11 | Hospedagem e servidor de produção | Dependem das opções que R4 levanta | O servidor de desenvolvimento do framework só serve para trabalhar e para a demonstração do encontro 9 | Proposta, a decidir no capítulo 14 |

## Pontos em aberto

- Hospedagem e servidor de produção: capítulo 14, com as opções de R4 (A-11).
- Segredos fora do código, a começar pela chave secreta: capítulo 13 (A-10).
- Respostas de falta de identificação e de permissão, além das já descritas: capítulo 13.

## Histórico de revisão

- 2026-10-24: esqueleto, participantes, responsabilidades e diagramas (#69).
- 2026-10-24: decisões A-01 a A-11 (#70).
