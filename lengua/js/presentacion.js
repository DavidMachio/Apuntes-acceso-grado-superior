/* Visor de una presentación: ?n=3&pdf=1 abre el PDF 1 del tema 3, con descarga y enlaces a la anterior y la siguiente del mismo tema */
(function () {
  const { esc, ic } = DS;
  const params = new URLSearchParams(location.search);
  const num = parseInt(params.get("n"), 10);
  const m = MODULOS_LENGUA[num - 1];
  const idx = m ? parseInt(params.get("pdf"), 10) || 1 : 0;
  if (!m || !(idx >= 1 && idx <= m.pdfs.length)) {
    document.getElementById("titulo").textContent = "No encontramos esa presentación";
    document.getElementById("migas-tema").hidden = true;
    document.getElementById("migas-pres").hidden = true;
    document.getElementById("visor").innerHTML = '<p>Vuelve a <a href="index.html">Lengua</a> y elige un tema.</p>';
    document.title = "Presentación no encontrada · " + SITIO.marca;
    return;
  }
  const p = m.pdfs[idx - 1];
  const urlTema = "tema.html?n=" + num;

  document.title = p.nombre + " · " + m.titulo + " · " + SITIO.marca;
  document.querySelector("#migas-tema a").setAttribute("href", urlTema);
  document.querySelector("#migas-tema a").textContent = m.titulo;
  document.getElementById("migas-pres").textContent = p.nombre;
  document.getElementById("titulo").textContent = p.nombre;

  document.getElementById("acciones").innerHTML =
    '<a class="ds-btn" href="' + esc(p.archivo) + '" download>' + ic("i-download") + "Descargar PDF</a>" +
    '<a class="ds-btn ds-btn--secondary" href="' + esc(p.archivo) + '" target="_blank" rel="noopener">' + ic("i-external-link") + "Abrir en otra pestaña</a>";

  const ant = m.pdfs[idx - 2], sig = m.pdfs[idx];
  document.getElementById("vecinos").innerHTML =
    (ant ? '<a class="ds-link-arrow" href="presentacion.html?n=' + num + "&pdf=" + (idx - 1) + '">' + ic("i-arrow-left") + esc(ant.nombre) + "</a>" : '<a class="ds-link-arrow" href="' + urlTema + '">' + ic("i-arrow-left") + "Volver al tema</a>") +
    (sig ? '<a class="ds-link-arrow" href="presentacion.html?n=' + num + "&pdf=" + (idx + 1) + '">' + esc(sig.nombre) + ic("i-arrow-right") + "</a>" : "");

  Visor.abrir(document.getElementById("visor"), { archivo: p.archivo, nombre: p.nombre });
})();
