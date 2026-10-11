/* =====================================================================
   TEMARIO DE LENGUA — un bloque por tema, con su PDF.
   · El número de tema es su posición en la lista (1, 2, 3…).
   · Aquí la lista se llama MODULOS_LENGUA (y no MODULOS, como en Matemáticas) para que la portada pueda cargar
     los dos temarios a la vez y sumar las cifras.
   · Los PDFs se guardan en lengua/pdfs y se generan con herramientas/generar_presentacion_lengua.py
     a partir de lengua/apuntes/presentaciones/tema-NN.json.
   · «paginas» es el número de diapositivas del PDF (cámbialo si regeneras el PDF y cambia).
   ===================================================================== */
const MODULOS_LENGUA = [
  {
    titulo: "Ortografía",
    resumen: "Estilo directo e indirecto, sílabas, diptongos, hiatos y tildes.",
    paginas: "25 diapositivas",
    pdfs: [
      { nombre: "Apuntes del tema 1", detalle: "Ortografía", archivo: "pdfs/tema-01-ortografia.pdf" }
    ]
  },
  {
    titulo: "La comunicación",
    resumen: "Elementos de la comunicación y funciones del lenguaje.",
    paginas: "38 diapositivas",
    pdfs: [
      { nombre: "Apuntes del tema 2", detalle: "La comunicación", archivo: "pdfs/tema-02-la-comunicacion.pdf" }
    ]
  }
];
