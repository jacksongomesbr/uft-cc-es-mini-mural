# Contrato das rotas

O Mini Mural monta as páginas no servidor (A-01), e por isso não tem API com
respostas em JSON. O contrato descreve as rotas: método, caminho, campos do
formulário, regras que o servidor aplica, código de status e destino. No lugar
dos exemplos de resposta, cada resposta diz a página, a mensagem exata e os
campos mantidos (A-12). Os testes do capítulo 12 conferem o código e a
mensagem.

Mudar uma rota, um campo ou uma mensagem passa por pull request que altera este
arquivo. Os nomes de campo são do glossário, e nenhum é nome de coluna.

## Respostas usadas

| Código | Nome no padrão | Quando |
|---|---|---|
| 200 | OK | A página pedida |
| 302 | Found | Página que exige conta, pedida sem conta: vai para `/entrar/`, com o caminho de volta |
| 303 | See Other | Formulário aceito: a página seguinte é lida com GET (A-06, RNF-03) |
| 403 | Forbidden | Ação de outra pessoa, como arquivar o aviso de outro autor; também é a resposta do framework a formulário sem a marca de proteção contra envio forjado |
| 404 | Not Found | Aviso que não existe, ou que a pessoa não pode ver (CA-07.4) |
| 405 | Method Not Allowed | Método que a rota não aceita, como sair por GET |
| 422 | Unprocessable Content | Formulário recusado: a mesma página, com a mensagem e o que foi preenchido, menos a senha (A-07) |
| 503 | Service Unavailable | O banco não respondeu ao gravar (UC-01, 4e) |

## Contas

### GET /entrar/

- **Origem:** HU-02, CA-02.3
- **Entrada:** `next`, opcional, com o caminho para onde voltar. Só caminho
  deste site é aceito; qualquer outro vira `/`. `motivo=aviso-nao-publicado`,
  opcional, vem do redirecionamento de `POST /avisos/` sem conta.
- **Sucesso:** 200, página de entrar. Com `motivo=aviso-nao-publicado`, a página
  mostra "Você saiu da conta em outra aba. Entre de novo; o aviso não foi
  publicado." Quem já entrou recebe 303 para `/`.

### POST /entrar/

- **Origem:** HU-02, CA-02.1, CA-02.2
- **Entrada:** `nome_usuario`, `senha`, `next`
- **Regras no servidor:** confere o nome e a senha; abre a sessão.
- **Sucesso:** 303 para `next`, ou para `/`.
- **Falha:** 422, página de entrar com "Nome de usuário ou senha não conferem.";
  mantém o nome de usuário e deixa a senha vazia. A mensagem não diz qual dos
  dois errou (CA-02.2).

### POST /sair/

- **Origem:** HU-02, CA-02.4
- **Regras no servidor:** apaga a sessão no servidor.
- **Na página:** sair é um botão de formulário, com a marca de proteção. O
  protótipo desenha uma ligação porque é rascunho.
- **Sucesso:** 303 para `/entrar/`.
- **GET /sair/:** 405, com uma página que oferece o botão de sair. Sair só por
  formulário, para que uma ligação ou o carregamento antecipado de uma página
  não tire a pessoa da conta.

### GET /cadastro/

- **Origem:** HU-01
- **Sucesso:** 200, página de criar conta. Quem já entrou recebe 303 para `/`.

### POST /cadastro/

- **Origem:** HU-01, CA-01.1 a CA-01.6, RE-02
- **Entrada:** `nome_usuario`, `nome_exibicao`, `senha`
- **Regras no servidor:**
  - nome de usuário único, sem diferenciar maiúsculas (CA-01.2);
  - senha com pelo menos 8 caracteres e algo além de números (CA-01.3);
  - nome para exibição obrigatório (CA-01.5);
  - nome para exibição único depois de tirar os espaços das pontas e juntar
    os repetidos, sem diferenciar maiúsculas (CA-01.6).
- **Sucesso:** 303 para `/`, com a sessão já aberta (CA-01.1).
- **Falhas:** 422, página de criar conta, com o que foi preenchido menos a
  senha. Cada campo recusado mostra a sua mensagem, junto dele, e mais de uma
  pode aparecer ao mesmo tempo:
  - "Esse nome de usuário já está em uso."
  - "A senha precisa de pelo menos 8 caracteres, com algo além de números."
  - "Escolha um nome para exibição; ele aparece como autor dos avisos."
  - "Esse nome para exibição já está em uso. Escolha outro."

## Avisos

### GET /

- **Origem:** HU-04, CA-04.1 a CA-04.3, CA-02.3
- **Sem conta:** 302 para `/entrar/?next=/` (CA-02.3). Quando HU-06 entrar,
  quem não entrou passa a ver os avisos abertos.
- **Com conta:** 200, o mural. Os avisos publicados, do mais recente para o mais
  antigo, com desempate pelo identificador (DP-06). Cada aviso mostra o texto,
  o nome para exibição e o nome de usuário do autor, a data e a hora no horário
  de Palmas (CA-04.1, CA-04.3).
- **Mural vazio:** a página diz "Ainda não há avisos." (CA-04.2).

### GET /avisos/novo/

- **Origem:** UC-01, passos 1 e 2
- **Sem conta:** 302 para `/entrar/?next=/avisos/novo/`.
- **Com conta:** 200, página de publicar, com o campo do texto e o limite de 500
  caracteres.

### GET /avisos/

- **Origem:** HU-16, CA-16.1
- **Sucesso:** 303 para `/avisos/novo/`. É o endereço que fica na barra depois
  de uma recusa de `POST /avisos/`, e abri-lo de novo leva à página de
  publicar.

### POST /avisos/

- **Origem:** HU-03, CA-03.1 a CA-03.5, UC-01, RN-01
- **Entrada:** `texto`. O autor não é campo: vem da sessão (A-08).
- **Regras no servidor:**
  - sessão válida e RN-01 (quem pode publicar);
  - quebras de linha enviadas pelo navegador contam um caractere cada;
  - o texto, sem os espaços das pontas, tem de 1 a 500 caracteres (CA-03.2 a
    CA-03.4);
  - o instante vem do banco (DP-10).
- **Sucesso:** 303 para `/`, com o aviso no topo do mural (A-06).
- **Falhas:**
  - **Sem conta:** 302 para
    `/entrar/?next=/avisos/novo/&motivo=aviso-nao-publicado`, e nada é
    gravado. O texto se perde, porque a sessão que o levaria já não existe, e
    a mensagem diz isso (UC-01, 4c; CA-02.4).
  - **Texto vazio ou só com espaços:** 422, página de publicar com "O aviso
    precisa de texto. Nada foi publicado." (UC-01, 4a; CA-03.2).
  - **Acima do limite:** 422, página de publicar com "O aviso tem N caracteres,
    e o limite é 500. Corte X caracteres e publique de novo.", e o texto
    mantido (UC-01, 4b; CA-03.3). Quando X é 1, a mensagem diz "Corte 1
    caractere".
  - **Banco sem resposta (ainda não implementado, HU-03.2):** 503, página de
    publicar com "O aviso não foi publicado, porque o sistema não conseguiu
    gravar. O texto continua no campo; tente de novo em instantes.", e o
    texto mantido (UC-01, 4e). A mensagem é proposta da equipe, e a
    alternativa ainda não tem critério.

## Depois da review parcial

Rotas das histórias importantes, em esboço. Elas se completam no planejamento
da iteração em que HU-05 a HU-07 entrarem.

### GET /avisos/{id}/

- **Origem:** HU-06, CA-07.4, CA-07.5, RNF-06
- **Sucesso:** 200, o aviso. Aviso interno pedido sem conta: 302 para
  `/entrar/`. Aviso arquivado pedido por quem não é o autor: 404, a mesma
  resposta de aviso inexistente (CA-07.4).

### POST /avisos/{id}/arquivar/

- **Origem:** HU-07, CA-07.1 a CA-07.3, RN-02
- **Sucesso:** 303 para `/`. Arquivar de novo também responde 303, e nada muda
  (CA-07.3).
- **Falhas:** 403, "Só quem publicou o aviso pode arquivá-lo." (CA-07.2);
  404 para aviso que não existe ou arquivado de outra pessoa.
