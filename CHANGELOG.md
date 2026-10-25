# Registro de mudanças

Todas as mudanças relevantes do projeto ficam registradas aqui. O formato
segue o [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/), e as
versões seguem o [versionamento semântico](https://semver.org/lang/pt-BR/).

## [0.11.0] - 2026-10-25

Fim do capítulo 12: testes automatizados e integração contínua, e fim da
iteração 5.

### Adicionado

- Opções de hospedagem levantadas para R4, com o conflito entre as
  hospedagens gratuitas e o RNF-01 (`ARQUITETURA.md`, #151).
- Plano da iteração 5, de uma semana (#152).
- `requirements-dev.txt`, com as ferramentas de verificação (#153).
- Ruff como formatador e verificador de estilo, com as regras no
  `pyproject.toml` e o que a ferramenta decide no `CONTRIBUTING.md` (#154).
- Verificação automática no GitHub Actions a cada pull request e a cada envio
  ao `main`, com PostgreSQL 18 de serviço (`.github/workflows/verificacao.yml`,
  #155).
- Cobertura de linhas e desvios, e os testes das duas regras do contrato que o
  mapa mostrou sem teste (#156).
- HU-18: confirmar antes de arquivar, pelo ciclo do desenvolvimento guiado por
  testes (#157).
- Execução automatizada e casos fora da automação no `TESTES.md`, relatório da
  build `1c57be3` e fim da iteração 5 com 7 de 7 pontos (#158).

### Alterado

- Dependências da aplicação com a versão fixa, que paga a dívida #110 (#153).
- Código formatado pelo Ruff; a recusa da senha guarda a causa original (#154).
- Proteção do `main`: a integração exige a verificação `testes` verde e o ramo
  atualizado com o `main` (#155).
- O "Arquivar" do mural e da página do aviso leva à página de confirmação, e o
  contrato do GET de arquivar acompanha (#157).
- Critério de saída do `TESTES.md` com a verificação verde no `main` (#158).

## [0.10.0] - 2026-10-25

Fim do capítulo 11: verificação e validação, e fim da iteração 4.

### Adicionado

- Inspeção de requisitos com os cinco papéis e cinco achados, quatro major
  (#126).
- Estratégia de teste, omissões deliberadas e 52 casos derivados dos critérios,
  com partição e valor limite (`TESTES.md`, #128).
- A-13: o que os testes funcionais não provam (`ARQUITETURA.md`, #128).
- Testes de unidade das regras do texto e da senha, sem banco (#129).
- HU-05: aviso aberto ou interno (#130).
- HU-06: aviso aberto lido sem conta, e a página de cada aviso (#131).
- HU-07: arquivar o próprio aviso (#132).
- Relatório de teste da build `18ea9f7`, teste de utilidade, HU-17 e HU-18, e
  o fim da iteração 4 com 12 de 12 pontos (#133).

### Alterado

- Critérios de HU-05 e HU-06 escritos antes do código; CA-02.3 e CA-07.2
  corrigidos; "caractere" no glossário; pergunta do nome com acento em aberto
  (`REQUISITOS.md`, #127).
- Rotas de HU-05 a HU-07 completas no contrato (#127).
- DP-12: a regra de quem vê em duas formas, com teste de concordância
  (`PROJETO.md`, #131).
- Rastreabilidade ligada aos casos do `TESTES.md` (#133).

## [0.9.0] - 2026-10-25

Fim do capítulo 10: qualidade de processo e produto.

### Adicionado

- Lista de verificação de revisão, com a pergunta tirada do defeito que
  escapou, e os tipos de comentário (`CONTRIBUTING.md`, #112).
- Modelo de descrição de pull request (`.github/pull_request_template.md`,
  #112).
- Plano da iteração 4, com a reserva técnica escolhida pelas mudanças
  esperadas (`ITERACOES.md`, #113).
- HU-16: `GET /avisos/` leva à página de publicar (#114).
- Testes de abrir de novo o endereço das rotas que recebem formulário (#115).
- Qualidade da revisão: aderência, eficácia, objetivo, perguntas e métricas
  (`PROCESSO.md`, #117); DP-11 e a leitura do módulo de avisos pela
  manutenibilidade (`PROJETO.md`, #117).
- Quatro dívidas técnicas registradas com custo de carregar, custo de pagar e
  gatilho (#109, #110, #111 e #116).

### Alterado

- A publicação usa o formulário do framework, sem mudar o comportamento:
  dívida paga na reserva da iteração 4 (#116).

### Corrigido

- `GET /avisos/` dava página vazia depois de uma recusa (#114).
- `GET /sair/` dava página vazia depois de um envio recusado pela proteção do
  formulário; continua 405, agora com página (#115).

## [0.8.0] - 2026-10-24

Fim do capítulo 9: review parcial, com a demonstração do código da `v0.7.0`.

### Adicionado

- Preparação da review: roteiro com o critério de cada passo, o que é
  declarado, papéis, decisões a defender, plano da falha e ensaio
  (`ITERACOES.md`, #98).
- Script que restaura o banco da demonstração e recusa banco que não termine
  em `_demo`, e o texto preparado do passo 5 (`scripts/`, #98).
- Registro da review, simulado: observações, autoavaliação com os cinco status
  (`ITERACOES.md`, #99).
- HU-16, defeito do endereço vazio depois de uma recusa, com CA-16.1, e CA-03.6
  para HU-03.2 (`REQUISITOS.md`, #100).
- Resultado e retrospectiva da iteração 3, com a primeira velocidade, 14 pontos
  (`ITERACOES.md`, #101).

### Alterado

- Artefatos corrigidos para descrever o que roda: índices que o framework cria
  (DP-07), onde mora a regra do texto, o campo sem limite e a alternativa 4e
  ainda não implementada (#97).
- HU-15 passa de fora desta versão a desejável, e N15 fica confirmada; HU-05 e
  HU-06 sobem ao topo dos importantes (#100).
- `PROCESSO.md` com as mudanças da retrospectiva da iteração 3 (#101).

## [0.7.0] - 2026-10-24

Fim do capítulo 8: planejamento da iteração 3 e o produto mínimo viável em
funcionamento.

### Adicionado

- Registro das iterações, com o plano da iteração 3, a rodada de estimativa,
  o quadro e a retrospectiva das iterações 1 e 2 (`ITERACOES.md`, #83).
- Criar conta (HU-01, #84), entrar e sair (HU-02, #85), ver o mural (HU-04,
  #86) e publicar aviso curto (HU-03.1, #87), com um teste por critério de
  aceitação: 54 testes no total.
- Modelo do aviso e a migração, com as restrições do `PROJETO.md` (#86).
- Comando `carregar_demonstracao` e a preparação da demonstração do encontro
  9, com a medição do RNF-01 (#88).

### Alterado

- Backlog com pontos, e HU-03 fatiada em HU-03.1 e HU-03.2 (`REQUISITOS.md`,
  #83).
- `PROCESSO.md` com o quadro, os limites de trabalho em andamento e as
  práticas adotadas (#83).
- Contrato: "Corte 1 caractere", no singular (#87).

### Corrigido

- O cadastro mostra a mensagem do CA-01.2, em vez de erro 500, quando o banco
  recusa um nome gravado ao mesmo tempo por outra pessoa (#84).

## [0.6.0] - 2026-10-24

Fim do capítulo 7: arquitetura e esqueleto do projeto Django.

### Adicionado

- Documento de arquitetura com responsabilidades, participantes, visão geral e
  implantação (#69), decisões A-01 a A-12 (#70, #71), verificações, qualidades
  e custos (#72) e a conferência do contrato (#74) (`ARQUITETURA.md`).
- Contrato das rotas do fluxo principal (`contrato/operacoes.md`, #71, #74).
- Esqueleto do projeto Django: configuração lida do ambiente, módulos `contas`
  e `avisos`, modelo de conta com os campos do `PROJETO.md`, página inicial,
  modelo base de página e 13 testes (#73).
- Instruções de desenvolvimento no README (#73).

### Alterado

- O `ROTEIRO.md` aponta para a decisão A-01 e passa a dizer, no capítulo 14,
  aplicação das migrações na implantação, porque as migrações começaram no
  esqueleto (A-09) (#75).

## [0.5.0] - 2026-10-24

Fim do capítulo 6: modelagem e projeto.

### Adicionado

- Documento de projeto com modelo de domínio (#55), modelo de dados e
  decisões de armazenamento (#56), estados do aviso (#57), sequência do UC-01,
  atividade do aviso vencido, responsabilidades e teste de Parnas (#58), e o
  registro da conferência cruzada (#60) (`PROJETO.md`).
- Fontes dos diagramas em Mermaid (`diagrams/`, #55 a #58).
- Protótipo navegável do fluxo principal, com as recusas (`prototipo/`, #59).

### Alterado

- Primeira mudança de requisito depois da linha de base: nome para exibição
  repetido é recusado, o mural mostra o nome de usuário junto, e o risco que
  sobra entrou como R9 (`REQUISITOS.md`, `DESCOBERTA.md`, #53). A comparação
  do nome passou a ignorar espaços a mais (#56).
- Critérios de aceitação de HU-07, arquivado como estado final visto só pelo
  autor, e N15 com HU-15, levantados pelo diagrama de estados (#57).
- Escopo do `DESCOBERTA.md` com N13 e N14 (#53).
- README com os documentos novos (#61).

## [0.4.0] - 2026-10-24

Fim do capítulo 5: requisitos especificados e validados, primeiro marco.

### Adicionado

- Resposta da coordenação sobre quem publica e quem arquiva, e resposta à
  pergunta evitada (`descoberta/D2-resposta-da-secretaria.md`, #34).
- Documento de requisitos com glossário do domínio (#33), backlog ordenado com
  estimativa dos obrigatórios (#35), critérios de aceitação e rastreabilidade
  (#36), requisitos não funcionais, restrições e regras de negócio (#37) e o
  caso de uso UC-01 (#38) (`REQUISITOS.md`).
- Protótipo do MVP e registro da validação V1 (`validacao/`, #40).

### Alterado

- Descoberta atualizada com D2, R7, R8, N13 e N14, e com N6 confirmada
  (`DESCOBERTA.md`, #34, #39, #40).
- Achados da revisão com a lista de verificação incorporados (#39).
- Definição de pronto com cinco pontos (`PROCESSO.md`, #41).
- README com os documentos novos, e "aviso" como termo único (#42).

## [0.3.0] - 2026-10-24

Fim do capítulo 4: descoberta do problema com os usuários.

### Adicionado

- Roteiro de entrevista, com a abertura que pede autorização para gravar e o
  cuidado com dados de quem é entrevistado (`descoberta/roteiro-entrevista.md`,
  #22).
- Atas sem identificação de cinco entrevistas e uma observação, simuladas
  como a equipe (`descoberta/`, #23).
- Descoberta do problema: partes interessadas, personas, fontes, necessidades,
  conflitos com critério, cenários atual e pretendido, escopo, MVP e riscos
  (`DESCOBERTA.md`, #24).

### Alterado

- O `PROBLEMA.md` fica como registro da proposta inicial e aponta para o
  `DESCOBERTA.md`, que passa a ser a referência do problema; o `README.md`
  aponta para os dois (#25).

## [0.2.0] - 2026-10-24

Fim do capítulo 3: processo de desenvolvimento escolhido e registrado.

### Adicionado

- Processo iterativo e incremental, com a avaliação dos cinco fatores, as
  divergências da equipe, a compensação para o fator pessoal, as iterações até
  cada marco, os papéis e a definição de pronto (`PROCESSO.md`, #12 e #13).
- `PROCESSO.md` na tabela de documentos do `README.md` (#15).

### Alterado

- O `CONTRIBUTING.md` passa a apontar para o `PROCESSO.md` nos papéis e na
  definição de pronto, que deixa de ter duas cópias (#14).

## [0.1.0] - 2026-10-23

Fim dos capítulos 1 e 2: problema proposto e repositório configurado.

### Adicionado

- Problema proposto em uma página, com a verificação do tema contra os
  critérios da disciplina (`PROBLEMA.md`, #1).
- Convenções de ramos, commits, pull requests, revisão e definição de pronto
  (`CONTRIBUTING.md`, #2).
- `.gitignore` para um projeto Python e Django (#3).
- `README.md` com a apresentação do projeto e da equipe simulada (#4).
- Este registro de mudanças (#5).
- Proteção do `main`: envio direto e reescrita de histórico bloqueados, com
  pull request obrigatório.

[0.11.0]: https://github.com/jacksongomesbr/uft-cc-es-mini-mural/compare/v0.10.0...v0.11.0
[0.10.0]: https://github.com/jacksongomesbr/uft-cc-es-mini-mural/compare/v0.9.0...v0.10.0
[0.9.0]: https://github.com/jacksongomesbr/uft-cc-es-mini-mural/compare/v0.8.0...v0.9.0
[0.8.0]: https://github.com/jacksongomesbr/uft-cc-es-mini-mural/compare/v0.7.0...v0.8.0
[0.7.0]: https://github.com/jacksongomesbr/uft-cc-es-mini-mural/compare/v0.6.0...v0.7.0
[0.6.0]: https://github.com/jacksongomesbr/uft-cc-es-mini-mural/compare/v0.5.0...v0.6.0
[0.5.0]: https://github.com/jacksongomesbr/uft-cc-es-mini-mural/compare/v0.4.0...v0.5.0
[0.4.0]: https://github.com/jacksongomesbr/uft-cc-es-mini-mural/compare/v0.3.0...v0.4.0
[0.3.0]: https://github.com/jacksongomesbr/uft-cc-es-mini-mural/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/jacksongomesbr/uft-cc-es-mini-mural/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/jacksongomesbr/uft-cc-es-mini-mural/releases/tag/v0.1.0
