# Testes

Este documento diz o que a equipe testa, em que nível, com que ambiente e com
que critério de pronto, e o que ela deixa de testar de propósito. Os casos saem
dos critérios de aceitação do `REQUISITOS.md`: o "Dado" vira o preparo, o
"Quando" vira os passos, e o "Então" vira o resultado esperado. A estratégia é
revista a cada iteração.

## Estratégia

| Nível | O que se testa | Como | Quem escreve | Quando |
|---|---|---|---|---|
| Unidade | Regras do domínio sem banco nem servidor: o texto do aviso, o nome para exibição, as regras de senha, quem vê e quem arquiva | Testes do framework que não abrem banco | Quem implementou | Junto com o código |
| Integração | Cada rota com formulário e banco, contra o contrato: código de status, destino e mensagem | Testes com o cliente do framework e o banco de teste | Quem implementou; quem revisa confere contra o contrato | No pull request |
| Sistema | O fluxo principal no navegador, em 360 por 640, na build identificada | Roteiro manual, como o da review parcial | Quem não implementou o fluxo | Antes de cada demonstração |
| Aceitação | Os critérios do fluxo com quem usa | Sessão com a servidora da secretaria | A equipe e a secretaria | Na review final, encontro 16 |

**Ambiente.** PostgreSQL local; o framework cria um banco de teste a cada
execução e o apaga no fim. Os critérios que dependem de hora (CA-04.1, CA-04.3,
CA-07.3) fixam o instante no próprio caso, e nenhum resultado depende da data de
hoje. A exceção é o caso do instante vindo do banco, que compara com o relógio,
com tolerância de um minuto.

**Identificação da build.** Todo resultado registra a tag ou o commit
executado. Resultado sem build não se liga a uma entrega.

**Critério de saída.** Todo caso do fluxo principal executado e com resultado,
nenhum defeito major aberto, e cada caso bloqueado listado com a pergunta que o
desbloqueia.

**Resultado de um caso.** Aprovado, falhou, bloqueado ou não executado. Caso
bloqueado é falta de evidência, e não aprovação.

## O que não se testa

| Fica de fora | Motivo | Risco aceito |
|---|---|---|
| Navegadores além do Chrome | O RNF-08 foi conferido nas ferramentas do Chrome, e a compatibilidade está sem exigência no `REQUISITOS.md` | O Safari do celular pode mostrar a página diferente |
| Mais de 200 avisos no mural | O RNF-01 foi escrito para 200 avisos | Com mais avisos, o mural pode passar de 3 segundos; é a dívida #111 |
| Resistência a ataques | Teste funcional não demonstra resistência a ataque, e a equipe não tem o conhecimento para um teste de intrusão (A-13) | Uma falha de segurança que nenhum caso descreve passa sem ser vista; o capítulo 13 revê os segredos e as dependências |
| Leitor de tela | Nenhum requisito pede acessibilidade além do RNF-02 | Uma pessoa com deficiência visual pode não ouvir as mensagens de recusa |

## Casos

A coluna "Teste" aponta para o teste automatizado que executa o caso. A
coluna "Classe ou limite" diz a partição de equivalência ou o valor limite que o
caso representa.

### HU-01 Criar conta

| ID | Critério | Classe ou limite | Preparo | Passos | Esperado | Nível | Teste |
|---|---|---|---|---|---|---|---|
| TC-01.1 | CA-01.1 | Dados válidos | Nenhuma conta "livia.m" | Criar conta com nome, nome para exibição e senha de 12 caracteres | 303 para o mural, já dentro | Integração | `test_ca_01_1_conta_criada_e_ja_dentro` |
| TC-01.2 | CA-01.2 | Nome em uso, com maiúsculas | Conta "livia.m" | Criar "Livia.M" | 422, mensagem do contrato, nome para exibição mantido, senha não | Integração | `test_ca_01_2_nome_de_usuario_em_uso` |
| TC-01.3a | CA-01.3 | Limite: 7 caracteres | Nenhum | Senha "1234567" | 422, regra da senha | Integração | `test_ca_01_3_senha_fraca` |
| TC-01.3b | CA-01.3 | Só números, 8 caracteres | Nenhum | Senha "12345678" | 422, regra da senha | Integração | `test_ca_01_3_senha_fraca` |
| TC-01.3c | CA-01.3 | Limite: 8 caracteres, com letra | Nenhum | Senha "abcd1234" | Aceita | Unidade | `test_tc_01_3_limites` |
| TC-01.4 | CA-01.4 | A conta continua | Conta criada e saída | Entrar com o mesmo nome e senha | Reconhecida | Integração | `test_ca_01_4_a_conta_continua` |
| TC-01.5 | CA-01.5 | Só espaços | Nenhum | Nome para exibição "   " | 422, mensagem do contrato | Integração | `test_ca_01_5_nome_para_exibicao_obrigatorio` |
| TC-01.6a | CA-01.6 | Maiúsculas e espaços a mais | "Secretaria do curso" existe | Criar com "secretaria  do curso " | 422, nome em uso | Integração | `test_ca_01_6_nome_para_exibicao_em_uso` |
| TC-01.6b | CA-01.6 | Espaços a mais, sem banco | Nenhum | Normalizar "  Secretaria   do curso " | "Secretaria do curso" | Unidade | `test_normalizar_nome_tira_espacos_a_mais` |
| TC-01.6c | CA-01.6 | Difere só por acento | "Secretaria do curso" existe | Criar com "Secretária do curso" | Sem resultado esperado: pergunta em aberto (#126, achado 4) | Integração | Bloqueado |

### HU-02 Entrar e sair

| ID | Critério | Classe ou limite | Preparo | Passos | Esperado | Nível | Teste |
|---|---|---|---|---|---|---|---|
| TC-02.1 | CA-02.1 | Nome e senha certos | Conta "paula.sec" | Entrar | 303 para o mural, nome no topo | Integração | `test_ca_02_1_entrar_leva_ao_mural_e_mostra_quem_entrou` |
| TC-02.2 | CA-02.2 | Senha errada | Conta "paula.sec" | Entrar com senha errada | 422, mensagem sem dizer qual errou | Integração | `test_ca_02_2_senha_errada` |
| TC-02.3 | CA-02.3 | Página que exige conta | Sem sessão | Abrir `/avisos/novo/`, entrar | Vai a entrar e volta à página de publicar | Integração | Ida: `test_pagina_de_publicar_sem_conta`; volta: a escrever com HU-06 (#131), que também tira o teste antigo do mural |
| TC-02.4 | CA-02.4 | Depois de sair | Entrou e saiu | Publicar pela mesma aba | 302 para entrar, nada publicado | Integração | `test_ca_02_4_depois_de_sair_nada_e_publicado` |

### HU-03.1 Publicar aviso curto

| ID | Critério | Classe ou limite | Preparo | Passos | Esperado | Nível | Teste |
|---|---|---|---|---|---|---|---|
| TC-03.1 | CA-03.1 | Texto válido | Paula entrou | Publicar a troca de sala | 303, aviso no topo com autor, data e hora | Integração | `test_ca_03_1_publicar` |
| TC-03.2a | CA-03.2 | Vazio | Paula entrou | Publicar "" | 422, nada publicado | Integração | `test_ca_03_2_texto_vazio_ou_so_com_espacos` |
| TC-03.2b | CA-03.2 | Só espaços e quebras | Paula entrou | Publicar "  \r\n  " | 422, nada publicado | Integração | `test_ca_03_2_texto_vazio_ou_so_com_espacos` |
| TC-03.3a | CA-03.3 | Limite: 501 | Paula entrou | Publicar 501 caracteres | 422, "Corte 1 caractere", texto mantido | Integração | `test_ca_03_3_acima_do_limite` |
| TC-03.3b | CA-03.3 | 500 com espaços nas pontas | Nenhum | Preparar "  " + 500 caracteres + "  " | Aceito: as pontas não contam | Unidade | `test_tc_03_3b_500_com_espacos_nas_pontas` |
| TC-03.4a | CA-03.4 | Limite: 500 acentuados | Paula entrou | Publicar 500 "á" | 303, 500 caracteres gravados | Integração | `test_ca_03_4_no_limite_com_acento` |
| TC-03.4b | CA-03.4 | Quebra de linha do navegador | Paula entrou | Publicar 250 + "\r\n" + 249 | 303, a quebra conta um | Integração | `test_quebra_de_linha_do_navegador_conta_um` |
| TC-03.4c | CA-03.4 | Emoji composto | Nenhum | Preparar texto com um emoji de família | Conta os pontos de código, como o glossário define | Unidade | `test_tc_03_4c_emoji_composto_conta_pontos_de_codigo` |
| TC-03.5 | CA-03.5 | O aviso continua | Paula publicou | Outra conta abre o mural | Aviso lá, com o mesmo autor | Integração | `test_ca_03_5_o_aviso_continua` |

### HU-04 Ver o mural

| ID | Critério | Classe ou limite | Preparo | Passos | Esperado | Nível | Teste |
|---|---|---|---|---|---|---|---|
| TC-04.1a | CA-04.1 | Muitos avisos | Avisos às 8h, 9h e 10h | Abrir o mural | Ordem 10h, 9h, 8h, com os dois nomes, data e hora | Integração | `test_ca_04_1_mais_recentes_primeiro_com_autor_data_e_hora` |
| TC-04.1b | CA-04.1 | Mesmo instante | Dois avisos às 9h | Abrir o mural | O mais novo primeiro | Integração | `test_ca_04_1_desempate_pelo_mais_novo` |
| TC-04.2 | CA-04.2 | Zero avisos | Nenhum aviso | Abrir o mural | "Ainda não há avisos." | Integração | `test_ca_04_2_mural_vazio` |
| TC-04.3 | CA-04.3 | Hora guardada em UTC | Aviso às 17h02 UTC | Abrir o mural | 14h02 | Integração | `test_ca_04_3_hora_local` |

### HU-16 Endereço de publicar depois de uma recusa

| ID | Critério | Classe ou limite | Preparo | Passos | Esperado | Nível | Teste |
|---|---|---|---|---|---|---|---|
| TC-16.1 | CA-16.1 | Recusa por limite | Paula entrou | Publicar 501, abrir `/avisos/` | 303 para a página de publicar | Integração | `test_ca_16_1_endereco_depois_da_recusa` |

### HU-05 Marcar o aviso como aberto ou interno

Escritos antes do código (#130).

| ID | Critério | Classe ou limite | Preparo | Passos | Esperado | Nível | Teste |
|---|---|---|---|---|---|---|---|
| TC-05.1 | CA-05.1 | Sem tipo | Paula entrou | Publicar sem o campo tipo | Aviso interno | Integração | A escrever |
| TC-05.2 | CA-05.2 | Aberto | Paula entrou | Publicar com tipo aberto | Aviso aberto | Integração | A escrever |
| TC-05.3 | CA-05.3 | Tipo fora da lista | Paula entrou | Publicar com tipo "publico" | 422, mensagem do contrato, nada publicado | Integração | A escrever |
| TC-05.4 | CA-05.4 | Um aberto e um interno | Dois avisos | Pessoa com conta abre o mural | Cada aviso mostra o tipo | Integração | A escrever |

### HU-06 Ler aviso aberto sem conta

Escritos antes do código (#131). A partição é quem pede, visitante ou pessoa
com conta, contra o tipo e a situação do aviso.

| ID | Critério | Classe ou limite | Preparo | Passos | Esperado | Nível | Teste |
|---|---|---|---|---|---|---|---|
| TC-06.1 | CA-06.1 | Visitante, aberto e interno | Um aberto e um interno | Visitante abre o mural | Só o aberto, com autor, data e hora | Integração | A escrever |
| TC-06.2 | CA-06.2 | Visitante, nenhum aberto | Só internos | Visitante abre o mural | "Ainda não há avisos abertos." e o caminho para entrar | Integração | A escrever |
| TC-06.3 | CA-06.3, RNF-06 | Visitante, interno pelo endereço | Um interno | Visitante pede `/avisos/{id}/` | 302 para entrar, sem o texto | Integração | A escrever |
| TC-06.4 | CA-06.4 | Visitante, aberto pelo endereço | Um aberto | Visitante pede `/avisos/{id}/` | 200, o aviso | Integração | A escrever |
| TC-06.5 | Regra de quem vê | Domínio, sem banco | Avisos aberto, interno e arquivado não gravados | Perguntar se cada um pode ser visto por visitante, pelo autor e por outra conta | Visitante vê só o aberto publicado; outra conta vê os publicados, abertos e internos; o autor vê também o próprio arquivado | Unidade | A escrever |

### HU-07 Arquivar o próprio aviso

Escritos antes do código (#132).

| ID | Critério | Classe ou limite | Preparo | Passos | Esperado | Nível | Teste |
|---|---|---|---|---|---|---|---|
| TC-07.1 | CA-07.1 | Autor, aviso publicado | Aviso de "prof.calculo" | Ele arquiva | 303, aviso fora do mural, data registrada | Integração | A escrever |
| TC-07.2a | CA-07.2 | Outra conta, aviso publicado | Aviso de "paula.sec" | "prof.calculo" arquiva | 403, mensagem do contrato, aviso no mural | Integração | A escrever |
| TC-07.2b | CA-07.2, CA-07.4 | Outra conta, aviso já arquivado | Aviso arquivado de "paula.sec" | "prof.calculo" arquiva | 404, como aviso inexistente | Integração | A escrever |
| TC-07.3 | CA-07.3 | Arquivar de novo | Arquivado às 10h | O autor arquiva às 11h | 303, a data continua 10h | Integração | A escrever |
| TC-07.4 | CA-07.4 | Outra conta pede o arquivado | Aviso arquivado de "paula.sec" | Outra conta pede o endereço | 404 | Integração | A escrever |
| TC-07.5 | CA-07.5 | Autor pede o arquivado | Aviso arquivado de "paula.sec" | Ela pede o endereço | 200, com a data e a hora do arquivamento | Integração | A escrever |
| TC-07.6 | CA-07.4 | Visitante pede o arquivado | Aviso arquivado e aberto | Visitante pede o endereço | 404, e não a página de entrar | Integração | A escrever |
| TC-07.7 | Lista de verificação | Endereço depois da recusa | Recusa do TC-07.2a | Abrir `/avisos/{id}/arquivar/` com GET | 303 para o aviso | Integração | A escrever |

O TC-07.6 saiu da partição, e não de um critério escrito: o CA-07.4 fala de
"outra pessoa com conta", e o visitante é outra pessoa sem conta. O contrato
responde 404 para quem não é o autor, e o caso segue o contrato.

### Requisitos não funcionais

| ID | Requisito | Esperado | Nível | Como |
|---|---|---|---|---|
| TC-RNF-01 | RNF-01 | Até 3 s com 200 avisos e rede limitada | Sistema | Medição na preparação de cada demonstração; a consulta fixa em 3 idas ao banco está em `test_rnf_01_uma_consulta_para_os_avisos_e_autores` |
| TC-RNF-03 | RNF-03 | Recarregar não publica de novo | Integração | `test_rnf_03_recarregar_nao_publica_de_novo` |
| TC-RNF-04 | RNF-04 | Senha guardada como valor derivado | Integração | `test_senha_guardada_como_valor_derivado` |
| TC-RNF-05 | RNF-05 | Marcação mostrada como texto | Integração | `test_rnf_05_texto_mostrado_como_texto` |
| TC-RNF-06 | RNF-06 | Sem o texto do interno para quem não entrou | Integração e sistema | TC-06.3 e um pedido com `curl` sem sessão |
| TC-RNF-08 | RNF-08 | Sem rolagem horizontal em 360 pixels | Sistema | Ferramentas do navegador, página por página |

## Casos bloqueados

| Caso | Pergunta | Quem responde |
|---|---|---|
| TC-01.6c | Nomes que diferem só por acento contam como o mesmo? (`REQUISITOS.md`, abaixo do CA-01.6) | A coordenação, na revisão de C2 e R9 |

## Relatório

O resultado de cada execução, com a build, fica nesta seção (#133).

## Histórico de revisão

- 2026-10-25: primeira versão, com a estratégia, as omissões e os casos do
  fluxo principal e de HU-05 a HU-07 (#128).
