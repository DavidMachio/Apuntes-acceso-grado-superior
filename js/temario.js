/* Página de temario: temas con sus PDFs y acceso al examen de cada tema */
(function () {
  const { esc, ic } = DS;

  document.title = "Temario: " + CURSO.marca;
  document.getElementById("intro").textContent =
    "Descarga los apuntes de cada tema o genera un examen con sus preguntas.";

  const indice = document.getElementById("indice");
  indice.innerHTML = '<div class="ds-sidebar__title">Temas</div>' + MODULOS.map((m, i) =>
    '<a href="#modulo-' + (i + 1) + '">' + ic("i-book-open") + esc(m.titulo) + "</a>").join("");

  document.getElementById("lista-modulos").innerHTML = MODULOS.map((m, i) => {
    const num = i + 1;
    const id = "modulo-" + num;
    const nPreguntas = (typeof PREGUNTAS !== "undefined" && PREGUNTAS[num]) ? PREGUNTAS[num].length : 0;

    const pdfs = m.pdfs.map(p =>
      '<div class="ds-pdf pdf-fila"><div class="ds-pdf__ico">PDF</div>' +
      '<div class="pdf-fila__texto"><b>' + esc(p.nombre) + "</b>" + (p.detalle ? '<div class="ds-caption">' + esc(p.detalle) + "</div>" : "") + "</div>" +
      '<a class="ds-btn ds-btn--secondary ds-btn--sm" href="' + esc(p.archivo) + '" download aria-label="Descargar ' + esc(p.nombre) + ' (PDF)">' +
      ic("i-download", "ds-icon--sm") + "Descargar</a></div>").join("");

    const examen = nPreguntas > 0
      ? '<div class="pdf-fila ds-row ds-row--between"><span class="ds-small ds-muted">' + nPreguntas +
        (nPreguntas === 1 ? " pregunta disponible" : " preguntas disponibles") + " para examen</span>" +
        '<a class="ds-btn ds-btn--ghost ds-btn--sm" href="examen.html?modulo=' + num + '">' + ic("i-file-text", "ds-icon--sm") + "Generar examen de este tema</a></div>"
      : "";

    return '<section class="ds-card modulo" id="' + id + '" aria-labelledby="' + id + '-titulo">' +
      '<div class="ds-row ds-row--between"><div><span class="ds-label">Tema ' + num + "</span>" +
      '<h2 class="modulo__titulo" id="' + id + '-titulo">' + esc(m.titulo) + "</h2></div>" +
      '<span class="ds-badge">' + ic("i-file-text") + esc(m.paginas) + "</span></div>" +
      "<p>" + esc(m.resumen) + "</p>" + pdfs + examen + "</section>";
  }).join("");

  // Marca en el menú lateral el tema que se está leyendo
  if ("IntersectionObserver" in window) {
    const enlaces = document.querySelectorAll("#indice a");
    const obs = new IntersectionObserver(entradas => {
      entradas.forEach(e => {
        if (!e.isIntersecting) return;
        enlaces.forEach(a => a.removeAttribute("aria-current"));
        const activo = document.querySelector('#indice a[href="#' + e.target.id + '"]');
        if (activo) activo.setAttribute("aria-current", "page");
      });
    }, { rootMargin: "-20% 0px -70% 0px" });
    document.querySelectorAll(".modulo").forEach(s => obs.observe(s));
  }
})();
