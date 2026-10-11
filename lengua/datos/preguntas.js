/* =====================================================================
   BANCO DE PREGUNTAS DE LENGUA — de aquí saldrá el generador de examen.
   (Preguntas basadas en los apuntes de Lengua: lengua/apuntes/transcripcion-apuntes-lengua.md.)

   · Mismo formato que matematicas/datos/preguntas.js: las preguntas se agrupan por número de tema
     (1, 2…), el mismo que en lengua/datos/temario.js.
   · Hay dos tipos de pregunta:

     TEST (una sola respuesta correcta, 1 punto):
       { tipo: "test",
         enunciado: "…",
         opciones: ["…", "…", "…", "…"],   // entre 3 y 5 opciones; el generador las baraja
         correcta: 1,                      // posición de la correcta en "opciones" (0 = la primera)
         explicacion: "…" }

     DESARROLLO (se resuelve a mano, 2 puntos; en Lengua es un ejercicio escrito, no un cálculo):
       { tipo: "calculo",                  // se mantiene el nombre «calculo» para reutilizar el generador de examen
         enunciado: "…",
         espacio: "m",                     // espacio para desarrollar: "s" (poco), "m" (medio) o "l" (mucho)
         solucion: ["paso 1", "paso 2"],   // resolución paso a paso (hoja de soluciones)
         respuesta: "…" }                  // respuesta final

   · Estado: PROPUESTA por revisar. Todas las preguntas salen de tus apuntes y de tus ejercicios; las de las
     funciones del lenguaje que usan definiciones están marcadas en lengua/apuntes/banco-preguntas-revision.md.
   · Si cambias o quitas preguntas, sube BANCO_VERSION: así los códigos de exámenes antiguos
     avisan de que ya no coinciden con el banco actual.
   ===================================================================== */
const BANCO_VERSION = 1;

const PREGUNTAS = {

  /* ------------------------- Tema 1 · Ortografía ------------------------- */
  1: [
    { tipo: "test",
      enunciado: "¿Cuál de estas frases está en estilo directo?",
      opciones: ["Cristina le dijo “trae el pan”.", "Cristina le dijo a su hija que trajera el pan.", "Cristina pidió a su hija que trajera el pan.", "Cristina contó que su hija había traído el pan."],
      correcta: 0,
      explicacion: "En el estilo directo se mantienen las palabras originales, entre comillas: “trae el pan”." },
    { tipo: "test",
      enunciado: "¿Qué se hace en el estilo indirecto?",
      opciones: ["Se mantienen las palabras originales.", "Se cuenta lo que una persona ha dicho.", "Se escribe siempre entre comillas.", "Se usa solo en los textos escritos."],
      correcta: 1,
      explicacion: "En el estilo indirecto se cuenta lo que una persona ha dicho: Cristina le dijo a su hija que trajera el pan." },
    { tipo: "test",
      enunciado: "¿Cuándo llevan tilde las palabras agudas?",
      opciones: ["Siempre.", "Cuando terminan en vocal, N o S.", "Cuando no terminan en vocal, N o S.", "Nunca."],
      correcta: 1,
      explicacion: "En las agudas suena más fuerte la última sílaba y llevan tilde si terminan en vocal, N o S: cortés, pantalón. «Robot» termina en T y no la lleva." },
    { tipo: "test",
      enunciado: "¿Cuándo llevan tilde las palabras llanas?",
      opciones: ["Siempre.", "Cuando terminan en vocal, N o S.", "Cuando no terminan en vocal, N o S.", "Nunca."],
      correcta: 2,
      explicacion: "En las llanas suena más fuerte la penúltima sílaba y llevan tilde si no terminan en vocal, N o S: césped, árbol, bíceps, ámbar." },
    { tipo: "test",
      enunciado: "¿Cuál de estas palabras es esdrújula?",
      opciones: ["Cortés", "Césped", "Cántaro", "Robot"],
      correcta: 2,
      explicacion: "«Cán-ta-ro» es esdrújula: suena más fuerte la antepenúltima sílaba y las esdrújulas siempre llevan tilde. «Cortés» y «robot» son agudas; «césped», llana." },
    { tipo: "test",
      enunciado: "¿Qué grupo está formado solo por vocales abiertas?",
      opciones: ["A, E, O", "I, U", "A, I, U", "E, I, O"],
      correcta: 0,
      explicacion: "Las vocales abiertas son A, E, O; las cerradas, I, U." },
    { tipo: "test",
      enunciado: "¿Cuál de estas palabras tiene un diptongo?",
      opciones: ["Maíz", "Huésped", "Reúne", "Ataúd"],
      correcta: 1,
      explicacion: "«Huésped» (hués-ped) tiene un diptongo: dos vocales en una misma sílaba. «Maíz» (ma-íz), «reúne» (re-ú-ne) y «ataúd» (a-ta-úd) tienen un hiato." },
    { tipo: "test",
      enunciado: "Un triptongo es la unión, en una misma sílaba, de…",
      opciones: ["dos vocales abiertas.", "una vocal abierta y una cerrada.", "una vocal cerrada, una abierta y otra cerrada.", "tres vocales abiertas."],
      correcta: 2,
      explicacion: "El triptongo une tres vocales en una sílaba: cerrada + abierta + cerrada. Ejemplo: fastidiéis." },
    { tipo: "test",
      enunciado: "En un hiato, cuando la vocal tónica es la cerrada (como en «fría», «río» o «reír»), la palabra…",
      opciones: ["no lleva tilde.", "lleva tilde solo si es aguda.", "siempre lleva tilde.", "lleva tilde solo si termina en vocal."],
      correcta: 2,
      explicacion: "Si la vocal tónica del hiato es la cerrada, siempre lleva tilde: fría, río, reír." },
    { tipo: "test",
      enunciado: "En «Tú has llegado muy pronto», ¿por qué «tú» lleva tilde?",
      opciones: ["Porque es un pronombre personal.", "Porque es un adjetivo.", "Porque es una conjunción.", "Porque es un artículo."],
      correcta: 0,
      explicacion: "«Tú» con tilde es un pronombre personal; «tu» sin tilde es un adjetivo (tu casa). Es la tilde diacrítica: distingue palabras iguales de distinta categoría gramatical." },
    { tipo: "calculo",
      enunciado: "Separa en sílabas y di si cada palabra es aguda, llana o esdrújula: césped, imágenes, pantalón, gramática.",
      espacio: "m",
      solucion: ["Césped: cés-ped. Suena más fuerte la penúltima sílaba: llana.", "Imágenes: i-má-ge-nes. Suena más fuerte la antepenúltima: esdrújula.", "Pantalón: pan-ta-lón. Suena más fuerte la última: aguda.", "Gramática: gra-má-ti-ca. Suena más fuerte la antepenúltima: esdrújula."],
      respuesta: "cés-ped (llana) · i-má-ge-nes (esdrújula) · pan-ta-lón (aguda) · gra-má-ti-ca (esdrújula)." },
    { tipo: "calculo",
      enunciado: "Separa por sílabas e indica si hay diptongo o hiato: vencéis, biología, resfriado, homeopatía.",
      espacio: "m",
      solucion: ["Vencéis: ven-céis. «éis» va en una sola sílaba: diptongo.", "Biología: bio-lo-gí-a. «gí-a» se separa en dos sílabas: hiato.", "Resfriado: res-fria-do. «ia» va en una sola sílaba: diptongo.", "Homeopatía: ho-me-o-pa-tí-a. «e-o» y «tí-a» se separan: hiato."],
      respuesta: "ven-céis (diptongo) · bio-lo-gí-a (hiato) · res-fria-do (diptongo) · ho-me-o-pa-tí-a (hiato)." },
    { tipo: "calculo",
      enunciado: "Pasa esta frase a estilo directo: «Cristina le dijo a su hija que trajera el pan.»",
      espacio: "s",
      solucion: ["En el estilo directo se mantienen las palabras originales, entre comillas.", "Lo que Cristina dijo fue: trae el pan."],
      respuesta: "Cristina le dijo “trae el pan”." }
  ],

  /* ------------------------- Tema 2 · La comunicación ------------------------- */
  2: [
    { tipo: "test",
      enunciado: "En la comunicación, ¿cómo se llama quien emite el mensaje?",
      opciones: ["Receptor", "Emisor", "Canal", "Código"],
      correcta: 1,
      explicacion: "El emisor es quien emite el mensaje; el receptor es quien lo recibe." },
    { tipo: "test",
      enunciado: "¿Qué es el código en la comunicación?",
      opciones: ["El medio por el que se transmite el mensaje.", "El entorno en el que se comunica.", "El conjunto de reglas y símbolos que emisor y receptor usan para entenderse.", "La información que se quiere transmitir."],
      correcta: 2,
      explicacion: "El código es el conjunto de reglas y símbolos que utilizan emisor y receptor para entenderse; por ejemplo, el idioma." },
    { tipo: "test",
      enunciado: "El canal de la comunicación es…",
      opciones: ["la persona que recibe el mensaje.", "el medio a través del cual se transmite el mensaje.", "el entorno en el que se lleva a cabo la comunicación.", "la información que el emisor intenta transmitir."],
      correcta: 1,
      explicacion: "El canal es el medio por el que viaja el mensaje: la voz y el aire, un teléfono, un papel…" },
    { tipo: "test",
      enunciado: "En un concierto, ¿quién es el receptor?",
      opciones: ["El cantante o el grupo", "El público", "La canción", "El idioma"],
      correcta: 1,
      explicacion: "En un concierto el emisor es el cantante o el grupo; el receptor, el público; el mensaje, la canción; el código, el idioma, y el canal, la voz y el aire." },
    { tipo: "test",
      enunciado: "Alberto envía un mensaje de texto a Carlos para invitarle al cine. ¿Cuál es el canal?",
      opciones: ["Alberto", "Carlos", "La invitación al cine", "WhatsApp o SMS"],
      correcta: 3,
      explicacion: "Alberto es el emisor, Carlos el receptor, la invitación al cine el mensaje, el idioma escrito el código y WhatsApp o SMS el canal." },
    { tipo: "test",
      enunciado: "Los gestos, las expresiones faciales y las posturas son comunicación…",
      opciones: ["verbal.", "no verbal.", "escrita.", "hablada."],
      correcta: 1,
      explicacion: "La comunicación verbal usa el lenguaje hablado o escrito; la no verbal, los gestos, las expresiones faciales y las posturas." },
    { tipo: "test",
      enunciado: "¿Qué función del lenguaje predomina en «Las abejas viven en colmenas.»?",
      opciones: ["Referencial", "Expresiva", "Apelativa", "Poética"],
      correcta: 0,
      explicacion: "Es una función referencial: informa de un hecho de la realidad." },
    { tipo: "test",
      enunciado: "¿Qué función del lenguaje predomina en «¡Estoy exhausto!»?",
      opciones: ["Referencial", "Expresiva", "Fática", "Metalingüística"],
      correcta: 1,
      explicacion: "Es una función expresiva: el emisor expresa cómo se siente." },
    { tipo: "test",
      enunciado: "¿Qué función del lenguaje predomina en «¿Sigues en línea?»?",
      opciones: ["Poética", "Apelativa", "Fática", "Referencial"],
      correcta: 2,
      explicacion: "Es una función fática: comprueba que el canal de comunicación sigue abierto." },
    { tipo: "test",
      enunciado: "¿Qué función del lenguaje predomina en «“Sensacional” es un adjetivo.»?",
      opciones: ["Referencial", "Metalingüística", "Expresiva", "Fática"],
      correcta: 1,
      explicacion: "Es una función metalingüística: se usa el lenguaje para hablar del propio lenguaje." },
    { tipo: "calculo",
      enunciado: "Identifica el emisor, el receptor, el mensaje, el código, el canal y el contexto en esta situación: «En el instituto suena el timbre a las 15:00 h.»",
      espacio: "l",
      solucion: ["Emisor: el que toca el timbre.", "Receptor: el que lo escucha.", "Mensaje: terminan las clases.", "Código: sonido.", "Canal: aire.", "Contexto: el instituto, a las 15:00 h, a la hora del fin de clase."],
      respuesta: "Emisor: quien toca el timbre · Receptor: quien lo escucha · Mensaje: terminan las clases · Código: sonido · Canal: aire · Contexto: el instituto a las 15:00 h." },
    { tipo: "calculo",
      enunciado: "Identifica el emisor, el receptor, el mensaje, el código, el canal y el contexto en esta situación: «Un mitin político en un auditorio.»",
      espacio: "l",
      solucion: ["Emisor: el que da el mitin.", "Receptor: las personas del auditorio.", "Mensaje: el mitin.", "Código: idioma.", "Canal: voz y aire.", "Contexto: un mitin político en un auditorio."],
      respuesta: "Emisor: quien da el mitin · Receptor: el público del auditorio · Mensaje: el mitin · Código: idioma · Canal: voz y aire · Contexto: un mitin político en un auditorio." },
    { tipo: "calculo",
      enunciado: "Señala la función del lenguaje de cada frase: a) «¡Estoy exhausto!» b) «Cállate de una vez.» c) «La magia de sus ojos me hipnotiza.» d) «¿Sigues en línea?»",
      espacio: "m",
      solucion: ["a) Expresa un estado del emisor: función expresiva.", "b) Es una orden al receptor: función apelativa.", "c) Cuida la forma para que resulte bello: función poética.", "d) Comprueba el canal: función fática."],
      respuesta: "a) expresiva · b) apelativa · c) poética · d) fática." }
  ]
};
