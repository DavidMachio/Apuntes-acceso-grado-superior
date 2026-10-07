# Acceso a grado superior

Web estática (HTML, CSS y JavaScript, sin instalar nada) con apuntes en PDF y exámenes para imprimir, organizada por materias. Se publica en Vercel desde la rama `main`.

## Estructura
```
index.html              Portada: una tarjeta grande por materia
datos/sitio.js          Marca, pie y lista de materias (común a toda la web)
css/  iconos/  js/      Design system y código común (cabecera, pie, tema claro/oscuro)
styles.css              Ajustes propios de la web
matematicas/            Materia de Matemáticas
  index.html            Resumen
  temario.html          Temas con su PDF (botón Ver / Descargar)
  tema.html             Visor de PDF de un tema (tema.html?n=N)
  examen.html           Generador de exámenes
  datos/                curso.js (textos), temario.js (temas y PDFs), preguntas.js (examen)
  pdfs/                 PDFs de los temas (diapositivas generadas con herramientas/generar_diapositivas.py)
  apuntes/              Apuntes de origen (.md)
lengua/                 Materia de Lengua (de momento, «Próximamente»)
herramientas/           Scripts (generar PDFs a partir de los apuntes)
```

## Añadir una materia
1. Crea su carpeta (por ejemplo `historia/`) con las páginas que necesite, copiando la estructura de `matematicas/`.
2. Añádela a la lista `materias` de `datos/sitio.js` (título, resumen, icono y pestañas). La portada, el menú y el pie la muestran solos.

## Matemáticas: dónde se edita cada cosa
| Qué | Archivo |
|---|---|
| Textos del resumen y ficha | `matematicas/datos/curso.js` |
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
```
python3 herramientas/generar_diapositivas.py matematicas/apuntes/apuntes-matematicas.md matematicas/pdfs
# El texto didáctico (descripciones, ideas para recordar, ejemplos) está en matematicas/apuntes/diapositivas.json
```
Crea un PDF A4 por apartado con el design system y las gráficas redibujadas (`herramientas/graficas.py`). Necesita `pandoc` y `playwright` con Chromium.

## Probarlo en local
Basta con abrir `index.html` con doble clic.
