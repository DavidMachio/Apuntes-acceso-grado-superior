/* =====================================================================
   TEMARIO — un bloque por tema, con su PDF.
   · El número de tema es su posición en la lista (1, 2, 3…).
   · Las preguntas del examen de cada tema se escriben en datos/preguntas.js
     con ese mismo número.
   · Los PDFs se guardan en la carpeta /pdfs (los genera herramientas/generar_pdfs.py).
   ===================================================================== */
const MODULOS = [
  {
    titulo: "Porcentajes",
    resumen: "IVA, IRPF, inflación, comisiones y tasas.",
    paginas: "3 páginas",
    pdfs: [
      { nombre: "Apuntes del tema 1", detalle: "Porcentajes", archivo: "pdfs/tema-01-porcentajes.pdf" }
    ]
  },
  {
    titulo: "Cantidades iniciales y finales",
    resumen: "Aumentos, disminuciones y variaciones encadenadas.",
    paginas: "4 páginas",
    pdfs: [
      { nombre: "Apuntes del tema 2", detalle: "Cantidades iniciales y finales", archivo: "pdfs/tema-02-cantidades-iniciales-y-finales.pdf" }
    ]
  },
  {
    titulo: "Porcentaje de un total",
    resumen: "Qué porcentaje representa una cantidad del total.",
    paginas: "2 páginas",
    pdfs: [
      { nombre: "Apuntes del tema 3", detalle: "Porcentaje de un total", archivo: "pdfs/tema-03-porcentaje-de-un-total.pdf" }
    ]
  },
  {
    titulo: "Variación absoluta y porcentual",
    resumen: "Cómo cambia una cantidad entre dos momentos.",
    paginas: "2 páginas",
    pdfs: [
      { nombre: "Apuntes del tema 4", detalle: "Variación absoluta y porcentual", archivo: "pdfs/tema-04-variacion-absoluta-y-porcentual.pdf" }
    ]
  },
  {
    titulo: "Interés simple",
    resumen: "Interés que no se acumula: capital, tasa y años.",
    paginas: "2 páginas",
    pdfs: [
      { nombre: "Apuntes del tema 5", detalle: "Interés simple", archivo: "pdfs/tema-05-interes-simple.pdf" }
    ]
  },
  {
    titulo: "Interés compuesto",
    resumen: "Intereses que se reinvierten y vuelven a generar beneficio.",
    paginas: "3 páginas",
    pdfs: [
      { nombre: "Apuntes del tema 6", detalle: "Interés compuesto", archivo: "pdfs/tema-06-interes-compuesto.pdf" }
    ]
  },
  {
    titulo: "Proporcionalidad",
    resumen: "Regla de tres, proporcionalidad directa e inversa.",
    paginas: "4 páginas",
    pdfs: [
      { nombre: "Apuntes del tema 7", detalle: "Proporcionalidad", archivo: "pdfs/tema-07-proporcionalidad.pdf" }
    ]
  },
  {
    titulo: "Despejar incógnitas",
    resumen: "Aislar una variable en una fórmula o ecuación.",
    paginas: "1 página",
    pdfs: [
      { nombre: "Apuntes del tema 8", detalle: "Despejar incógnitas", archivo: "pdfs/tema-08-despejar-incognitas.pdf" }
    ]
  },
  {
    titulo: "Tablas y frecuencias",
    resumen: "Frecuencia absoluta, frecuencia relativa y porcentaje.",
    paginas: "3 páginas",
    pdfs: [
      { nombre: "Apuntes del tema 9", detalle: "Tablas y frecuencias", archivo: "pdfs/tema-09-tablas-y-frecuencias.pdf" }
    ]
  },
  {
    titulo: "Representaciones gráficas",
    resumen: "Gráficas de barras, de sectores y de líneas.",
    paginas: "6 páginas",
    pdfs: [
      { nombre: "Apuntes del tema 10", detalle: "Representaciones gráficas", archivo: "pdfs/tema-10-representaciones-graficas.pdf" }
    ]
  },
  {
    titulo: "Ejercicios para casa",
    resumen: "Tres bloques de ejercicios resueltos.",
    paginas: "5 páginas",
    pdfs: [
      { nombre: "Apuntes del tema 11", detalle: "Ejercicios para casa", archivo: "pdfs/tema-11-ejercicios-para-casa.pdf" }
    ]
  },
  {
    titulo: "Repaso del 6 de octubre",
    resumen: "Resumen de los ejercicios rehechos en el cuaderno.",
    paginas: "1 página",
    pdfs: [
      { nombre: "Apuntes del tema 12", detalle: "Repaso del 6 de octubre", archivo: "pdfs/tema-12-repaso-6-octubre.pdf" }
    ]
  }
];
