/* Portada: título y una tarjeta grande por materia (datos/sitio.js). Cada tarjeta usa el color de su materia. */
(function () {
  const { esc, ic } = DS;

  document.getElementById("titulo").textContent = SITIO.titulo;
  document.getElementById("subtitulo").textContent = SITIO.subtitulo;

  document.getElementById("materias").innerHTML = SITIO.materias.map(m => {
    const estado = m.proximamente ? '<span class="ds-badge ds-badge--accent">Próximamente</span>' : "";
    return '<article class="ds-card ds-card--dark ds-card--link materia" data-variante="' + esc(m.id) + '">' +
      '<span class="ds-logo__mark">' + ic(m.icono) + "</span>" + estado +
      '<h2 class="ds-card__title"><a href="' + esc(m.id) + '/index.html">' + esc(m.titulo) + "</a></h2>" +
      "<p>" + esc(m.resumen) + "</p>" +
      '<span class="ds-link-arrow">Entrar ' + ic("i-arrow-right") + "</span></article>";
  }).join("");
})();
