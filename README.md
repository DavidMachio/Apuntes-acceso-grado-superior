# Acceso a grado superior · Matemáticas

Web estática (HTML, CSS y JavaScript, sin instalar nada) para consultar y descargar los apuntes en PDF y generar exámenes para imprimir. Se publica en Vercel desde la rama `main`.

## Páginas
- `index.html` · Inicio
- `temario.html` · Módulos con sus PDFs y acceso al examen de cada módulo
- `examen.html` · Generador de exámenes (se imprimen o guardan en PDF para rellenar a mano)

## Dónde se edita cada cosa
| Qué | Archivo |
|---|---|
| Textos de portada, ficha y pie | `datos/curso.js` |
| Módulos y PDFs | `datos/temario.js` (los PDFs van en `pdfs/`) |
| Preguntas de examen | `datos/preguntas.js` (el formato está explicado al principio del archivo) |
| Estilos propios | `styles.css` y `examen.css` |
| Design system (no tocar) | `css/variables.css`, `css/componentes.css`, `iconos/` |

Para añadir un módulo: nueva entrada en `datos/temario.js`, su PDF en `pdfs/` y sus preguntas en `datos/preguntas.js` con el mismo número.

## Exámenes
- Eliges módulos, número de preguntas y tipo (test, problemas o mixto).
- Cada examen tiene un **código** (por ejemplo `1-1.2.3-10-M-ABCDE`). Con el mismo código sale siempre el mismo examen, así que se puede recuperar o repartir.
- Botones «Imprimir examen» e «Imprimir soluciones»: en el cuadro de impresión elige «Guardar como PDF» (A4, márgenes predeterminados).
- Si cambias o quitas preguntas del banco, sube `BANCO_VERSION` en `datos/preguntas.js`.
- Las fórmulas usan un formato propio (`js/mate.js`) con sintaxis LaTeX básica: `$\frac{3}{4}$`, `x^2`, `\sqrt{9}`…

## Contenido de ejemplo
Los módulos, los PDFs y las 26 preguntas actuales son de ejemplo y se sustituirán por los generados a partir de tus apuntes.

## Probarlo en local
Basta con abrir `index.html` con doble clic.
