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
})();
