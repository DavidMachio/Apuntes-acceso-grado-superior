/* =====================================================================
   BANCO DE PREGUNTAS — de aquí sale el generador de examen.
   (Preguntas de EJEMPLO: se sustituirán por las que se generen a partir de tus apuntes.)

   · Las preguntas se agrupan por número de módulo (1, 2, 3…), el mismo que en datos/temario.js.
   · Hay dos tipos de pregunta:

     TEST (una sola respuesta correcta, 1 punto):
       { tipo: "test",
         enunciado: "…",
         opciones: ["…", "…", "…", "…"],   // entre 3 y 5 opciones; el generador las baraja
         correcta: 1,                      // posición de la correcta en "opciones" (0 = la primera)
         explicacion: "…" }

     PROBLEMA (se resuelve a mano, 2 puntos):
       { tipo: "calculo",
         enunciado: "…",
         espacio: "m",                     // espacio para desarrollar: "s" (poco), "m" (medio) o "l" (mucho)
         solucion: ["paso 1", "paso 2"],   // resolución paso a paso (hoja de soluciones)
         respuesta: "…" }                  // resultado final

   · Fórmulas: se escriben entre signos $ … $ con una versión sencilla de LaTeX:
       fracción  \frac{3}{4}      potencia  x^2  o  x^{10}      subíndice  x_v
       raíz      \sqrt{144}       símbolos  \cdot  \times  \pi  \approx  \le  \ge  \neq  \pm
     Se usa String.raw (la "r" delante de las comillas invertidas) para no tener que duplicar las barras.

   · Si cambias o quitas preguntas, sube BANCO_VERSION: así los códigos de exámenes antiguos
     avisan de que ya no coinciden con el banco actual.
   ===================================================================== */
const r = String.raw;
const BANCO_VERSION = 1;

const PREGUNTAS = {

  /* ------------------------- Módulo 1 · Números y operaciones ------------------------- */
  1: [
    { tipo: "test",
      enunciado: r`Calcula $\frac{3}{4}+\frac{5}{6}$.`,
      opciones: [r`$\frac{8}{10}$`, r`$\frac{19}{12}$`, r`$\frac{15}{24}$`, r`$\frac{9}{10}$`],
      correcta: 1,
      explicacion: r`Se reducen a común denominador (12): $\frac{9}{12}+\frac{10}{12}=\frac{19}{12}$.` },
    { tipo: "test",
      enunciado: r`¿Cuánto es el 15 % de 240?`,
      opciones: ["24", "30", "36", "40"],
      correcta: 2,
      explicacion: r`El 15 % es multiplicar por 0,15: $240\cdot 0,15=36$.` },
    { tipo: "test",
      enunciado: r`Simplifica $2^3\cdot 2^4$.`,
      opciones: [r`$2^7$`, r`$2^{12}$`, r`$4^7$`, r`$4^{12}$`],
      correcta: 0,
      explicacion: r`Al multiplicar potencias de la misma base se suman los exponentes: $2^{3+4}=2^7$.` },
    { tipo: "test",
      enunciado: r`Un artículo cuesta 80 € y sube un 25 %. ¿Cuál es su nuevo precio?`,
      opciones: ["85 €", "100 €", "105 €", "120 €"],
      correcta: 1,
      explicacion: r`Subir un 25 % es multiplicar por 1,25: $80\cdot 1,25=100$ €.` },
    { tipo: "calculo",
      enunciado: r`Calcula $\sqrt{144}-3^2+5$.`,
      espacio: "s",
      solucion: [r`$\sqrt{144}=12$ y $3^2=9$.`, r`$12-9+5=8$.`],
      respuesta: r`$8$` },
    { tipo: "calculo",
      enunciado: r`Efectúa y simplifica: $\frac{2}{3}\cdot\frac{9}{4}$.`,
      espacio: "s",
      solucion: [r`Se multiplican numeradores y denominadores: $\frac{2\cdot 9}{3\cdot 4}=\frac{18}{12}$.`, r`Se simplifica dividiendo entre 6: $\frac{3}{2}$.`],
      respuesta: r`$\frac{3}{2}$` }
  ],

  /* ------------------------- Módulo 2 · Álgebra ------------------------- */
  2: [
    { tipo: "test",
      enunciado: r`Resuelve la ecuación $3x-7=11$.`,
      opciones: [r`$x=4$`, r`$x=6$`, r`$x=18$`, r`$x=\frac{4}{3}$`],
      correcta: 1,
      explicacion: r`$3x=11+7=18$, luego $x=\frac{18}{3}=6$.` },
    { tipo: "test",
      enunciado: r`Desarrolla $(x+3)^2$.`,
      opciones: [r`$x^2+9$`, r`$x^2+6x+9$`, r`$x^2+3x+9$`, r`$x^2+6x+6$`],
      correcta: 1,
      explicacion: r`Cuadrado de una suma: $(a+b)^2=a^2+2ab+b^2$. Aquí, $x^2+2\cdot x\cdot 3+3^2$.` },
    { tipo: "test",
      enunciado: r`¿Cuál es la solución de la inecuación $2x+5>11$?`,
      opciones: [r`$x>3$`, r`$x>8$`, r`$x<3$`, r`$x>\frac{11}{2}$`],
      correcta: 0,
      explicacion: r`$2x>11-5=6$, luego $x>3$.` },
    { tipo: "calculo",
      enunciado: r`Resuelve el sistema formado por $x+y=10$ y $x-y=2$.`,
      espacio: "m",
      solucion: [r`Sumando las dos ecuaciones: $2x=12$, luego $x=6$.`, r`Sustituyendo en la primera: $6+y=10$, luego $y=4$.`],
      respuesta: r`$x=6$ e $y=4$` },
    { tipo: "calculo",
      enunciado: r`Resuelve la ecuación $x^2-5x+6=0$.`,
      espacio: "m",
      solucion: [r`Se buscan dos números que sumen 5 y multipliquen 6: son 2 y 3.`, r`Por tanto, $(x-2)(x-3)=0$.`],
      respuesta: r`$x=2$ y $x=3$` }
  ],

  /* ------------------------- Módulo 3 · Funciones ------------------------- */
  3: [
    { tipo: "test",
      enunciado: r`¿Cuál es la pendiente de la recta $y=-2x+5$?`,
      opciones: ["5", "−2", "2", "−5"],
      correcta: 1,
      explicacion: r`En $y=mx+n$ la pendiente es $m$. Aquí, $m=-2$.` },
    { tipo: "test",
      enunciado: r`Si $f(x)=x^2-4$, ¿cuánto vale $f(3)$?`,
      opciones: ["5", "2", "−1", "13"],
      correcta: 0,
      explicacion: r`$f(3)=3^2-4=9-4=5$.` },
    { tipo: "test",
      enunciado: r`¿Cuál es el vértice de la parábola $y=x^2-6x+5$?`,
      opciones: [r`$(3,-4)$`, r`$(-3,-4)$`, r`$(6,5)$`, r`$(3,4)$`],
      correcta: 0,
      explicacion: r`$x_v=-\frac{b}{2a}=\frac{6}{2}=3$ y $y_v=3^2-6\cdot 3+5=-4$.` },
    { tipo: "calculo",
      enunciado: r`Halla la ecuación de la recta que pasa por los puntos $A(1,3)$ y $B(3,7)$.`,
      espacio: "m",
      solucion: [r`Pendiente: $m=\frac{7-3}{3-1}=2$.`, r`Ecuación punto-pendiente: $y-3=2(x-1)$.`, r`Despejando: $y=2x+1$.`],
      respuesta: r`$y=2x+1$` },
    { tipo: "calculo",
      enunciado: r`Calcula los puntos de corte de $y=x^2-4$ con el eje X.`,
      espacio: "s",
      solucion: [r`Se hace $y=0$: $x^2-4=0$.`, r`Entonces $x^2=4$, luego $x=2$ o $x=-2$.`],
      respuesta: r`$(-2,0)$ y $(2,0)$` }
  ],

  /* ------------------------- Módulo 4 · Geometría ------------------------- */
  4: [
    { tipo: "test",
      enunciado: r`¿Cuál es el área de un círculo de radio 5 cm?`,
      opciones: [r`$10\pi$ cm²`, r`$25\pi$ cm²`, r`$5\pi$ cm²`, r`$50\pi$ cm²`],
      correcta: 1,
      explicacion: r`$A=\pi r^2=\pi\cdot 5^2=25\pi$ cm².` },
    { tipo: "test",
      enunciado: r`Un triángulo rectángulo tiene catetos de 6 cm y 8 cm. ¿Cuánto mide la hipotenusa?`,
      opciones: ["10 cm", "14 cm", "12 cm", "48 cm"],
      correcta: 0,
      explicacion: r`Por Pitágoras: $h=\sqrt{6^2+8^2}=\sqrt{100}=10$ cm.` },
    { tipo: "test",
      enunciado: r`Dos figuras son semejantes con razón de semejanza 3. ¿Cuál es la razón entre sus áreas?`,
      opciones: ["3", "6", "9", "27"],
      correcta: 2,
      explicacion: r`Las áreas se relacionan con el cuadrado de la razón: $3^2=9$.` },
    { tipo: "calculo",
      enunciado: r`Calcula el volumen de un cilindro de radio 3 cm y altura 10 cm. Da el resultado exacto y aproximado con dos decimales.`,
      espacio: "m",
      solucion: [r`Fórmula: $V=\pi r^2 h$.`, r`$V=\pi\cdot 3^2\cdot 10=90\pi$ cm³.`, r`Con $\pi\approx 3,1416$: $V\approx 282,74$ cm³.`],
      respuesta: r`$90\pi\approx 282,74$ cm³` },
    { tipo: "calculo",
      enunciado: r`Una escalera de 5 m se apoya en una pared con el pie a 3 m de ella. ¿A qué altura de la pared llega?`,
      espacio: "m",
      solucion: [r`La escalera, el suelo y la pared forman un triángulo rectángulo con hipotenusa 5 m y un cateto de 3 m.`, r`$h=\sqrt{5^2-3^2}=\sqrt{16}=4$ m.`],
      respuesta: r`4 m` }
  ],

  /* ------------------------- Módulo 5 · Estadística y probabilidad ------------------------- */
  5: [
    { tipo: "test",
      enunciado: r`¿Cuál es la media de los datos 4, 8, 6, 10 y 12?`,
      opciones: ["6", "8", "9", "10"],
      correcta: 1,
      explicacion: r`La suma es 40 y hay 5 datos: $\frac{40}{5}=8$.` },
    { tipo: "test",
      enunciado: r`¿Cuál es la mediana de los datos 3, 9, 4, 7 y 5?`,
      opciones: ["4", "5", "6", "7"],
      correcta: 1,
      explicacion: r`Ordenados: 3, 4, 5, 7, 9. El valor central es 5.` },
    { tipo: "test",
      enunciado: r`¿Cuál es la moda de los datos 2, 3, 3, 5, 3, 7 y 5?`,
      opciones: ["2", "3", "5", "7"],
      correcta: 1,
      explicacion: r`El 3 aparece tres veces, más que ningún otro valor.` },
    { tipo: "test",
      enunciado: r`Se lanza un dado de seis caras. ¿Cuál es la probabilidad de obtener un número par?`,
      opciones: [r`$\frac{1}{3}$`, r`$\frac{1}{2}$`, r`$\frac{1}{6}$`, r`$\frac{2}{3}$`],
      correcta: 1,
      explicacion: r`Hay 3 números pares (2, 4 y 6) entre 6 posibles: $\frac{3}{6}=\frac{1}{2}$.` },
    { tipo: "calculo",
      enunciado: r`Una bolsa tiene 3 bolas rojas y 5 azules. Se sacan dos bolas sin devolverlas. ¿Cuál es la probabilidad de que las dos sean rojas?`,
      espacio: "m",
      solucion: [r`Primera bola roja: $\frac{3}{8}$.`, r`Segunda bola roja (quedan 2 rojas entre 7 bolas): $\frac{2}{7}$.`, r`Se multiplican: $\frac{3}{8}\cdot\frac{2}{7}=\frac{6}{56}=\frac{3}{28}$.`],
      respuesta: r`$\frac{3}{28}$` }
  ]
};
