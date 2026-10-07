/* =====================================================================
   TEMARIO — un bloque por módulo, con sus PDFs.
   · El número de módulo es su posición en la lista (1, 2, 3…).
   · Las preguntas del examen de cada módulo se escriben en datos/preguntas.js
     con ese mismo número.
   · Los PDFs se guardan en la carpeta /pdfs y se enlazan aquí.
   (Contenido de ejemplo: sustitúyelo por el tuyo.)
   ===================================================================== */
const MODULOS = [
  {
    titulo: "Números y operaciones",
    resumen: "Fracciones, potencias, raíces y porcentajes.",
    horas: "6 h",
    pdfs: [
      { nombre: "Apuntes del módulo 1", detalle: "Teoría y ejemplos", archivo: "pdfs/modulo-1-apuntes.pdf" }
    ]
  },
  {
    titulo: "Álgebra",
    resumen: "Ecuaciones, sistemas e inecuaciones.",
    horas: "8 h",
    pdfs: [
      { nombre: "Apuntes del módulo 2", detalle: "Teoría y ejemplos", archivo: "pdfs/modulo-2-apuntes.pdf" }
    ]
  },
  {
    titulo: "Funciones",
    resumen: "Gráficas, pendiente y funciones lineales y cuadráticas.",
    horas: "7 h",
    pdfs: [
      { nombre: "Apuntes del módulo 3", detalle: "Teoría y ejemplos", archivo: "pdfs/modulo-3-apuntes.pdf" }
    ]
  },
  {
    titulo: "Geometría",
    resumen: "Áreas, volúmenes, semejanza y teorema de Pitágoras.",
    horas: "6 h",
    pdfs: [
      { nombre: "Apuntes del módulo 4", detalle: "Teoría y ejemplos", archivo: "pdfs/modulo-4-apuntes.pdf" }
    ]
  },
  {
    titulo: "Estadística y probabilidad",
    resumen: "Media, mediana, moda y probabilidad básica.",
    horas: "5 h",
    pdfs: [
      { nombre: "Apuntes del módulo 5", detalle: "Teoría y ejemplos", archivo: "pdfs/modulo-5-apuntes.pdf" }
    ]
  }
];
