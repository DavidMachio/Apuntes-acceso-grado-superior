/* =====================================================================
   CONTENIDO DEL PROGRAMA — es lo único que tienes que editar.
   Para añadir un módulo, copia uno de los bloques de "modulos" y cambia
   sus textos. Los PDFs se guardan en la carpeta /pdfs y se enlazan aquí.
   ===================================================================== */
const PROGRAMA = {
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
function crear(etiqueta, clase, texto) {
  const nodo = document.createElement(etiqueta);
  if (clase) nodo.className = clase;
  if (texto !== undefined) nodo.textContent = texto;
  return nodo;
}

function pintar() {
  document.getElementById("titulo").textContent = PROGRAMA.titulo;
  document.getElementById("subtitulo").textContent = PROGRAMA.subtitulo;
  document.getElementById("pie").textContent = PROGRAMA.pie;
  document.title = PROGRAMA.titulo;

  const descripcion = document.getElementById("descripcion");
  PROGRAMA.descripcion.forEach(p => descripcion.appendChild(crear("p", "", p)));

  const ficha = document.getElementById("ficha");
  PROGRAMA.ficha.forEach(dato => {
    const fila = crear("div", "ficha__fila");
    fila.appendChild(crear("dt", "", dato.etiqueta));
    fila.appendChild(crear("dd", "", dato.valor));
    ficha.appendChild(fila);
  });

  const indice = document.getElementById("indice");
  const modulos = document.getElementById("modulos");

  PROGRAMA.modulos.forEach((m, i) => {
    const id = "modulo-" + (i + 1);

    // Entrada del índice lateral
    const li = crear("li");
    const enlace = crear("a", "", m.titulo);
    enlace.href = "#" + id;
    li.appendChild(enlace);
    indice.appendChild(li);

    // Bloque del módulo
    const sec = crear("section", "modulo");
    sec.id = id;
    sec.setAttribute("aria-labelledby", id + "-titulo");

    const numero = crear("p", "modulo__numero", String(i + 1));
    numero.setAttribute("aria-hidden", "true");

    const info = crear("div", "modulo__info");
    const h3 = crear("h3", "", m.titulo);
    h3.id = id + "-titulo";
    info.appendChild(h3);
    info.appendChild(crear("p", "modulo__resumen", m.resumen));
    info.appendChild(crear("p", "modulo__horas", "Duración: " + m.horas));

    const materiales = crear("div", "modulo__materiales");
    const h4 = crear("h4", "", "Materiales");
    materiales.appendChild(h4);
    const lista = crear("ul", "pdfs");
    m.pdfs.forEach(pdf => {
      const item = crear("li");
      const a = crear("a", "pdf");
      a.href = pdf.archivo;
      a.target = "_blank";
      a.rel = "noopener";
      a.appendChild(crear("span", "pdf__marca", "PDF"));
      const textos = crear("span", "pdf__textos");
      textos.appendChild(crear("span", "pdf__nombre", pdf.nombre));
      if (pdf.detalle) textos.appendChild(crear("span", "pdf__detalle", pdf.detalle));
      a.appendChild(textos);
      item.appendChild(a);
      lista.appendChild(item);
    });
    materiales.appendChild(lista);

    sec.append(numero, info, materiales);
    modulos.appendChild(sec);
  });

  marcarModuloActivo();
}

/* Resalta en el índice el módulo que se está leyendo */
function marcarModuloActivo() {
  if (!("IntersectionObserver" in window)) return;
  const enlaces = document.querySelectorAll(".indice a");
  const observador = new IntersectionObserver(entradas => {
    entradas.forEach(e => {
      if (e.isIntersecting) {
        enlaces.forEach(a => a.removeAttribute("aria-current"));
        const activo = document.querySelector('.indice a[href="#' + e.target.id + '"]');
        if (activo) activo.setAttribute("aria-current", "true");
      }
    });
  }, { rootMargin: "-20% 0px -70% 0px" });
  document.querySelectorAll(".modulo").forEach(s => observador.observe(s));
}

pintar();
