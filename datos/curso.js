/* =====================================================================
   DATOS GENERALES DE LA WEB — textos de la portada, ficha y pie.
   (El temario está en datos/temario.js y las preguntas en datos/preguntas.js)
   ===================================================================== */
const CURSO = {
  marca: "Acceso a grado superior",              // nombre corto: arriba a la izquierda y en el pie
  etiqueta: "Prueba de acceso a grado superior", // texto pequeño sobre el título de la portada
  titulo: "Matemáticas aplicadas",
  subtitulo: "Apuntes en PDF y exámenes para imprimir, con las soluciones aparte.",

  descripcion: [
    "Apuntes de matemáticas para preparar la prueba de acceso a grado superior: porcentajes, interés simple y compuesto, proporcionalidad, tablas de datos y gráficas.",
    "Cada tema tiene su PDF con la teoría y ejemplos resueltos. Después puedes generar un examen con preguntas de los temas que elijas, imprimirlo, hacerlo a mano y corregirlo con la hoja de soluciones."
  ],

  ficha: [
    { etiqueta: "Nivel",       valor: "Acceso a grado superior" },
    { etiqueta: "Material",    valor: "10 temas en PDF" },
    { etiqueta: "Exámenes",    valor: "Para imprimir y rellenar a mano" },
    { etiqueta: "Soluciones",  valor: "En una hoja aparte" }
  ],

  examenTitulo: "Examen de matemáticas",         // título que sale en la hoja del examen

  pie: "Última actualización: octubre de 2026. Contacto: tu-correo@ejemplo.com"
};
