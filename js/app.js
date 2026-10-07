/* =====================================================================
   PARTES COMUNES A TODAS LAS PÁGINAS: cabecera, pie, selector de tema,
   menú del móvil y ayudas. Necesita datos/sitio.js cargado antes.
   ===================================================================== */
(function () {
  const body = document.body;
  const actual = body.getAttribute("data-pagina") || "";
  const raiz = body.getAttribute("data-raiz") || "";        // ruta hasta la carpeta principal ("" o "../")
  const materiaId = body.getAttribute("data-materia") || ""; // materia en la que estamos ("" en la portada)
  const materia = SITIO.materias.find(m => m.id === materiaId) || null;

  function esc(s) {
    return String(s).replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  }
  function ic(id, clase) {
    return '<svg class="ds-icon' + (clase ? " " + clase : "") + '" aria-hidden="true" focusable="false"><use href="#' + id + '"/></svg>';
  }
  window.DS = { esc: esc, ic: ic };

  // Menú principal: Inicio + una entrada por materia
  const PRINCIPAL = [{ texto: "Inicio", href: raiz + "index.html", icono: "i-home", actual: materiaId === "" }]
    .concat(SITIO.materias.map(m => ({
      texto: m.titulo, href: raiz + m.id + "/index.html", icono: m.icono, actual: m.id === materiaId
    })));
  // Pestañas de la materia actual (Resumen / Temario / Examen…)
  const PESTANAS = materia ? materia.paginas.map(p => ({
    texto: p.texto, href: p.href, actual: p.id === actual
  })) : [];

  function logo() {
    return '<a class="ds-logo" href="' + raiz + 'index.html"><span class="ds-logo__ph">' + ic("i-graduation-cap", "ds-icon--sm") +
      "</span>" + esc(SITIO.marca) + "</a>";
  }

  function pintarCabecera() {
    const nodo = document.getElementById("cabecera");
    if (!nodo) return;
    const enlaces = PRINCIPAL.map(p =>
      '<li><a href="' + p.href + '"' + (p.actual ? ' aria-current="page"' : "") + ">" + esc(p.texto) + "</a></li>").join("");
    let movil = PRINCIPAL.map(p =>
      '<a href="' + p.href + '"' + (p.actual ? ' aria-current="page"' : "") + ">" + ic(p.icono) + esc(p.texto) + "</a>").join("");
    if (PESTANAS.length) {
      movil += '<span class="ds-label menu-sub">' + esc(materia.titulo) + "</span>" + PESTANAS.map(p =>
        '<a href="' + p.href + '"' + (p.actual ? ' aria-current="page"' : "") + ">" + esc(p.texto) + "</a>").join("");
    }
    const pestanas = PESTANAS.length
      ? '<div class="subnav"><div class="ds-container"><nav class="ds-tabs" aria-label="Secciones de ' + esc(materia.titulo) + '">' +
        PESTANAS.map(p => '<a class="ds-tab"' + (p.actual ? ' aria-current="page"' : "") + ' href="' + p.href + '">' + esc(p.texto) + "</a>").join("") +
        "</nav></div></div>"
      : "";
    nodo.outerHTML =
      '<header class="ds-navbar"><div class="ds-container"><div class="ds-navbar__in">' + logo() +
      '<nav aria-label="Principal"><ul class="ds-nav">' + enlaces + "</ul></nav>" +
      '<div class="ds-navbar__actions">' +
      '<div class="ds-btn-group" role="group" aria-label="Tema de color">' +
      '<button class="ds-btn ds-btn--secondary ds-btn--sm" type="button" data-theme-set="auto" aria-pressed="true">Auto</button>' +
      '<button class="ds-btn ds-btn--secondary ds-btn--sm" type="button" data-theme-set="light" aria-pressed="false">' + ic("i-sun", "ds-icon--sm") + '<span class="ds-sr-only">Claro</span></button>' +
      '<button class="ds-btn ds-btn--secondary ds-btn--sm" type="button" data-theme-set="dark" aria-pressed="false">' + ic("i-moon", "ds-icon--sm") + '<span class="ds-sr-only">Oscuro</span></button>' +
      "</div>" +
      '<button class="ds-btn ds-btn--ghost ds-btn--icon ds-menu-toggle" type="button" aria-expanded="false" aria-label="Abrir menú">' + ic("i-menu") + "</button>" +
      "</div></div>" +
      '<nav class="ds-mobile-menu" aria-label="Menú móvil">' + movil + "</nav></div></header>" + pestanas;
  }

  function pintarPie() {
    const nodo = document.getElementById("pie");
    if (!nodo) return;
    const enlaces = PRINCIPAL.map(p => '<li><a href="' + p.href + '">' + esc(p.texto) + "</a></li>").join("");
    nodo.outerHTML =
      '<footer class="ds-footer"><div class="ds-container"><div class="ds-grid">' +
      "<div>" + logo() + '<p class="ds-small ds-muted" style="margin-top:12px">' + esc(SITIO.etiqueta) + "</p></div>" +
      "<div><h6>Web</h6><ul>" + enlaces + "</ul></div>" +
      "<div><h6>Contacto</h6><p class=\"ds-small ds-muted\">" + esc(SITIO.pie) + "</p></div>" +
      "</div></div></footer>";
  }

  function iniciarTema() {
    const raiz = document.documentElement;
    const botones = document.querySelectorAll("[data-theme-set]");

    function aplicar(t) {
      const modo = (t === "light" || t === "dark") ? t : "auto";
      if (modo === "auto") raiz.removeAttribute("data-theme");
      else raiz.setAttribute("data-theme", modo);
      botones.forEach(b => b.setAttribute("aria-pressed", String(b.getAttribute("data-theme-set") === modo)));
    }

    let guardado = "auto";
    try { guardado = localStorage.getItem("theme") || "auto"; } catch (e) {}
    aplicar(guardado);

    botones.forEach(b => b.addEventListener("click", () => {
      const t = b.getAttribute("data-theme-set");
      aplicar(t);
      try { localStorage.setItem("theme", t); } catch (e) {}
    }));

    // Al imprimir se usa siempre el modo claro (como indica el design system)
    let temaPrevio = null;
    window.addEventListener("beforeprint", () => {
      temaPrevio = raiz.getAttribute("data-theme");
      raiz.setAttribute("data-theme", "light");
    });
    window.addEventListener("afterprint", () => {
      if (temaPrevio === null) raiz.removeAttribute("data-theme");
      else raiz.setAttribute("data-theme", temaPrevio);
    });
  }

  function iniciarMenuMovil() {
    const toggle = document.querySelector(".ds-menu-toggle");
    const menu = document.querySelector(".ds-mobile-menu");
    if (!toggle || !menu) return;
    toggle.addEventListener("click", () => {
      const abierto = menu.getAttribute("data-open") === "true";
      menu.setAttribute("data-open", String(!abierto));
      toggle.setAttribute("aria-expanded", String(!abierto));
    });
  }

  pintarCabecera();
  pintarPie();
  iniciarTema();
  iniciarMenuMovil();
})();
