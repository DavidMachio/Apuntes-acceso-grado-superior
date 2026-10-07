/* Visor de un tema: ?n=3 muestra el PDF del tema 3 con botón de descarga y enlaces al tema anterior y siguiente */
(function () {
  const { esc, ic } = DS;
  const params = new URLSearchParams(location.search);
  let num = parseInt(params.get("n"), 10);
  if (!(num >= 1 && num <= MODULOS.length)) {
    document.getElementById("titulo").textContent = "No encontramos ese tema";
    document.getElementById("resumen").innerHTML = 'Vuelve al <a href="temario.html">temario</a> y elige uno de la lista.';
    document.title = "Tema no encontrado · " + SITIO.marca;
    return;
  }
  const m = MODULOS[num - 1];
  let actual = Math.min(Math.max(parseInt(params.get("pdf"), 10) || 1, 1), m.pdfs.length) - 1;
  const nPreguntas = (typeof PREGUNTAS !== "undefined" && PREGUNTAS[num]) ? PREGUNTAS[num].length : 0;

  document.title = m.titulo + " · " + CURSO.materia + " · " + SITIO.marca;
  document.getElementById("migas-tema").textContent = "Tema " + num;
  document.getElementById("etiqueta").textContent = "Tema " + num + " de " + MODULOS.length;
  document.getElementById("titulo").textContent = m.titulo;
  document.getElementById("resumen").textContent = m.resumen;

  function pintar() {
    const p = m.pdfs[actual];
    document.getElementById("acciones").innerHTML =
      '<a class="ds-btn" href="' + esc(p.archivo) + '" download>' + ic("i-download", "ds-icon--sm") + "Descargar PDF</a>" +
      '<a class="ds-btn ds-btn--secondary" href="' + esc(p.archivo) + '" target="_blank" rel="noopener">' + ic("i-external-link", "ds-icon--sm") + "Abrir en otra pestaña</a>" +
      (nPreguntas > 0 ? '<a class="ds-btn ds-btn--ghost" href="examen.html?modulo=' + num + '">' + ic("i-file-text", "ds-icon--sm") + "Generar examen de este tema</a>" : "");

    document.getElementById("selector").innerHTML = m.pdfs.length > 1
      ? '<div class="ds-tabs" role="tablist" style="margin-bottom:var(--space-4)">' + m.pdfs.map((q, i) =>
        '<button class="ds-tab" role="tab" type="button" data-i="' + i + '" aria-selected="' + (i === actual) + '">' + esc(q.nombre) + "</button>").join("") + "</div>"
      : "";

    Visor.abrir(document.getElementById("visor"), { archivo: p.archivo, nombre: p.nombre });
  }

  document.getElementById("selector").addEventListener("click", e => {
    const b = e.target.closest("[data-i]");
    if (!b) return;
    actual = parseInt(b.getAttribute("data-i"), 10);
    pintar();
  });

  const ant = MODULOS[num - 2], sig = MODULOS[num];
  document.getElementById("vecinos").innerHTML =
    (ant ? '<a class="ds-btn ds-btn--ghost" href="tema.html?n=' + (num - 1) + '">' + ic("i-arrow-left", "ds-icon--sm") + "Tema " + (num - 1) + ": " + esc(ant.titulo) + "</a>" : "<span></span>") +
    (sig ? '<a class="ds-btn ds-btn--ghost" href="tema.html?n=' + (num + 1) + '">Tema ' + (num + 1) + ": " + esc(sig.titulo) + ic("i-arrow-right", "ds-icon--sm") + "</a>" : "");

  pintar();
})();
