# Programa formativo (web estática)

Web sencilla en HTML, CSS y JavaScript, sin dependencias ni instalación.

## Qué editar
- **Todo el contenido** (título, ficha, módulos y enlaces a PDFs) está al principio de `script.js`.
- **Los PDFs** van en la carpeta `pdfs/`. Los que hay ahora son de ejemplo: sustitúyelos por los tuyos.
- El título que aparece en la pestaña del navegador se cambia en `index.html` (etiqueta `<title>`).

## Probarla en tu ordenador
Haz doble clic en `index.html`.

## Subirla a GitHub
```bash
git init
git add .
git commit -m "Primera versión del programa formativo"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/programa-formativo.git
git push -u origin main
```

## Desplegarla en Vercel
1. En vercel.com/new, importa el repositorio.
2. Framework Preset: **Other**. No hay que poner comando de build ni carpeta de salida.
3. Pulsa **Deploy**.

A partir de ahí, cada `git push` a `main` actualiza la web.
