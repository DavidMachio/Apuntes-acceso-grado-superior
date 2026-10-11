/* Página de la materia de Lengua: lista de temas a partir de lengua/datos/curso.js y lengua/datos/temario.js */
(function () {
  const { esc } = DS;

  document.title = CURSO.materia + " · " + SITIO.marca;
  document.getElementById("titulo").textContent = CURSO.materia;
  document.getElementById("subtitulo").textContent = CURSO.subtitulo;

  document.getElementById("temas").innerHTML = MODULOS_LENGUA.map((m, i) => {
    const url = "tema.html?n=" + (i + 1);
    return '<li><div><h3 class="ds-index__title"><a href="' + url + '">' + esc(m.titulo) + "</a></h3><p>" + esc(m.resumen) + "</p></div>" +
      '<a class="ds-btn ds-btn--secondary ds-btn--sm" href="' + url + '" aria-label="Abrir el tema ' + esc(m.titulo) + '">Abrir</a></li>';
  }).join("");

  const diapositivas = MODULOS_LENGUA.reduce((n, m) => n + (parseInt(m.paginas, 10) || 0), 0);
  DS.cifras("cifras", [
    { tipo: "grande marca", etiqueta: "Temario", valor: String(MODULOS_LENGUA.length), unidad: "temas", texto: MODULOS_LENGUA[0].titulo + " y " + MODULOS_LENGUA[1].titulo.toLowerCase() + ", cada uno con su presentación en PDF." },
    { tipo: "oscura", etiqueta: "Banco de preguntas", valor: "—", texto: "Próximamente." },
    { etiqueta: "Presentaciones", valor: String(diapositivas), unidad: "diapositivas", texto: "Con ejercicios y sus soluciones." },
    { tipo: "marca ancha", etiqueta: "Exámenes", valor: "—", texto: "Próximamente, cuando esté el banco de preguntas." }
  ]);
})();
