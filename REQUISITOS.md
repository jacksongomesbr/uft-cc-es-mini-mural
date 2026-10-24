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

Preenchido na issue #35.

## Histórias de usuário e critérios de aceitação

Histórias preenchidas na issue #35; critérios, na issue #36.

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
