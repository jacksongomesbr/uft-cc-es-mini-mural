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

Preenchidas na issue #70.

## Pontos em aberto

- Hospedagem e servidor de produção: capítulo 14, com as opções de R4.

## Histórico de revisão

- 2026-10-24: esqueleto, participantes, responsabilidades e diagramas (#69).
