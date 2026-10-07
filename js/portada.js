/* Portada: textos de datos/sitio.js y una tarjeta grande por materia */
(function () {
  const { esc, ic } = DS;

  document.getElementById("etiqueta").textContent = SITIO.etiqueta;
  document.getElementById("titulo").textContent = SITIO.titulo;
  document.getElementById("subtitulo").textContent = SITIO.subtitulo;

  // Datos que se calculan a partir del contenido de cada materia (si está cargado)
  function detalles(m) {
    if (m.proximamente) return [];
    if (m.id === "matematicas" && typeof MODULOS !== "undefined") {
      const n = Object.keys(PREGUNTAS).reduce((t, k) => t + PREGUNTAS[k].length, 0);
      return [MODULOS.length + " temas en PDF", n + " preguntas de examen"];
    }
    return [];
  }

  document.getElementById("materias").innerHTML = SITIO.materias.map(m => {
    const meta = detalles(m).map(t => "<span>" + ic("i-check") + esc(t) + "</span>").join("");
    const estado = m.proximamente ? '<span class="ds-badge ds-badge--review">Próximamente</span>' : "";
    return '<a class="ds-card ds-card--link ds-card--l materia" href="' + esc(m.id) + '/index.html">' +
      '<span class="materia__icono">' + ic(m.icono, "ds-icon--lg") + "</span>" +
      '<div class="materia__texto">' + estado +
      "<h2>" + esc(m.titulo) + "</h2><p>" + esc(m.resumen) + "</p></div>" +
      (meta ? '<div class="ds-card__meta">' + meta + "</div>" : "") +
      '<span class="materia__entrar">' + (m.proximamente ? "Ver" : "Entrar") + " " + ic("i-arrow-right", "ds-icon--sm") + "</span></a>";
  }).join("");
})();
