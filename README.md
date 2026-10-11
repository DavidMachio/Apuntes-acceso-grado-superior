# Acceso a grado superior

Web estática (HTML, CSS y JavaScript, sin instalar nada) con apuntes en PDF y exámenes para imprimir, organizada por materias. Se publica en Vercel desde la rama `main`.

## Estructura
La web tiene cuatro niveles: **portada → materia → tema → presentación**.
```
index.html              Portada: título y una tarjeta negra por materia
datos/sitio.js          Marca, pie y lista de materias (común a toda la web)
css/  iconos/  js/      Design system v2 y código común (cabecera, pie, tema claro/oscuro)
styles.css              Ajustes propios de la web (visor de PDF, portada)
matematicas/            Materia de Matemáticas (color lima)
  index.html            Lista de temas
  tema.html             Presentaciones de un tema (tema.html?n=N)
  presentacion.html     Visor de PDF (presentacion.html?n=N&pdf=M)
  examen.html           Generador de exámenes
  temario.html          Redirige a index.html (antiguo enlace)
  datos/                curso.js (textos), temario.js (temas y PDFs), preguntas.js (examen)
  pdfs/                 PDFs de los temas (presentaciones generadas con herramientas/generar_presentacion.py)
  apuntes/              Apuntes de origen (.md) y presentaciones/tema-NN.json (origen de cada PDF)
lengua/                 Materia de Lengua (rosa rojizo; de momento, «Próximamente»)
herramientas/           Scripts (generar PDFs a partir de los apuntes)
```

## Colores por página
Se eligen con `data-variante` en la etiqueta `<html>`: `amarillo` (portada), `matematicas` (lima) y `lengua` (rosa). El menú y la banda superior toman ese color; los botones y etiquetas, también.

## Añadir una materia
1. Crea su carpeta (por ejemplo `historia/`) con las páginas que necesite, copiando la estructura de `matematicas/`.
2. Añádela a la lista `materias` de `datos/sitio.js` (título, resumen e icono). La portada, el menú y el pie la muestran solos. Si quieres un color propio, añade una variante en el design system.

## Matemáticas: dónde se edita cada cosa
| Qué | Archivo |
|---|---|
| Título y subtítulo de la materia | `matematicas/datos/curso.js` |
| Temas y PDFs | `matematicas/datos/temario.js` |
| Preguntas de examen | `matematicas/datos/preguntas.js` (el formato está explicado al principio del archivo) |
| Estilos del examen | `matematicas/examen.css` |

Para añadir un tema: nueva entrada en `temario.js`, su PDF en `matematicas/pdfs/` y sus preguntas en `preguntas.js` con el mismo número. Si cambias o quitas preguntas, sube `BANCO_VERSION`.

## Exámenes
- Eliges temas, número de preguntas y tipo (test, problemas o mixto).
- Cada examen tiene un **código** (por ejemplo `1-1.2.3-10-M-ABCDE`). Con el mismo código sale siempre el mismo examen.
- «Imprimir examen» / «Imprimir soluciones»: en el cuadro de impresión elige «Guardar como PDF» (A4).
- Las fórmulas usan un formato propio (`matematicas/js/mate.js`) con sintaxis LaTeX básica: `$\frac{3}{4}$`, `x^2`, `\sqrt{9}`, `\text{…}`.

## Generar los PDFs de los apuntes
Cada tema tiene su origen en `matematicas/apuntes/presentaciones/tema-NN.json` (título, fórmulas, 3 ejemplos y 10 ejercicios con sus soluciones). Para crear o regenerar un PDF:
```
python3 herramientas/generar_presentacion.py matematicas/apuntes/presentaciones/tema-01.json matematicas/pdfs/tema-01-porcentajes.pdf
# opción --html: guarda también el HTML intermedio para revisarlo en el navegador
```
- Orden de las diapositivas: portada · qué vas a ver · fórmulas · ejemplos (planteamiento y desarrollo) · «A practicar» · 10 ejercicios · «Soluciones» · 10 soluciones · cierre.
- Los cálculos de cada ejemplo y ejercicio se comprueban por código (campo `check`): si algo no cuadra, el script se detiene.
- Admite tablas de frecuencias (campo `tabla`) y gráficos de barras, sectores y líneas (campo `grafico`).
- El script avisa si algo no cabe en una diapositiva. El diseño sale de `css/diapositivas.css` y de los tokens del design system.
- Los ejemplos y ejercicios de los temas 5 a 10 son de creación propia y están **por revisar**.
- Necesita `pandoc` y `playwright` con Chromium. No edites los PDFs a mano: cambia el JSON y regenera.
- `herramientas/generar_diapositivas.py` es el generador antiguo (apuntes en A4 a partir de los `.md`); ya no se usa para los temas.

## Probarlo en local
Basta con abrir `index.html` con doble clic.

## Visor de PDF
`js/visor.js` muestra cada PDF página a página (flechas, teclado, miniaturas, ampliar y descargar) con pdf.js, guardado en `js/vendor/` (licencia Apache 2.0). No hay que generar imágenes: basta con sustituir el PDF.
