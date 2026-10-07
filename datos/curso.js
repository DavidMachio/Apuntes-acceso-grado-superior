/* =====================================================================
   DATOS GENERALES DE LA WEB — textos de la portada, ficha y pie.
   (El temario está en datos/temario.js y las preguntas en datos/preguntas.js)
   ===================================================================== */
const CURSO = {
  marca: "Acceso a grado superior",              // nombre corto: arriba a la izquierda y en el pie
  etiqueta: "Prueba de acceso a grado superior", // texto pequeño sobre el título de la portada
  titulo: "Prepara las matemáticas a tu ritmo",
  subtitulo: "Apuntes en PDF y exámenes para imprimir, con las soluciones aparte.",

  descripcion: [
    "Escribe aquí la presentación: a quién va dirigido el material, qué incluye y cómo se recomienda estudiarlo.",
    "Puedes añadir tantos párrafos como necesites; cada texto entre comillas es un párrafo."
  ],

  ficha: [
    { etiqueta: "Nivel",       valor: "Acceso a grado superior" },
    { etiqueta: "Material",    valor: "Apuntes en PDF" },
    { etiqueta: "Exámenes",    valor: "Para imprimir y rellenar a mano" },
    { etiqueta: "Soluciones",  valor: "En una hoja aparte" }
  ],

  examenTitulo: "Examen de matemáticas",         // título que sale en la hoja del examen

  pie: "Última actualización: octubre de 2026. Contacto: tu-correo@ejemplo.com"
};
