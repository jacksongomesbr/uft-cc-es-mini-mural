// Contador de caracteres da página de publicar. É só ajuda: a página funciona
// sem ele, e quem decide o limite é o servidor (ARQUITETURA.md, verificações).
document.querySelectorAll("[data-limite]").forEach(function (campo) {
  var saida = document.getElementById(campo.dataset.contador);
  var limite = Number(campo.dataset.limite);

  function atualizar() {
    // Conta como o servidor: quebra de linha vale um, e as pontas não contam.
    // Array.from conta caracteres, e não unidades de 16 bits.
    var quantidade = Array.from(campo.value.replace(/\r\n/g, "\n").trim()).length;
    saida.textContent = quantidade + " de " + limite + " caracteres";
    saida.classList.toggle("erro", quantidade > limite);
  }

  campo.addEventListener("input", atualizar);
  atualizar();
});
