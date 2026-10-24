# Protótipo do MVP

Protótipo de baixa fidelidade do fluxo do produto mínimo viável, com uma tela
por passo, montado em uma hora para a sessão de validação V1. A aparência de
rascunho é proposital: rascunho recebe comentário sobre o passo que falta, e
tela com aparência acabada recebe comentário sobre cor e alinhamento.

Na sessão, cada tela foi impressa em uma folha, e quem conduz troca a folha
quando a pessoa "toca" em um elemento. Os textos entre colchetes são os
elementos que a pessoa pode tocar.

## Tela 1: entrar

```text
+-------------------------------------------+
| Mini Mural                                |
+-------------------------------------------+
| Nome de usuário  [ paula.sec           ]  |
| Senha            [ ************        ]  |
|                                           |
| [ entrar ]          [ criar conta ]       |
+-------------------------------------------+
```

## Tela 2: mural

```text
+-------------------------------------------+
| Mini Mural            paula.sec  [ sair ] |
+-------------------------------------------+
| [ publicar aviso ]                        |
|                                           |
| Prova de Cálculo II adiada para 05/11.    |
| prof.calculo - 23/10, 18h40               |
|-------------------------------------------|
| Inscrições abertas para a monitoria.      |
| ca.computacao - 22/10, 09h12              |
+-------------------------------------------+
```

## Tela 3: publicar aviso

```text
+-------------------------------------------+
| Publicar aviso                            |
+-------------------------------------------+
| [                                       ] |
| [                                       ] |
| [                                       ] |
|                    0 de 280 caracteres    |
|                                           |
| [ publicar ]        [ voltar ]            |
+-------------------------------------------+
```

## Tela 4: mural com o aviso publicado

```text
+-------------------------------------------+
| Mini Mural            paula.sec  [ sair ] |
+-------------------------------------------+
| [ publicar aviso ]                        |
|                                           |
| (o texto que a pessoa escreveu)           |
| paula.sec - agora                         |
|-------------------------------------------|
| Prova de Cálculo II adiada para 05/11.    |
| prof.calculo - 23/10, 18h40               |
+-------------------------------------------+
```

## Roteiro da sessão

1. **Situar.** "Você é da secretaria e precisa avisar a turma de uma mudança.
   A conta já está criada." A tela não é explicada.
2. **Tarefas, uma por vez.**
   - "A aula de Engenharia de Software de amanhã mudou para a sala 12 do bloco
     B. Avise a turma."
   - "A semana acadêmica tem uma palestra na quinta. Avise os alunos, com o que
     eles precisam saber para ir."
   - "Confira se o aviso apareceu."
3. **Observar em silêncio.** Quem anota registra onde a pessoa parou, o que
   procurou e o que chamou por outro nome, e cronometra a primeira tarefa
   (RNF-02).
4. **Perguntar no fim.** O que você esperava que acontecesse aqui? O que você
   faria se esta tela não existisse? O que falta para você conseguir terminar?
