/* =====================================================================
   CONTENIDO DEL PROGRAMA — es lo único que tienes que editar.
   Para añadir un módulo, copia uno de los bloques de "modulos" y cambia
   sus textos. Los PDFs se guardan en la carpeta /pdfs y se enlazan aquí.
   ===================================================================== */
const PROGRAMA = {
  marca: "Programa formativo",             // nombre corto: aparece arriba a la izquierda y en el pie
  titulo: "Nombre del programa formativo",
  subtitulo: "Una frase que explique qué aprenderá la persona que lo complete.",

  descripcion: [
    "Escribe aquí la presentación del programa: a quién va dirigido, qué objetivos tiene y cómo se organiza.",
    "Puedes añadir tantos párrafos como necesites; cada texto entre comillas es un párrafo."
  ],

  ficha: [
    { etiqueta: "Duración",     valor: "40 horas" },
    { etiqueta: "Modalidad",    valor: "Presencial / Online" },
    { etiqueta: "Dirigido a",   valor: "Equipos de la empresa cliente" },
    { etiqueta: "Certificado",  valor: "Sí, al finalizar" }
  ],

  modulos: [
    {
      titulo: "Introducción y objetivos",
      resumen: "Presentación del programa, calendario y herramientas que se usarán.",
      horas: "4 h",
      pdfs: [
        { nombre: "Guía del alumno",        detalle: "Calendario y normas",  archivo: "pdfs/modulo-1-guia-del-alumno.pdf" },
        { nombre: "Presentación del módulo", detalle: "Diapositivas",         archivo: "pdfs/modulo-1-presentacion.pdf" }
      ]
    },
    {
      titulo: "Contenidos principales",
      resumen: "Desarrollo de los temas centrales del programa con ejemplos prácticos.",
      horas: "28 h",
      pdfs: [
        { nombre: "Manual del módulo", detalle: "Teoría y ejemplos", archivo: "pdfs/modulo-2-manual.pdf" }
      ]
    },
    {
      titulo: "Práctica y evaluación",
      resumen: "Ejercicios de aplicación y prueba final para obtener el certificado.",
      horas: "8 h",
      pdfs: [
        { nombre: "Cuaderno de ejercicios", detalle: "Para resolver en clase", archivo: "pdfs/modulo-3-ejercicios.pdf" },
        { nombre: "Criterios de evaluación", detalle: "Cómo se puntúa",        archivo: "pdfs/modulo-3-criterios.pdf" }
      ]
    }
  ],

  pie: "Última actualización: octubre de 2026. Contacto: tu-correo@empresa.com"
};

/* ---------------------------------------------------------------------
   A partir de aquí no hace falta tocar nada.
   --------------------------------------------------------------------- */
const SVG_NS = "http://www.w3.org/2000/svg";

function crear(etiqueta, clase, texto) {
  const nodo = document.createElement(etiqueta);
  if (clase) nodo.className = clase;
  if (texto !== undefined) nodo.textContent = texto;
  return nodo;
}

// Icono del sprite incluido en index.html (por ejemplo "i-download")
function icono(id, clase) {
  const svg = document.createElementNS(SVG_NS, "svg");
  svg.setAttribute("class", "ds-icon" + (clase ? " " + clase : ""));
  svg.setAttribute("aria-hidden", "true");
  svg.setAttribute("focusable", "false");
  const uso = document.createElementNS(SVG_NS, "use");
  uso.setAttribute("href", "#" + id);
  svg.appendChild(uso);
  return svg;
}

function pintar() {
  const marca = PROGRAMA.marca || PROGRAMA.titulo;
  document.title = PROGRAMA.titulo;
  document.querySelectorAll("[data-marca]").forEach(n => { n.textContent = marca; });
  document.getElementById("titulo").textContent = PROGRAMA.titulo;
  document.getElementById("subtitulo").textContent = PROGRAMA.subtitulo;
  document.getElementById("pie").textContent = PROGRAMA.pie;

  const descripcion = document.getElementById("descripcion");
  PROGRAMA.descripcion.forEach(p => descripcion.appendChild(crear("p", "", p)));

  const ficha = document.getElementById("ficha");
  PROGRAMA.ficha.forEach(dato => {
    const item = crear("div", "ficha__item");
    item.appendChild(crear("dt", "", dato.etiqueta));
    item.appendChild(crear("dd", "", dato.valor));
    ficha.appendChild(item);
  });

  const indice = document.getElementById("indice");
  indice.appendChild(crear("div", "ds-sidebar__title", "Módulos"));
  const lista = document.getElementById("lista-modulos");

  PROGRAMA.modulos.forEach((m, i) => {
    const id = "modulo-" + (i + 1);

    // Enlace del menú lateral
    const enlace = crear("a");
    enlace.href = "#" + id;
    enlace.appendChild(icono("i-book-open"));
    enlace.appendChild(document.createTextNode(m.titulo));
    indice.appendChild(enlace);

    // Tarjeta del módulo
    const tarjeta = crear("section", "ds-card modulo");
    tarjeta.id = id;
    tarjeta.setAttribute("aria-labelledby", id + "-titulo");

    const cabecera = crear("div", "ds-row ds-row--between");
    const izquierda = crear("div");
    izquierda.appendChild(crear("span", "ds-label", "Módulo " + (i + 1)));
    const h2 = crear("h2", "modulo__titulo", m.titulo);
    h2.id = id + "-titulo";
    izquierda.appendChild(h2);
    cabecera.appendChild(izquierda);

    const duracion = crear("span", "ds-badge");
    duracion.appendChild(icono("i-clock"));
    duracion.appendChild(document.createTextNode(m.horas));
    cabecera.appendChild(duracion);

    tarjeta.appendChild(cabecera);
    tarjeta.appendChild(crear("p", "", m.resumen));

    m.pdfs.forEach(pdf => {
      const fila = crear("div", "ds-pdf pdf-fila");
      fila.appendChild(crear("div", "ds-pdf__ico", "PDF"));

      const textos = crear("div", "pdf-fila__texto");
      textos.appendChild(crear("b", "", pdf.nombre));
      if (pdf.detalle) textos.appendChild(crear("div", "ds-caption", pdf.detalle));
      fila.appendChild(textos);

      const boton = crear("a", "ds-btn ds-btn--secondary ds-btn--sm");
      boton.href = pdf.archivo;
      boton.setAttribute("download", "");
      boton.setAttribute("aria-label", "Descargar " + pdf.nombre + " (PDF)");
      boton.appendChild(icono("i-download", "ds-icon--sm"));
      boton.appendChild(document.createTextNode("Descargar"));
      fila.appendChild(boton);

      tarjeta.appendChild(fila);
    });

    lista.appendChild(tarjeta);
  });

  marcarModuloActivo();
}

/* Resalta en el menú lateral el módulo que se está leyendo */
function marcarModuloActivo() {
  if (!("IntersectionObserver" in window)) return;
  const enlaces = document.querySelectorAll("#indice a");
  const observador = new IntersectionObserver(entradas => {
    entradas.forEach(e => {
      if (e.isIntersecting) {
        enlaces.forEach(a => a.removeAttribute("aria-current"));
        const activo = document.querySelector('#indice a[href="#' + e.target.id + '"]');
        if (activo) activo.setAttribute("aria-current", "page");
      }
    });
  }, { rootMargin: "-20% 0px -70% 0px" });
  document.querySelectorAll(".modulo").forEach(s => observador.observe(s));
}

/* Selector de tema (Auto / Claro / Oscuro) y menú del móvil */
function iniciarInterfaz() {
  const raiz = document.documentElement;
  const botones = document.querySelectorAll("[data-theme-set]");

  function aplicarTema(t) {
    const modo = (t === "light" || t === "dark") ? t : "auto";
    if (modo === "auto") raiz.removeAttribute("data-theme");
    else raiz.setAttribute("data-theme", modo);
    botones.forEach(b => b.setAttribute("aria-pressed", String(b.getAttribute("data-theme-set") === modo)));
  }

  let guardado = "auto";
  try { guardado = localStorage.getItem("theme") || "auto"; } catch (e) {}
  aplicarTema(guardado);

  botones.forEach(b => b.addEventListener("click", () => {
    const t = b.getAttribute("data-theme-set");
    aplicarTema(t);
    try { localStorage.setItem("theme", t); } catch (e) {}
  }));

  const toggle = document.querySelector(".ds-menu-toggle");
  const menu = document.querySelector(".ds-mobile-menu");
  if (toggle && menu) {
    toggle.addEventListener("click", () => {
      const abierto = menu.getAttribute("data-open") === "true";
      menu.setAttribute("data-open", String(!abierto));
      toggle.setAttribute("aria-expanded", String(!abierto));
    });
    menu.querySelectorAll("a").forEach(a => a.addEventListener("click", () => {
      menu.setAttribute("data-open", "false");
      toggle.setAttribute("aria-expanded", "false");
    }));
  }
}

pintar();
iniciarInterfaz();
