# Acceso a grado superior · Matemáticas

Web estática (HTML, CSS y JavaScript, sin instalar nada) para consultar y descargar los apuntes en PDF y generar exámenes para imprimir. Se publica en Vercel desde la rama `main`.

## Páginas
- `index.html` · Inicio
- `temario.html` · Temas con sus PDFs y acceso al examen de cada módulo
- `examen.html` · Generador de exámenes (se imprimen o guardan en PDF para rellenar a mano)

## Dónde se edita cada cosa
| Qué | Archivo |
|---|---|
| Textos de portada, ficha y pie | `datos/curso.js` |
| Temas y PDFs | `datos/temario.js` (los PDFs van en `pdfs/`) |
| Preguntas de examen | `datos/preguntas.js` (el formato está explicado al principio del archivo) |
| Estilos propios | `styles.css` y `examen.css` |
| Design system (no tocar) | `css/variables.css`, `css/componentes.css`, `iconos/` |

Para añadir un tema: nueva entrada en `datos/temario.js`, su PDF en `pdfs/` y sus preguntas en `datos/preguntas.js` con el mismo número.

## Exámenes
- Eliges temas, número de preguntas y tipo (test, problemas o mixto).
- Cada examen tiene un **código** (por ejemplo `1-1.2.3-10-M-ABCDE`). Con el mismo código sale siempre el mismo examen, así que se puede recuperar o repartir.
- Botones «Imprimir examen» e «Imprimir soluciones»: en el cuadro de impresión elige «Guardar como PDF» (A4, márgenes predeterminados).
- Si cambias o quitas preguntas del banco, sube `BANCO_VERSION` en `datos/preguntas.js`.
- Las fórmulas usan un formato propio (`js/mate.js`) con sintaxis LaTeX básica: `$\frac{3}{4}$`, `x^2`, `\sqrt{9}`…

## Contenido
Los 10 temas y sus PDFs salen de los apuntes «Matemáticas aplicadas» (`apuntes/apuntes-matematicas.md`). Los ejercicios repetidos de los apuntes originales se han unificado en su tema. Todos los temas tienen preguntas de examen.

## Probarlo en local
Basta con abrir `index.html` con doble clic.

## Generar los PDFs de los apuntes
`herramientas/generar_pdfs.py` convierte los apuntes transcritos (`.md` con etiquetas) en un PDF A4 por apartado, con el design system y las gráficas redibujadas (`herramientas/graficas.py`).

```
python3 herramientas/generar_pdfs.py apuntes/apuntes-matematicas.md pdfs
```
Necesita `pandoc` y `playwright` con Chromium. Si cambias los apuntes, vuelve a ejecutarlo.
