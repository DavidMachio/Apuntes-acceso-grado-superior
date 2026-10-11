#!/usr/bin/env python3
"""Genera la presentación PDF (diapositivas 16:9) de un tema de LENGUA a partir de su archivo JSON.

Uso:
    python3 herramientas/generar_presentacion_lengua.py lengua/apuntes/presentaciones/tema-01.json lengua/pdfs/tema-01-ortografia.pdf [--html]

Misma estructura y mismos estilos que las presentaciones de Matemáticas (design system v2, variante rosa):
  portada · qué vas a ver · conceptos (una idea por diapositiva) · ejemplos resueltos (si los hay)
  · «A practicar» · ejercicios · «a continuación tienes las soluciones» · soluciones · cierre
Sin pie de página y sin datos que cambien al añadir contenido (nada de «tema 1 de 2»).

Diferencias con Matemáticas (no hay fórmulas ni cálculos que verificar):
  · los conceptos son de tipo «definiciones», «comparacion», «regla» o «tabla»;
  · los ejercicios son de tipo «palabras», «situacion» o «frases», cada uno con su solución.
Los estilos salen de css/variables.css, css/componentes.css, css/diapositivas.css y css/diapositivas-lengua.css.
Necesita playwright (Chromium).
"""
import json
import sys
from html import escape
from pathlib import Path

from playwright.sync_api import sync_playwright

sys.path.insert(0, str(Path(__file__).resolve().parent))
from generar_presentacion import cabecera, etiquetas, marca, slide  # noqa: E402  (mismos bloques que Matemáticas)

RAIZ = Path(__file__).resolve().parent.parent
VARIANTE = "lengua"   # color de la materia: rosa rojizo
CSS = ("variables.css", "componentes.css", "diapositivas.css", "diapositivas-lengua.css")


def e(txt):
    return escape(str(txt))


def pildora(txt, clara=False):
    return f'<span class="ds-slide__pildora{" ds-slide__pildora--clara" if clara else ""}">{e(txt)}</span>'


# ---------- Conceptos ----------

def concepto_definiciones(c):
    items = c["items"]
    doble = len(items) > 3
    filas = []
    for it in items:
        regla = f'<b>{e(it["regla"])}</b>' if it.get("regla") else ""
        if doble:   # rejilla de 2 columnas: término arriba y explicación debajo, en una sola tarjeta
            filas.append(f'<div class="ds-slide__def"><div class="ds-slide__card2 ds-slide__card2--menta"><span class="ds-slide__termino">{e(it["t"])}</span><div class="ds-slide__texto">{e(it["d"])}{regla}</div></div></div>')
        else:
            filas.append(f'<div class="ds-slide__def"><div class="ds-slide__card2 ds-slide__card2--menta"><span class="ds-slide__termino">{e(it["t"])}</span></div>'
                         f'<div class="ds-slide__card2"><div class="ds-slide__texto">{e(it["d"])}{regla}</div></div></div>')
    return f'<div class="ds-slide__defs{" ds-slide__defs--2" if doble else ""}">' + "".join(filas) + "</div>"


def concepto_comparacion(c):
    tarjetas = []
    for k, it in enumerate(c["items"]):
        cls = "ds-slide__card2--menta" if k == 0 else "ds-slide__card2--formula"
        grande = f'<div class="ds-slide__grande">{e(it["grande"])}</div>' if it.get("grande") else ""
        texto = f'<div class="ds-slide__texto">{e(it["texto"])}</div>' if it.get("texto") else ""
        cita = f'<div class="ds-slide__cita">{e(it["ejemplo"])}</div>' if it.get("ejemplo") else ""
        tarjetas.append(f'<div class="ds-slide__card2 {cls}">{pildora(it["etiqueta"])}{grande}{texto}{cita}</div>')
    return '<div class="ds-slide__duo">' + "".join(tarjetas) + "</div>"


def concepto_regla(c):
    partes = [f'<div class="ds-slide__card2 ds-slide__card2--menta">{pildora(c.get("etiqueta", "Concepto"))}<div class="ds-slide__enun-regla">{e(c["enunciado"])}</div></div>']
    if c.get("puntos"):
        pts = []
        for p in c["puntos"]:
            pts.append(f'<div class="ds-slide__punto"><b>{e(p["etiqueta"])}</b> → {e(p["texto"])}</div>' if isinstance(p, dict) else f'<div class="ds-slide__punto">{e(p)}</div>')
        partes.append('<div class="ds-slide__puntos">' + "".join(pts) + "</div>")
    if c.get("nota"):
        partes.append(f'<div class="ds-slide__nota">{e(c["nota"])}</div>')
    if c.get("chips"):
        partes.append(f'<div class="ds-slide__etq">{pildora(c.get("chips_etiqueta", "Ejemplos"), True)}<div class="ds-slide__palabras ds-slide__palabras--sm">' + "".join(f'<span class="ds-slide__palabra">{e(x)}</span>' for x in c["chips"]) + "</div></div>")
    return "".join(partes)


def tabla(cab, filas, compacta=False):
    th = "".join(f"<th>{e(x)}</th>" for x in cab)
    tr = "".join("<tr>" + "".join(f"<td>{e(x)}</td>" for x in f) + "</tr>" for f in filas)
    return f'<table class="ds-slide__tabla ds-slide__tabla--lista{" ds-slide__tabla--compacta" if compacta else ""}"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table>'


def concepto_tabla(c):
    intro = f'<div class="ds-slide__card2 ds-slide__card2--menta ds-slide__card2--sm">{pildora(c.get("etiqueta", "Concepto"))}<div class="ds-slide__enun-regla">{e(c["enunciado"])}</div></div>' if c.get("enunciado") else ""
    return intro + tabla(c["cab"], c["filas"], compacta=True)


CONCEPTOS = {"definiciones": concepto_definiciones, "comparacion": concepto_comparacion, "regla": concepto_regla, "tabla": concepto_tabla}


# ---------- Ejercicios y soluciones ----------

def enunciado(txt, grande=False, sm=False):
    return f'<div class="ds-slide__card2 ds-slide__card2--menta{" ds-slide__card2--sm" if sm else ""}">{pildora("Enunciado")}<div class="ds-slide__enun2{" ds-slide__enun2--grande" if grande else ""}">{e(txt)}</div></div>'


def ejercicio(x):
    if x["tipo"] == "palabras":
        palabras = '<div class="ds-slide__palabras">' + "".join(f'<span class="ds-slide__palabra">{e(p)}</span>' for p in x["palabras"]) + "</div>"
        return enunciado(x["enunciado"]) + f'<div class="ds-slide__card2">{pildora("Palabras", True)}{palabras}</div>'
    if x["tipo"] == "situacion":
        pistas = '<div class="ds-slide__etq">' + pildora("Identifica", True) + '<div class="ds-slide__palabras ds-slide__palabras--sm">' + "".join(f'<span class="ds-slide__palabra">{e(p)}</span>' for p in x["identifica"]) + "</div></div>"
        return enunciado(x["enunciado"], grande=True) + pistas
    filas = "".join(f'<div class="ds-slide__frase"><i>{e(l)}</i><span>{e(f)}</span></div>' for l, f, _ in x["items"])
    return enunciado(x["enunciado"], sm=True) + f'<div class="ds-slide__frases">{filas}</div>'


def solucion(x):
    if x["tipo"] == "frases":
        filas = "".join(f'<div class="ds-slide__frase"><i>{e(l)}</i><span>{e(f)}</span><b>{e(r)}</b></div>' for l, f, r in x["items"])
        return f'<div class="ds-slide__frases">{filas}</div>'
    cab = tabla(x["cab"], x["filas"], compacta=(x["tipo"] == "situacion" or len(x["filas"]) > 6))
    if x["tipo"] == "situacion":
        return f'<div class="ds-slide__card2 ds-slide__card2--menta">{pildora("Situación")}<div class="ds-slide__texto">{e(x["enunciado"])}</div></div>' + cab
    return cab


def verificar(t):
    """Comprobaciones de estructura (en Lengua no hay cálculos): cada ejercicio tiene todo lo que su tipo necesita."""
    n = 0
    for k in t.get("conceptos", []):
        if k["tipo"] not in CONCEPTOS:
            sys.exit(f"ERROR: tipo de concepto desconocido «{k['tipo']}» en «{k['titulo']}»")
        n += 1
    for x in t["ejercicios"]:
        if x["tipo"] in ("palabras", "situacion"):
            if x["tipo"] == "palabras" and [f[0].lower() for f in x["filas"]] != [p.lower() for p in x["palabras"]]:
                sys.exit(f"ERROR: en «{x['titulo']}» las palabras del enunciado y las filas de la solución no coinciden")
            if any(len(f) != len(x["cab"]) for f in x["filas"]):
                sys.exit(f"ERROR: en «{x['titulo']}» alguna fila no tiene {len(x['cab'])} columnas")
        elif x["tipo"] != "frases":
            sys.exit(f"ERROR: tipo de ejercicio desconocido «{x['tipo']}»")
        n += 1
    return n


def construir(t):
    S = []
    n = 0
    sec = len(t["conceptos"]) + 1   # número de sección tras los conceptos (igual que en Matemáticas)
    sec_ej = sec if t.get("ejemplos") else None
    sec_ejer = sec + (1 if t.get("ejemplos") else 0)
    sec_sol = sec_ejer + 1

    def add(clase, interior, oscuro=False):
        nonlocal n
        n += 1
        S.append(slide(clase, interior, n, oscuro))

    extras = (["Ejemplos resueltos"] if t.get("ejemplos") else []) + [f"{len(t['ejercicios'])} ejercicios para practicar", "Soluciones de los ejercicios"]
    add("ds-slide--portada", marca(t["marca"]) + etiquetas(t) + f'<h1>{e(t["titulo"])}</h1><p class="ds-slide__lead">{e(t["lead"])}</p><span class="ds-slide__rayas"></span>', True)
    add("", cabecera("Antes de empezar", "Qué vas a ver") + '<div class="ds-slide__body"><ol class="ds-slide__lista">' + "".join(f"<li>{e(x)}</li>" for x in t["vas_a_ver"] + extras) + "</ol></div>")
    for i, c in enumerate(t["conceptos"], 1):
        add("", cabecera(c.get("tag", "El concepto"), c["titulo"], i) + '<div class="ds-slide__body">' + CONCEPTOS[c["tipo"]](c) + "</div>")
    for i, x in enumerate(t.get("ejemplos", []), 1):
        add("", cabecera("Ejemplo", x["titulo"], f"{sec_ej:02d}.{i}") + '<div class="ds-slide__body">' + tabla(x["cab"], x["filas"], compacta=len(x["filas"]) > 6) + "</div>")
    add("ds-slide--portada", marca("?") + etiquetas(t, "Ejercicios") + f'<h1>A practicar</h1><p class="ds-slide__lead">Ahora te toca a ti. Resuelve los {len(t["ejercicios"])} ejercicios.</p><span class="ds-slide__rayas"></span>', True)
    for i, x in enumerate(t["ejercicios"], 1):
        add("", cabecera("Ejercicio", x["titulo"], f"{sec_ejer:02d}.{i}") + '<div class="ds-slide__body">' + ejercicio(x) + "</div>")
    add("ds-slide--negra", marca("✓") + etiquetas(t, "Soluciones") + '<h1>A continuación tienes las soluciones</h1><p class="ds-slide__lead">Intenta resolver los ejercicios antes de mirarlas.</p><span class="ds-slide__rayas"></span>', True)
    for i, x in enumerate(t["ejercicios"], 1):
        add("", cabecera("Solución · Ejercicio", x["titulo"], f"{sec_sol:02d}.{i}") + '<div class="ds-slide__body">' + solucion(x) + "</div>")
    add("ds-slide--cierre", marca(t["marca"]) + etiquetas(t) + '<h1>Tema completado</h1><p class="ds-slide__lead">Repasa los conceptos y vuelve a intentar los ejercicios.</p><span class="ds-slide__rayas"></span>', True)
    return S


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) != 2:
        sys.exit(__doc__)
    t = json.loads(Path(args[0]).read_text(encoding="utf-8"))
    print(verificar(t), "bloques comprobados")
    css = "\n".join((RAIZ / "css" / f).read_text(encoding="utf-8") for f in CSS)
    html = (f'<!doctype html><html lang="es" data-variante="{VARIANTE}"><head><meta charset="utf-8"><title>{e(t["titulo"])}</title>'
            f'<style>{css}</style></head><body class="ds-slides">' + "\n".join(construir(t)) + "</body></html>")
    salida = Path(args[1])
    salida.parent.mkdir(parents=True, exist_ok=True)
    if "--html" in sys.argv:
        salida.with_suffix(".html").write_text(html, encoding="utf-8")
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1280, "height": 720})
        pg.set_content(html)
        pg.wait_for_timeout(300)
        desbordadas = pg.evaluate("""() => [...document.querySelectorAll('.ds-slide')].map((s, i) => [i + 1, (!s.matches('.ds-slide--portada,.ds-slide--cierre,.ds-slide--negra') && s.scrollHeight > s.clientHeight + 1) || [...s.querySelectorAll('.ds-slide__body')].some(b => b.scrollHeight > b.clientHeight + 1)]).filter(x => x[1]).map(x => x[0])""")
        if desbordadas:
            print("AVISO: diapositivas con contenido que no cabe:", desbordadas)
        pg.pdf(path=str(salida), width="1280px", height="720px", print_background=True, prefer_css_page_size=True)
        b.close()
    print("Generado", salida, "·", len(construir(t)), "diapositivas")


if __name__ == "__main__":
    main()
