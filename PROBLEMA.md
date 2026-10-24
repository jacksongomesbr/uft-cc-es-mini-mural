# Problema proposto

Proposta da equipe para o projeto da disciplina, escrita no encontro 1. As
afirmações sobre o curso vêm da experiência dos integrantes como alunos e
serão conferidas com os usuários na descoberta (capítulo 4).

> **Atualização do encontro 4:** a descoberta foi feita e está no
> [DESCOBERTA.md](DESCOBERTA.md), que passa a ser a referência do problema.
> Este arquivo fica como registro da proposta inicial. As regras listadas na
> verificação do tema foram conferidas lá: as de aviso aberto e interno e de
> arquivamento só pelo autor ainda dependem de decisão da coordenação (C2, C3).

## Equipe

Ana, Bruno, Carla, Davi e Eva. A equipe é simulada, como explica o
[ROTEIRO.md](ROTEIRO.md). Os papéis serão definidos no `PROCESSO.md`, no
capítulo 3.

## O problema

No curso de Ciência da Computação, os avisos para os alunos circulam por canais
separados: grupos de mensagem de cada turma, e-mail institucional e o mural de
papel do bloco. A equipe observa três consequências:

- quem não está no grupo de uma turma, ou saiu dele, perde o aviso;
- quem publica não tem um lugar único em que o aviso fique registrado, com
  autor e data;
- aviso vencido continua no mural de papel, misturado aos que ainda valem.

Alguns avisos interessam a qualquer pessoa, como uma palestra aberta. Outros
só fazem sentido para quem é do curso, como uma troca de sala.

## Usuário pretendido

- **Quem publica:** a secretaria da coordenação, os professores e o centro
  acadêmico.
- **Quem lê:** os alunos do curso e, nos avisos abertos, qualquer visitante.

A conversa com os usuários é viável porque eles estão no mesmo bloco da
equipe. A secretaria atende no horário de expediente, e Eva fica responsável
por marcar a primeira entrevista. Davi procura os professores ao fim das aulas,
Carla conversa com os representantes do centro acadêmico, e Ana e Bruno ouvem
os colegas de turma nos intervalos.

## Por que o software existe

Para que cada aviso tenha um lugar único, com autor e data, separando o que é
público do que é só da comunidade do curso, e para que o aviso que perdeu a
validade saia do mural sem que outra pessoa precise apagá-lo.

## Verificação do tema

| Critério | Atende? | Evidência e ressalva |
|---|---|---|
| Usuário real e acessível | Sim | Secretaria, professores e colegas estão no bloco do curso. Ressalva: o horário da secretaria limita as entrevistas. |
| Regra de negócio, e não apenas cadastro | Sim | Aviso público ou restrito a quem entrou, arquivamento só por quem publicou, aviso arquivado fora do mural. Ressalva: as regras ainda são hipóteses da equipe. |
| Dado que justifique persistência | Sim | Avisos com autor, data de publicação e data de arquivamento, consultados em ordem de data. |
| Escopo cabível em um semestre | Sim | Um dado principal, o aviso, e as contas de quem publica. Ficam fora anexos, notificações e integração com outros sistemas. |
| Sem dependência de acesso incerto | Sim | O sistema tem contas próprias. A equipe descarta entrar com a conta institucional, porque isso depende de autorização da universidade. |
| Sem dado pessoal sensível | Sim | O sistema guarda nome de usuário e senha, esta só como hash. Não pede matrícula, CPF nem telefone. |
