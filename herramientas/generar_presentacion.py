#!/usr/bin/env python3
"""Genera la presentación PDF (diapositivas 16:9) de un tema a partir de su archivo JSON.

Uso:
    python3 herramientas/generar_presentacion.py matematicas/apuntes/presentaciones/tema-01.json SALIDA.pdf [--html]

Orden fijo de todas las presentaciones:
  portada · qué vas a ver · explicación de la fórmula · ejemplos resueltos · ejercicios (10)
  · «a continuación tienes las soluciones» · soluciones (10) · cierre
Cada ejemplo y cada ejercicio lleva: título, fórmula a aplicar y desarrollo con los valores.
Antes de generar, comprueba por código todos los cálculos del JSON (campo "check").
Los estilos salen de css/variables.css y css/diapositivas.css (design system v2). Sin pie de página.
Necesita pandoc y playwright (Chromium).
"""
import json
import random
import re
import subprocess
import sys
from html import escape
from pathlib import Path

from playwright.sync_api import sync_playwright

sys.path.insert(0, str(Path(__file__).resolve().parent))
from iconos_presentacion import ICONOS  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent
VARIANTE = "matematicas"   # color de la materia: matematicas (menta) · lengua (rosa rojizo) · amarillo
_cache = {}


def verificar(t):
    """Comprueba que cada cálculo del JSON da el resultado indicado. Si no, para sin generar nada."""
    n = 0
    for seccion in ("ejemplos", "ejercicios"):
        for e in t[seccion]:
            for expr, esperado in e["check"]:
                valor = eval(expr, {"__builtins__": {}}, {})  # solo operaciones numéricas escritas en el JSON
                if abs(valor - esperado) > 1e-9:
                    sys.exit(f"ERROR de cálculo en «{e['titulo']}»: {expr} = {valor}, esperado {esperado}")
                n += 1
    return n


def mate(tex):
    """LaTeX → MathML (lo muestra Chromium sin librerías extra). Los números van como texto para que lleven la tipografía de la web y la coma decimal sin espacios."""
    if tex not in _cache:
        tex = re.sub(r"\d+(?:\\,\d{3})*(?:\{,\}\d+)?", lambda m: "\\text{" + m.group(0).replace("\\,", "\u202f").replace("{,}", ",") + "}", tex)
        r = subprocess.run(["pandoc", "-f", "markdown", "-t", "html", "--mathml"], input=f"$${tex}$$", capture_output=True, text=True, check=True)
        s = r.stdout
        _cache[tex] = s[s.index("<math"):s.rindex("</math>") + 7]
    return _cache[tex]


def formulas(lista, cls=""):
    return '<div class="ds-slide__formulas ds-slide__formulas--sm">' + "".join(
        f'<div class="ds-slide__formula ds-slide__formula--sm {cls}">{mate(f)}</div>' for f in lista) + "</div>"


def resultado(r):
    if any(ch.isdigit() for ch in r[0]):  # varias líneas de resultado
        return '<div class="ds-slide__resultado">' + "".join(f"<span>{escape(x)}</span>" for x in r) + "</div>"
    return f'<div class="ds-slide__resultado"><span>{escape(r[0])}</span><b>{escape(r[1])}</b></div>'


def resaltar(texto):
    """Marca en el enunciado los datos numéricos (cantidades, euros y porcentajes)."""
    return re.sub(r"(\d[\d.,]*(?:\s?[€%])?)", r'<span class="ds-slide__dato">\1</span>', escape(texto))


def slide(clase, interior, n=0, fondo_oscuro=False):
    return f'<section class="ds-slide {clase}">{fondo(n, fondo_oscuro)}<div class="ds-slide__capa">{interior}</div></section>'


SIMBOLOS = ["+", "−", "×", "÷", "=", "%", "+", "−", "%", "÷", "p/100", "× 1,21", "x", "+"]


def fondo(n, oscuro=False):
    """Marca de agua: símbolos matemáticos de distintos tamaños repartidos por los bordes (siempre igual para la misma diapositiva)."""
    r = random.Random(n * 7919 + 13)
    puestos = []
    zonas = [(40, 60), (1180, 70), (1210, 330), (1100, 640), (640, 690), (150, 650), (30, 380), (900, 40), (420, 40), (1240, 560), (330, 700)]
    r.shuffle(zonas)
    for k, (x, y) in enumerate(zonas[:8]):
        tam = r.choice([70, 110, 160, 220, 300]) if k < 4 else r.choice([50, 80, 120])
        simbolo = r.choice(SIMBOLOS)
        giro = r.choice([-18, -8, 0, 10, 20, 35])
        vacio = " ds-slide__sim--trazo" if (oscuro or k % 3 == 0) else ""
        puestos.append(f'<text class="ds-slide__sim{vacio}" x="{x}" y="{y}" font-size="{tam}" transform="rotate({giro} {x} {y})">{escape(simbolo)}</text>')
    return f'<svg class="ds-slide__fondo" viewBox="0 0 1280 720" aria-hidden="true">{"".join(puestos)}</svg>'


def cabecera(tag, titulo, num=None):
    chip = f'<span class="ds-slide__num">{num:02d}</span>' if num else ""
    return f'<header class="ds-slide__head">{chip}<div><span class="ds-slide__tag">{escape(tag)}</span><h2 class="ds-slide__title">{escape(titulo)}</h2></div></header>'


def marca(simbolo):
    return ('<svg class="ds-slide__marca" viewBox="0 0 560 560" aria-hidden="true">'
            f'<text x="50%" y="70%" text-anchor="middle" font-size="430" font-weight="800" font-family="sans-serif">{escape(simbolo)}</text></svg>')


def datos(lista, cls=""):
    return f'<div class="ds-slide__datos {cls}">' + "".join(f'<div class="ds-slide__minicard"><span>{escape(a)}</span><b>{escape(b)}</b></div>' for a, b in lista) + "</div>"


def tarjeta_formula(e):
    return f'<div class="ds-slide__card2 ds-slide__card2--formula"><span class="ds-slide__cap">Fórmula a aplicar</span>{formulas(e["formula"])}</div>'


def tarjeta_desarrollo(e):
    return ('<div class="ds-slide__card2"><span class="ds-slide__cap">Desarrollo</span><div class="ds-slide__pasos">' +
            "".join(f'<div class="ds-slide__paso">{mate(p)}</div>' for p in e["desarrollo"]) + "</div></div>")


def construir(t):
    S = []
    n = 0

    def add(clase, interior, oscuro=False):
        nonlocal n
        n += 1
        S.append(slide(clase, interior, n, oscuro))

    add("ds-slide--portada", marca(t["marca"]) + f'<span class="ds-slide__tag">{escape(t["materia"])}</span><h1>{escape(t["titulo"])}</h1><p class="ds-slide__lead">{escape(t["lead"])}</p><span class="ds-slide__rayas"></span>', True)
    add("", cabecera("Antes de empezar", "Qué vas a ver") + '<div class="ds-slide__body"><ol class="ds-slide__lista">' + "".join(f"<li>{escape(x)}</li>" for x in t["vas_a_ver"]) + "</ol></div>")
    for i, f in enumerate(t["formulas"], 1):
        add("", cabecera("La fórmula", f["titulo"], i) + '<div class="ds-slide__body">' +
            '<div class="ds-slide__formulas">' + "".join(f'<div class="ds-slide__card2 ds-slide__card2--menta"><div class="ds-slide__formula">{mate(x)}</div></div>' for x in f["formulas"]) + "</div>" +
            f'<p class="ds-slide__explica">{escape(f["explicacion"])}</p></div>')
    for i, e in enumerate(t["ejemplos"], 1):
        add("", cabecera("Ejemplo · Planteamiento", e["titulo"], i) + '<div class="ds-slide__body"><div class="ds-slide__fila">' +
            f'<div class="ds-slide__izq"><div class="ds-slide__card2 ds-slide__card2--menta"><span class="ds-slide__cap">Enunciado</span><div class="ds-slide__enun2">{resaltar(e["enunciado"])}</div></div>' +
            f'<span class="ds-slide__cap ds-slide__cap--suelto">Datos que da el enunciado</span>{datos(e["datos"])}</div>' +
            tarjeta_formula(e) + "</div></div>")
        add("", cabecera("Ejemplo · Desarrollo", e["titulo"], i) + '<div class="ds-slide__body">' + datos(e["datos"], "ds-slide__datos--fila") +
            '<div class="ds-slide__cols2">' + tarjeta_formula(e) + tarjeta_desarrollo(e) + "</div>" + resultado(e["resultado"]) + "</div>")
    for i, e in enumerate(t["ejercicios"], 1):
        add("", cabecera("Ejercicio", e["titulo"], i) + '<div class="ds-slide__body"><div class="ds-slide__fila ds-slide__fila--ej">' +
            f'<div class="ds-slide__card2 ds-slide__card2--menta"><div class="ds-slide__enun2 ds-slide__enun2--grande">{resaltar(e["enunciado"])}</div></div>' +
            f'<div class="ds-slide__izq"><span class="ds-slide__cap ds-slide__cap--suelto">Datos</span>{datos(e["datos"])}</div></div></div>')
    add("ds-slide--negra", marca("✓") + '<span class="ds-slide__tag">Soluciones</span><h1>A continuación tienes las soluciones</h1><p class="ds-slide__lead">Intenta resolver los ejercicios antes de mirarlas.</p><span class="ds-slide__rayas"></span>', True)
    for i, e in enumerate(t["ejercicios"], 1):
        add("", cabecera("Solución · Ejercicio", e["titulo"], i) + '<div class="ds-slide__body">' + datos(e["datos"], "ds-slide__datos--fila") +
            '<div class="ds-slide__cols2">' + tarjeta_formula(e) + tarjeta_desarrollo(e) + "</div>" + resultado(e["resultado"]) + "</div>")
    add("ds-slide--cierre", marca(t["marca"]) + f'<span class="ds-slide__tag">{escape(t["materia"])}</span><h1>Tema completado</h1><p class="ds-slide__lead">Repasa la fórmula y vuelve a intentar los ejercicios.</p><span class="ds-slide__rayas"></span>', True)
    return S


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) != 2:
        sys.exit(__doc__)
    t = json.loads(Path(args[0]).read_text(encoding="utf-8"))
    print(verificar(t), "cálculos verificados")
    css = "\n".join((RAIZ / "css" / f).read_text(encoding="utf-8") for f in ("variables.css", "componentes.css", "diapositivas.css"))
    html = (f'<!doctype html><html lang="es" data-variante="{VARIANTE}"><head><meta charset="utf-8"><title>{escape(t["titulo"])}</title>'
            f"<style>{css}</style></head><body class=\"ds-slides{' ds-slides--horiz' if '--horizontal' in sys.argv else ''}\">" + "\n".join(construir(t)) + "</body></html>")
    salida = Path(args[1])
    salida.parent.mkdir(parents=True, exist_ok=True)
    if "--html" in sys.argv:
        salida.with_suffix(".html").write_text(html, encoding="utf-8")
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1280, "height": 720})
        pg.set_content(html)
        pg.wait_for_timeout(300)
        desbordadas = pg.evaluate("""() => [...document.querySelectorAll('.ds-slide')].map((s, i) => [i + 1, s.scrollHeight > s.clientHeight + 1 || [...s.querySelectorAll('.ds-slide__body')].some(b => b.scrollHeight > b.clientHeight + 1)]).filter(x => x[1]).map(x => x[0])""")
        if desbordadas:
            print("AVISO: diapositivas con contenido que no cabe:", desbordadas)
        pg.pdf(path=str(salida), width="1280px", height="720px", print_background=True, prefer_css_page_size=True)
        b.close()
    print("Generado", salida, "·", len(construir(t)), "diapositivas")


if __name__ == "__main__":
    main()
