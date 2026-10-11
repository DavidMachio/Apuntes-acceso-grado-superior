/* Página de la materia: lista de temas a partir de datos/curso.js y datos/temario.js */
(function () {
  const { esc } = DS;

  document.title = CURSO.materia + " · " + SITIO.marca;
  document.getElementById("titulo").textContent = CURSO.materia;
  document.getElementById("subtitulo").textContent = CURSO.subtitulo;

  document.getElementById("temas").innerHTML = MODULOS.map((m, i) => {
    const url = "tema.html?n=" + (i + 1);
    return '<li><div><h3 class="ds-index__title"><a href="' + url + '">' + esc(m.titulo) + "</a></h3><p>" + esc(m.resumen) + "</p></div>" +
      '<a class="ds-btn ds-btn--secondary ds-btn--sm" href="' + url + '" aria-label="Abrir el tema ' + esc(m.titulo) + '">Abrir</a></li>';
  }).join("");

  const preguntas = Object.values(PREGUNTAS).reduce((n, lista) => n + lista.length, 0);
  const diapositivas = MODULOS.reduce((n, m) => n + (parseInt(m.paginas, 10) || 0), 0);
  DS.cifras("cifras", [
    { tipo: "grande marca", etiqueta: "Temario", valor: String(MODULOS.length), unidad: "temas", texto: MODULOS[0].titulo + ", " + MODULOS[1].titulo.toLowerCase() + " y más, cada uno con su presentación en PDF." },
    { tipo: "oscura", etiqueta: "Banco de preguntas", valor: String(preguntas), unidad: "preguntas", texto: "Con solución explicada." },
    { etiqueta: "Presentaciones", valor: String(diapositivas), unidad: "diapositivas", texto: "Con ejemplos y ejercicios." },
    { tipo: "marca ancha", etiqueta: "Exámenes", valor: "∞", texto: "A medida, con hoja de soluciones aparte." }
  ]);
})();
