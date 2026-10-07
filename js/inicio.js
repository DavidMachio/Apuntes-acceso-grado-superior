/* Página de inicio: rellena los textos a partir de datos/curso.js y datos/temario.js */
(function () {
  const { esc, ic } = DS;

  document.title = CURSO.marca;
  document.getElementById("etiqueta").textContent = CURSO.etiqueta;
  document.getElementById("titulo").textContent = CURSO.titulo;
  document.getElementById("subtitulo").textContent = CURSO.subtitulo;

  document.getElementById("descripcion").innerHTML =
    CURSO.descripcion.map(p => "<p>" + esc(p) + "</p>").join("");

  document.getElementById("ficha").innerHTML = CURSO.ficha.map(d =>
    '<div class="ficha__item"><dt>' + esc(d.etiqueta) + "</dt><dd>" + esc(d.valor) + "</dd></div>").join("");

  document.getElementById("modulos").innerHTML = MODULOS.map((m, i) => {
    const pdfs = m.pdfs.length + (m.pdfs.length === 1 ? " PDF" : " PDFs");
    return '<a class="ds-card ds-card--link ds-card--hl" href="temario.html#modulo-' + (i + 1) + '">' +
      '<span class="ds-label">Tema ' + (i + 1) + "</span>" +
      "<h3>" + esc(m.titulo) + "</h3><p>" + esc(m.resumen) + "</p>" +
      '<div class="ds-card__meta"><span>' + ic("i-file-text") + esc(m.paginas) + "</span><span>" + ic("i-file-text") + pdfs + "</span></div></a>";
  }).join("");
})();
