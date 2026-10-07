/* =====================================================================
   DATOS COMUNES DE TODA LA WEB — marca, pie y lista de materias.
   · Cada materia vive en su carpeta (matematicas/, lengua/…) con su propio temario y exámenes.
   · Para añadir una materia: crea su carpeta, añádela aquí y se mostrará sola en
     la portada, en el menú y en el pie.
   ===================================================================== */
const SITIO = {
  marca: "Acceso a grado superior",              // arriba a la izquierda, en el pie y en la hoja del examen
  etiqueta: "Prueba de acceso a grado superior", // texto pequeño sobre el título de la portada
  titulo: "Prepara tu acceso a grado superior",
  subtitulo: "Apuntes en PDF y exámenes para imprimir, materia por materia.",
  pie: "Última actualización: octubre de 2026. Contacto: tu-correo@ejemplo.com",

  materias: [
    {
      id: "matematicas",                         // nombre de la carpeta
      titulo: "Matemáticas",
      resumen: "Porcentajes, interés, proporcionalidad, tablas de datos y gráficas, con apuntes en PDF y exámenes para imprimir.",
      icono: "i-sigma",
      // pestañas de la materia (rutas dentro de su carpeta)
      paginas: [
        { id: "inicio",  texto: "Resumen", href: "index.html" },
        { id: "temario", texto: "Temario", href: "temario.html" },
        { id: "examen",  texto: "Examen",  href: "examen.html" }
      ]
    },
    {
      id: "lengua",
      titulo: "Lengua",
      resumen: "Apuntes y ejercicios de lengua para la prueba de acceso.",
      icono: "i-edit",
      proximamente: true,
      paginas: []
    }
  ]
};
