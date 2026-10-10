/* Tarjetas de cifras (componente .ds-stat del design system).
   DS.cifras("id-del-contenedor", [ { tipo: "grande marca" | "oscura" | "", etiqueta, valor, unidad, texto, barra (0-100) }, ... ]) */
(function () {
  const { esc } = DS;
  DS.cifras = function (id, lista) {
    document.getElementById(id).innerHTML = lista.map(c => {
      const tipos = (c.tipo || "").split(" ").filter(Boolean).map(t => " ds-stat--" + t).join("");
      return '<article class="ds-stat' + tipos + '">' +
        '<span class="ds-stat__etiqueta">' + esc(c.etiqueta) + "</span>" +
        '<div class="ds-stat__valor"><span>' + esc(c.valor) + "</span>" + (c.unidad ? '<span class="ds-stat__unidad">' + esc(c.unidad) + "</span>" : "") + "</div>" +
        (c.texto ? '<p class="ds-stat__texto">' + esc(c.texto) + "</p>" : "") +
        (c.barra != null ? '<div class="ds-stat__barra" style="--p:' + Number(c.barra) + '"><i></i></div>' : "") +
        "</article>";
    }).join("");
  };
})();
