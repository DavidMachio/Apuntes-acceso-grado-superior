/* Portada: título y una tarjeta grande por materia (datos/sitio.js). Cada tarjeta usa el color de su materia. */
(function () {
  const { esc, ic } = DS;

  document.getElementById("titulo").textContent = SITIO.titulo;
  document.getElementById("subtitulo").textContent = SITIO.subtitulo;

  document.getElementById("materias").innerHTML = SITIO.materias.map(m => {
    const estado = m.proximamente ? '<span class="ds-badge ds-badge--accent">Próximamente</span>' : "";
    return '<article class="ds-card ds-card--dark ds-card--link materia" data-variante="' + esc(m.id) + '">' +
      '<div class="materia__cabecera"><span class="ds-logo__mark materia__icono">' + ic(m.icono) + "</span>" +
      '<h2 class="ds-card__title"><a href="' + esc(m.id) + '/index.html">' + esc(m.titulo) + "</a></h2></div>" + estado +
      "<p>" + esc(m.resumen) + "</p>" +
      '<span class="ds-link-arrow">Entrar ' + ic("i-arrow-right") + "</span></article>";
  }).join("");

  /* Cifras: salen de los datos de Matemáticas (temario y banco de preguntas), así se actualizan solas */
  const disponibles = SITIO.materias.filter(m => !m.proximamente).length;
  const preguntas = Object.values(PREGUNTAS).reduce((n, lista) => n + lista.length, 0);
  const diapositivas = MODULOS.reduce((n, m) => n + (parseInt(m.paginas, 10) || 0), 0);
  DS.cifras("cifras", [
    { tipo: "grande marca", etiqueta: "Asignaturas", valor: String(SITIO.materias.length), texto: "Matemáticas ya disponible; Lengua, muy pronto.", barra: Math.round(100 * disponibles / SITIO.materias.length) },
    { tipo: "oscura", etiqueta: "Lecciones", valor: String(MODULOS.length), unidad: "temas", texto: "Cada uno con su presentación en PDF." },
    { etiqueta: "Banco de preguntas", valor: String(preguntas), unidad: "preguntas", texto: "Con solución explicada." },
    { etiqueta: "Presentaciones", valor: String(diapositivas), unidad: "diapositivas", texto: "Para estudiar en pantalla o imprimir." },
    { tipo: "marca", etiqueta: "Exámenes", valor: "∞", texto: "Se generan a medida, con hoja de soluciones." }
  ]);
})();
