/* Página de un tema: ?n=3 muestra las presentaciones (PDF) del tema 3 y los enlaces al tema anterior y siguiente */
(function () {
  const { esc, ic } = DS;
  const num = parseInt(new URLSearchParams(location.search).get("n"), 10);
  if (!(num >= 1 && num <= MODULOS.length)) {
    document.getElementById("titulo").textContent = "No encontramos ese tema";
    document.getElementById("resumen").innerHTML = 'Vuelve a <a href="index.html">Matemáticas</a> y elige uno de la lista.';
    document.title = "Tema no encontrado · " + SITIO.marca;
    document.getElementById("h-pres").closest("section").hidden = true;
    return;
  }
  const m = MODULOS[num - 1];
  const nPreguntas = (typeof PREGUNTAS !== "undefined" && PREGUNTAS[num]) ? PREGUNTAS[num].length : 0;

  document.title = m.titulo + " · " + CURSO.materia + " · " + SITIO.marca;
  document.getElementById("migas-tema").textContent = m.titulo;
  document.getElementById("titulo").textContent = m.titulo;
  document.getElementById("resumen").textContent = m.resumen;

  if (nPreguntas > 0) {
    document.getElementById("acciones").innerHTML =
      '<a class="ds-btn ds-btn--secondary" href="examen.html?modulo=' + num + '">' + ic("i-file-text") + "Generar examen de este tema</a>";
  }

  document.getElementById("presentaciones").innerHTML = m.pdfs.map((p, i) => {
    const url = "presentacion.html?n=" + num + "&pdf=" + (i + 1);
    return '<li><div><h3 class="ds-index__title"><a href="' + url + '">' + esc(p.nombre) + "</a></h3>" +
      (p.detalle ? "<p>" + esc(p.detalle) + "</p>" : "") + "</div>" +
      '<span class="ds-row"><a class="ds-btn ds-btn--secondary ds-btn--sm" href="' + url + '" aria-label="Ver ' + esc(p.nombre) + '">Ver</a>' +
      '<a class="ds-btn ds-btn--ghost ds-btn--icon ds-btn--sm" href="' + esc(p.archivo) + '" download aria-label="Descargar ' + esc(p.nombre) + ' (PDF)">' + ic("i-download") + "</a></span></li>";
  }).join("");

  const ant = MODULOS[num - 2], sig = MODULOS[num];
  document.getElementById("vecinos").innerHTML =
    (ant ? '<a class="ds-link-arrow" href="tema.html?n=' + (num - 1) + '">' + ic("i-arrow-left") + esc(ant.titulo) + "</a>" : "<span></span>") +
    (sig ? '<a class="ds-link-arrow" href="tema.html?n=' + (num + 1) + '">' + esc(sig.titulo) + ic("i-arrow-right") + "</a>" : "");
})();
