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
                valor = eval(expr, {"__builtins__": {}, "round": round}, {})  # solo operaciones numéricas escritas en el JSON
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


def valor(txt):
    """Separa cifra y unidad (300 € → <b>300</b><i>€</i>) para darles distinto peso, como en las tarjetas de referencia."""
    m = re.match(r"^([−+-]?[\d.,]+)\s*(.*)$", txt)
    return f"<b>{escape(m.group(1))}</b><i>{escape(m.group(2))}</i>" if m else f"<b>{escape(txt)}</b>"


def resultado(r):
    if any(ch.isdigit() for ch in r[0]):  # varias líneas de resultado: «Etiqueta 1.234 €»
        grupos = []
        for x in r:
            m = re.match(r"^(.*?)\s*([−+-]?\d[\d.,]*\s*.*)$", x)
            grupos.append(f'<div class="ds-slide__grupo"><span>{escape(m.group(1))}</span><div class="ds-slide__valor">{valor(m.group(2))}</div></div>')
        return '<div class="ds-slide__resultado ds-slide__resultado--varios">' + "".join(grupos) + "</div>"
    return f'<div class="ds-slide__resultado ds-slide__resultado--uno"><span>{escape(r[0])}</span><div class="ds-slide__valor">{valor(r[1])}</div></div>'


def resaltar(texto):
    """Enunciado tal cual (sin subrayar cantidades)."""
    return re.sub(r"(\d) ([€%])", "\\1\u00a0\\2", escape(texto))


def slide(clase, interior, n=0, fondo_oscuro=False):
    return f'<section class="ds-slide {clase}">{fondo(n, fondo_oscuro)}<div class="ds-slide__capa">{interior}</div></section>'


SIMBOLOS = ["+", "−", "×", "÷", "=", "%", "+", "−", "%", "÷", "p/100", "× 1,21", "x", "+"]


def fondo(n, oscuro=False):
    return ""  # sin marcas de agua (pedido del usuario); se conserva la función por si se vuelve a activar


def fondo_simbolos(n, oscuro=False):
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
    chip = f'<span class="ds-slide__num">{num if isinstance(num, str) else f"{num:02d}"}</span>' if num else ""
    return f'<header class="ds-slide__head">{chip}<div><span class="ds-slide__tag">{escape(tag)}</span><h2 class="ds-slide__title">{escape(titulo)}</h2></div></header>'


def marca(simbolo):
    """Símbolo gigante estilo LED: una capa desenfocada (resplandor) y otra de contorno fino algo difuminada."""
    txt = f'<text x="50%" y="72%" text-anchor="middle" font-size="520" font-weight="800" font-family="sans-serif">{escape(simbolo)}</text>'
    return ('<svg class="ds-slide__marca" viewBox="0 0 640 640" aria-hidden="true"><defs>'
            '<filter id="led-g" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="22"/></filter>'
            '<filter id="led-n" x="-10%" y="-10%" width="120%" height="120%"><feGaussianBlur stdDeviation="1.6"/></filter></defs>'
            f'<g class="ds-slide__led-glow" filter="url(#led-g)">{txt}</g><g class="ds-slide__led-trazo" filter="url(#led-n)">{txt}</g></svg>')


def etiquetas(t, texto=None):
    """Píldoras de la portada: número de tema (relleno) y materia/sección (contorno)."""
    num = f'<span class="ds-slide__tema">Tema {t["numero"]:02d}</span>' if texto is None else ""
    return f'<div class="ds-slide__etiquetas">{num}<span class="ds-slide__tag">{escape(texto or t["materia"])}</span></div>'


def datos(lista, cls=""):
    def una(a, b):
        m = re.match(r"^([\d.,]+)\s*%$", b)
        barra = f'<div class="ds-slide__barra" style="--p:{m.group(1).replace(",", ".")}"><i></i></div>' if m else ""
        return f'<div class="ds-slide__minicard"><span>{escape(a)}</span><div class="ds-slide__valor">{valor(b)}</div>{barra}</div>'
    return f'<div class="ds-slide__datos {cls} ds-slide__datos--n{len(lista)}">' + "".join(una(a, b) for a, b in lista) + "</div>"


def par(e, grande=False):
    """Enunciado (tarjeta menta) + columna de datos (tarjetas blanca y negra)."""
    return (f'<div class="ds-slide__fila{" ds-slide__fila--ej" if grande else ""}">'
            f'<div class="ds-slide__card2 ds-slide__card2--menta"><span class="ds-slide__pildora">Enunciado</span><div class="ds-slide__enun2{" ds-slide__enun2--grande" if grande else ""}">{resaltar(e["enunciado"])}</div></div>'
            f'{datos(e["datos"], "ds-slide__datos--col")}</div>')


def tarjeta_formula(e):
    return f'<div class="ds-slide__card2 ds-slide__card2--formula"><span class="ds-slide__pildora">Fórmula a aplicar</span>{formulas(e["formula"])}</div>'


def tarjeta_desarrollo(e):
    return ('<div class="ds-slide__card2"><span class="ds-slide__pildora ds-slide__pildora--clara">Desarrollo</span><div class="ds-slide__pasos">' +
            "".join(f'<div class="ds-slide__paso">{mate(p)}</div>' for p in e["desarrollo"]) + "</div></div>")


def construir(t):
    S = []
    n = 0
    sec_ej = len(t["formulas"]) + 1   # secciones tras las fórmulas: ejemplos, ejercicios y soluciones
    sec_ejer = sec_ej + 1
    sec_sol = sec_ej + 2

    def add(clase, interior, oscuro=False):
        nonlocal n
        n += 1
        S.append(slide(clase, interior, n, oscuro))

    add("ds-slide--portada", marca(t["marca"]) + etiquetas(t) + f'<h1>{escape(t["titulo"])}</h1><p class="ds-slide__lead">{escape(t["lead"])}</p><span class="ds-slide__rayas"></span>', True)
    add("", cabecera("Antes de empezar", "Qué vas a ver") + '<div class="ds-slide__body"><ol class="ds-slide__lista">' + "".join(f"<li>{escape(x)}</li>" for x in t["vas_a_ver"] + ["Ejemplos resueltos paso a paso", "10 ejercicios para practicar", "Soluciones de los ejercicios"]) + "</ol></div>")
    for i, f in enumerate(t["formulas"], 1):
        add("", cabecera("La fórmula", f["titulo"], i) + '<div class="ds-slide__body">' +
            '<div class="ds-slide__formulas">' + "".join(f'<div class="ds-slide__card2 ds-slide__card2--menta"><div class="ds-slide__formula">{mate(x)}</div></div>' for x in f["formulas"]) + "</div>" +
            f'<p class="ds-slide__explica">{escape(f["explicacion"])}</p></div>')
    for i, e in enumerate(t["ejemplos"], 1):
        add("", cabecera("Ejemplo · Planteamiento", e["titulo"], f"{sec_ej:02d}.{i}") + '<div class="ds-slide__body">' + par(e) + tarjeta_formula(e) + "</div>")
        add("", cabecera("Ejemplo · Desarrollo", e["titulo"], f"{sec_ej:02d}.{i}") + '<div class="ds-slide__body">' + datos(e["datos"], "ds-slide__datos--fila") +
            '<div class="ds-slide__cols2">' + tarjeta_formula(e) + tarjeta_desarrollo(e) + "</div>" + resultado(e["resultado"]) + "</div>")
    add("ds-slide--portada", marca("?") + etiquetas(t, "Ejercicios") + '<h1>A practicar</h1><p class="ds-slide__lead">Ahora te toca a ti. Resuelve los 10 ejercicios.</p><span class="ds-slide__rayas"></span>', True)
    for i, e in enumerate(t["ejercicios"], 1):
        add("", cabecera("Ejercicio", e["titulo"], f"{sec_ejer:02d}.{i}") + '<div class="ds-slide__body">' + par(e, True) + "</div>")
    add("ds-slide--negra", marca("✓") + etiquetas(t, "Soluciones") + '<h1>A continuación tienes las soluciones</h1><p class="ds-slide__lead">Intenta resolver los ejercicios antes de mirarlas.</p><span class="ds-slide__rayas"></span>', True)
    for i, e in enumerate(t["ejercicios"], 1):
        add("", cabecera("Solución · Ejercicio", e["titulo"], f"{sec_sol:02d}.{i}") + '<div class="ds-slide__body">' + datos(e["datos"], "ds-slide__datos--fila") +
            '<div class="ds-slide__cols2">' + tarjeta_formula(e) + tarjeta_desarrollo(e) + "</div>" + resultado(e["resultado"]) + "</div>")
    add("ds-slide--cierre", marca(t["marca"]) + etiquetas(t) + f'<h1>Tema completado</h1><p class="ds-slide__lead">Repasa la fórmula y vuelve a intentar los ejercicios.</p><span class="ds-slide__rayas"></span>', True)
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
