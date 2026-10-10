/* =====================================================================
   PARTES COMUNES A TODAS LAS PÁGINAS: cabecera, pie, selector de tema
   y menú del móvil. Necesita datos/sitio.js cargado antes.
   ===================================================================== */
(function () {
  const body = document.body;
  const raiz = body.getAttribute("data-raiz") || "";        // ruta hasta la carpeta principal ("" o "../")
  const materiaId = body.getAttribute("data-materia") || ""; // materia en la que estamos ("" en la portada)

  function esc(s) {
    return String(s).replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  }
  function ic(id, clase) {
    return '<svg class="ds-icon' + (clase ? " " + clase : "") + '" aria-hidden="true" focusable="false"><use href="#' + id + '"/></svg>';
  }
  window.DS = { esc: esc, ic: ic };

  // Menú principal: Inicio + una entrada por materia
  const PRINCIPAL = [{ texto: "Inicio", href: raiz + "index.html", actual: materiaId === "" }]
    .concat(SITIO.materias.map(m => ({ texto: m.titulo, href: raiz + m.id + "/index.html", actual: m.id === materiaId })));

  function logo() {
    return '<a class="ds-logo" href="' + raiz + 'index.html" aria-label="' + esc(SITIO.marca) + '"><span class="ds-logo__mark">' + ic("i-sigma") +
      '</span><span class="ds-logo__text">' + esc(SITIO.marca) + "</span></a>";
  }

  function pintarCabecera() {
    const nodo = document.getElementById("cabecera");
    if (!nodo) return;
    const enlaces = PRINCIPAL.map(p =>
      '<li><a href="' + p.href + '"' + (p.actual ? ' aria-current="page"' : "") + ">" + esc(p.texto) + "</a></li>").join("");
    nodo.outerHTML =
      '<header class="ds-navbar"><div class="ds-container ds-navbar__inner">' + logo() +
      '<ul class="ds-navbar__links">' + enlaces + "</ul>" +
      '<div class="ds-navbar__actions">' +
      '<div class="ds-theme-switch" role="group" aria-label="Tema de color">' +
      '<button type="button" data-theme-set="auto" aria-pressed="true">Auto</button>' +
      '<button type="button" data-theme-set="light" aria-pressed="false">' + ic("i-sun") + '<span class="ds-sr-only">Claro</span></button>' +
      '<button type="button" data-theme-set="dark" aria-pressed="false">' + ic("i-moon") + '<span class="ds-sr-only">Oscuro</span></button>' +
      "</div>" +
      '<button type="button" class="ds-btn ds-btn--ghost ds-btn--icon ds-menu-toggle" aria-expanded="false" aria-controls="menu-movil" aria-label="Abrir menú">' + ic("i-menu") + "</button>" +
      "</div></div>" +
      '<nav class="ds-mobile-menu" id="menu-movil" aria-label="Menú móvil" hidden><ul>' + enlaces + "</ul></nav></header>";
  }

  function pintarPie() {
    const nodo = document.getElementById("pie");
    if (!nodo) return;
    const enlaces = PRINCIPAL.map(p => '<li><a href="' + p.href + '">' + esc(p.texto) + "</a></li>").join("");
    nodo.outerHTML =
      '<footer class="ds-footer"><div class="ds-container"><div class="ds-footer__grid">' +
      "<div>" + logo() + '<p style="margin-top:var(--space-3)">' + esc(SITIO.etiqueta) + "</p></div>" +
      "<div><h2>Web</h2><ul>" + enlaces + "</ul></div>" +
      '<div><h2>Contacto</h2><ul><li><a href="mailto:' + esc(SITIO.email) + '">' + esc(SITIO.email) + "</a></li></ul></div>" +
      '</div><p class="ds-footer__legal">' + esc(SITIO.actualizacion) + "</p></div></footer>";
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
    const menu = document.getElementById("menu-movil");
    if (!toggle || !menu) return;
    toggle.addEventListener("click", () => {
      const abrir = menu.hidden;
      menu.hidden = !abrir;
      toggle.setAttribute("aria-expanded", String(abrir));
    });
  }

  pintarCabecera();
  pintarPie();
  iniciarTema();
  iniciarMenuMovil();
})();
