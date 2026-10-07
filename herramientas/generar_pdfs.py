#!/usr/bin/env python3
"""Convierte los apuntes transcritos (.md con etiquetas) en un PDF A4 por apartado.

Uso:
    python3 herramientas/generar_pdfs.py matematicas/apuntes/apuntes-matematicas.md matematicas/pdfs

Necesita: pandoc (fórmulas LaTeX -> MathML) y playwright con Chromium (HTML -> PDF).
Estilo: design system «Curso de Matemáticas» v1.1 (css/variables.css y css/componentes.css).
"""
import re
import subprocess
import sys
import unicodedata
from functools import lru_cache
from html import escape
from pathlib import Path

from playwright.sync_api import sync_playwright

sys.path.insert(0, str(Path(__file__).parent))
import graficas  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent
CSS_DS = RAIZ / "css"
NOMBRES = {1: "porcentajes", 2: "cantidades-iniciales-y-finales", 3: "porcentaje-de-un-total",
           4: "variacion-absoluta-y-porcentual", 5: "interes-simple", 6: "interes-compuesto",
           7: "proporcionalidad", 8: "despejar-incognitas", 9: "tablas-y-frecuencias",
           10: "representaciones-graficas"}
TOTAL_TEMAS = 10


# ---------------------------------------------------------------- fórmulas
@lru_cache(maxsize=None)
def mathml(tex, bloque):
    tex = tex.replace("{,}", "\\text{,}")
    tex = re.sub(r"([=(]|\\Rightarrow)\s*-(?=\d|\\)", r"\1 \\mathord{-}", tex)
    entrada = f"$${tex}$$" if bloque else f"${tex}$"
    r = subprocess.run(["pandoc", "-f", "markdown", "-t", "html", "--mathml"], input=entrada,
                       capture_output=True, text=True, check=True)
    s = r.stdout.strip()
    s = re.sub(r"^<p>|</p>$", "", s)
    s = re.sub(r"<annotation[^>]*>.*?</annotation>", "", s, flags=re.S)
    s = re.sub(r"</?semantics>", "", s)
    return s


def trocear(tex):
    """Parte una fórmula larga en trozos en los \\qquad / \\quad de nivel superior."""
    trozos, prof, ini, i = [], 0, 0, 0
    while i < len(tex):
        c = tex[i]
        if c == "{":
            prof += 1
        elif c == "}":
            prof -= 1
        elif prof == 0 and tex.startswith("\\qquad", i):
            trozos.append(tex[ini:i]); i += 6; ini = i; continue
        elif prof == 0 and tex.startswith("\\quad", i) and not tex.startswith("\\quad", i + 5):
            trozos.append(tex[ini:i]); i += 5; ini = i; continue
        i += 1
    trozos.append(tex[ini:])
    def limpio(t):
        t = re.sub(r"^(\\[;,!:]|\s)+|(\\[;,!:]|\s)+$", "", t)
        return t
    return [limpio(t) for t in trozos if limpio(t)]


def formula_bloque(tex):
    return '<div class="mf">' + "".join(f'<span class="mp">{mathml(t, True)}</span>' for t in trocear(tex)) + "</div>"


def texto(s, tabla=False):
    """Texto con $…$ en línea -> HTML con MathML (las fracciones, a tamaño normal fuera de tablas)."""
    partes = re.split(r"(\$[^$]+\$)", s)
    out = []
    for p in partes:
        if p.startswith("$") and p.endswith("$") and len(p) > 2:
            tex = p[1:-1].strip()
            if not tabla:
                tex = re.sub(r"\\frac(?![a-z])", r"\\dfrac", tex)
            out.append(mathml(tex, False))
        else:
            out.append(escape(p))
    return "".join(out)


# ---------------------------------------------------------------- lectura
ETIQ = re.compile(r"^\[([A-ZÁÉÍÓÚÑ ]+)\]\s*(.*)$")


def secciones(lineas):
    res, act = [], None
    for ln in lineas:
        t = ln.strip()
        if t == "[INICIO SECCIÓN]":
            act = []
        elif t == "[FIN SECCIÓN]":
            res.append(act); act = None
        elif act is not None:
            act.append(ln.rstrip("\n"))
    return res


def bloques(lineas):
    nodos, i, n = [], 0, len(lineas)

    def hasta(cierre, i):
        j = i
        while j < n and lineas[j].strip() != cierre:
            j += 1
        return lineas[i:j], j + 1

    while i < n:
        t = lineas[i].strip()
        i += 1
        if not t:
            continue
        m = ETIQ.match(t)
        if not m:
            nodos.append(("p", t)); continue
        et, resto = m.group(1), m.group(2).strip()
        if et in ("EJEMPLO", "MÉTODO ALTERNATIVO"):
            dentro, i = hasta(f"[/{et}]", i)
            nodos.append(("ejemplo" if et == "EJEMPLO" else "metodo", bloques(dentro)))
        elif et == "FÓRMULA DESTACADA":
            dentro, i = hasta("[/FÓRMULA DESTACADA]", i)
            forms = [d.strip() for d in dentro if d.strip()]
            nodos.append(("destacada", resto, forms))
        elif et == "TABLA":
            dentro, i = hasta("[/TABLA]", i)
            filas = [[c.strip() for c in d.strip().strip("|").split("|")] for d in dentro
                     if d.strip().startswith("|") and not re.match(r"^\|[\s\-|:]+\|$", d.strip())]
            nodos.append(("tabla", filas))
        elif et in ("LISTA", "LISTA NUMERADA"):
            dentro, i = hasta(f"[/{et}]", i)
            items = [re.sub(r"^(-|\d+\.)\s*", "", d.strip()) for d in dentro if d.strip()]
            nodos.append(("lista", et == "LISTA NUMERADA", items))
        elif et in ("IMAGEN", "DIAGRAMA"):
            clave = Path(resto.split("—")[0].strip()).stem
            nodos.append(("figura", clave))
        elif et == "FÓRMULA":
            nodos.append(("formula", resto))
        elif et == "TEXTO":
            nodos.append(("p", resto))
        elif et == "NOTA":
            nodos.append(("nota", resto))
        elif et == "DESTACADO":
            nodos.append(("destacado", resto))
        elif et == "SUBTÍTULO":
            nodos.append(("h2", resto))
        elif et == "TÍTULO APARTADO":
            nodos.append(("titulo", resto))
        else:
            nodos.append(("p", t))
    return nodos


# ---------------------------------------------------------------- HTML
FIGURAS = graficas.catalogo()
USADAS = set()


def parrafo(s):
    s = re.sub(r"^EJ\.\s*", "", s)
    m = re.search(r"(?:^|\s)R\.\s+(.*)$", s)
    if m:
        antes = s[:m.start()].strip()
        out = f"<p>{texto(antes)}</p>" if antes else ""
        return out + f'<p class="resp"><strong>Respuesta:</strong> {texto(m.group(1))}</p>'
    return f"<p>{texto(s)}</p>"


def callout(clase, titulo, cuerpo):
    t = f'<span class="ds-callout__t">{escape(titulo)}</span>' if titulo else ""
    return f'<div class="ds-callout ds-callout--{clase}"><div class="cb">{t}{cuerpo}</div></div>'


def tabla(filas):
    def num(c):
        return bool(re.fullmatch(r"[\d.,\s%€−-]*\d[\d.,\s%€]*", c)) and c != ""
    cab, cuerpo = filas[0], filas[1:]
    h = "<tr>" + "".join(f'<th scope="col"{" class=n" if num(c) else ""}>{texto(c, True)}</th>' for c in cab) + "</tr>"
    b = ""
    for f in cuerpo:
        celdas = ""
        for k, c in enumerate(f):
            if k == 0 and not num(c) and c:
                celdas += f'<th scope="row">{texto(c, True)}</th>'
            else:
                celdas += f'<td{" class=n" if num(c) else ""}>{texto(c, True)}</td>'
        b += f"<tr>{celdas}</tr>"
    return f'<div class="ds-table-wrap"><table class="ds-table ds-table--zebra"><thead>{h}</thead><tbody>{b}</tbody></table></div>'


def render(nodos, en_ejemplo=False):
    out = []
    for k, nd in enumerate(nodos):
        tipo = nd[0]
        if tipo == "p":
            out.append(parrafo(nd[1]))
        elif tipo == "formula":
            out.append(formula_bloque(nd[1]))
        elif tipo == "h2":
            out.append(f"<h2>{texto(nd[1])}</h2>")
        elif tipo == "nota":
            out.append(callout("info", "Nota", f"<p>{texto(nd[1])}</p>"))
        elif tipo == "destacado":
            out.append(callout("atencion", "", f"<p><strong>{texto(nd[1])}</strong></p>"))
        elif tipo == "tabla":
            out.append(tabla(nd[1]))
        elif tipo == "lista":
            tag = "ol" if nd[1] else "ul"
            out.append(f"<{tag}>" + "".join(f"<li>{texto(x)}</li>" for x in nd[2]) + f"</{tag}>")
        elif tipo == "figura":
            titulo, svg = FIGURAS[nd[1]]
            USADAS.add(nd[1])
            out.append(f'<figure>{svg}<figcaption>{escape(titulo)}</figcaption></figure>')
        elif tipo == "destacada":
            etiqueta, forms = nd[1], nd[2]
            clase = "important" if etiqueta.startswith("¡") else "definicion"
            titulo = etiqueta or "Fórmula"
            out.append(callout(clase, titulo, "".join(formula_bloque(f) for f in forms)))
        elif tipo == "metodo":
            hijos = nd[1]
            titulo = "Cómo lo haría yo"
            if hijos and hijos[0][0] == "p" and hijos[0][1].lower().startswith("cómo lo haría yo"):
                hijos = hijos[1:]
            out.append(callout("tip", titulo, render(hijos, True)))
        elif tipo == "ejemplo":
            hijos = nd[1]
            titulo = "Ejemplo"
            if hijos and hijos[0][0] == "p":
                m = re.match(r"^(\d+)\.\s+(.*)$", hijos[0][1])
                if m:
                    titulo = f"Ejercicio {m.group(1)}"
                    hijos = [("p", m.group(2))] + hijos[1:]
            out.append(callout("ejemplo", titulo, render(hijos, True)))
        elif tipo == "titulo":
            pass
    return "".join(out)


def leer_tokens():
    css = (CSS_DS / "variables.css").read_text(encoding="utf-8")
    ligero = css.split("@media")[0]
    g = lambda nombre: re.search(rf"--{nombre}:\s*([^;]+);", ligero).group(1).strip()
    return {"txt2": g("color-text-secondary"), "borde": g("color-border-default"), "marca": g("color-action-primary-bg")}


CSS_PDF = """
@page{size:A4;margin:22mm 20mm}
html{background:var(--color-bg-page)}
body{margin:0;font:400 11pt/16pt var(--font-family-body);color:var(--color-text-primary);-webkit-print-color-adjust:exact;print-color-adjust:exact}
h1{font:600 28pt/34pt var(--font-family-heading);margin:2mm 0 6mm}
p:has(+ .ds-table-wrap),p:has(+ figure),p:has(+ .ds-callout),h2:has(+ p + .ds-callout){break-after:avoid}
h2{font:600 20pt/26pt var(--font-family-heading);margin:9mm 0 3mm;break-after:avoid}
p{margin:0 0 3mm;max-width:none}
ul,ol{margin:0 0 3mm;padding-left:6mm}li{margin:0 0 1.5mm}
.cb{flex:1;min-width:0}
.ds-callout{break-inside:avoid;margin:4mm 0}
.ds-callout .ds-callout__t{font-size:10pt;line-height:14pt;margin-bottom:2mm}
.ds-callout p:last-child{margin-bottom:0}
.mf{display:flex;flex-wrap:wrap;justify-content:center;align-items:center;gap:2mm 9mm;margin:3mm 0;break-inside:avoid}
.mp{display:block}
math{font-family:"Latin Modern Math","DejaVu Math TeX Gyre",var(--font-family-heading);font-size:12.5pt}
p math,li math,td math,th math{font-size:11.5pt}
.resp{margin-top:2mm}
figure{margin:4mm 0;text-align:center;break-inside:avoid}
figure svg{width:100%;max-width:140mm;height:auto}
figcaption{font-size:9pt;line-height:13pt;color:var(--color-text-secondary);margin-top:1mm}
.ds-table-wrap{margin:4mm 0;break-inside:avoid;overflow:visible}
.ds-table{min-width:0;font-size:10pt}
.ds-table th,.ds-table td{padding:2mm 3mm}
.ds-table th.n,.ds-table td.n{text-align:right}
.ds-table th[scope=row]{background:transparent;border-bottom:var(--border-hairline) solid var(--color-border-default);font-weight:600}
.ds-table th{position:static}
.p-antes-tabla{break-after:avoid}
.ds-callout--ejemplo .ds-table-wrap{background:var(--color-bg-page)}
"""


def pagina(num, titulo, cuerpo):
    sprite = ""
    return f"""<!DOCTYPE html><html lang="es" data-theme="light"><head><meta charset="utf-8">
<title>Tema {num}: {escape(titulo)} · Matemáticas aplicadas</title>
<link rel="stylesheet" href="{(CSS_DS / 'variables.css').as_uri()}">
<link rel="stylesheet" href="{(CSS_DS / 'componentes.css').as_uri()}">
<style>{CSS_PDF}</style></head><body>
<span class="ds-label">Tema {num} de {TOTAL_TEMAS}</span>
<h1>{escape(titulo)}</h1>
{cuerpo}
</body></html>"""


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    md, salida = Path(sys.argv[1]), Path(sys.argv[2])
    salida.mkdir(parents=True, exist_ok=True)
    secs = secciones(md.read_text(encoding="utf-8").splitlines())
    global TOTAL_TEMAS
    TOTAL_TEMAS = len(secs)
    tk = leer_tokens()
    cab = (f'<div style="font:8pt Inter,sans-serif;color:{tk["txt2"]};width:100%;padding:0 20mm;display:flex;justify-content:space-between;'
           f'box-sizing:border-box"><span>Matemáticas aplicadas · Apuntes</span><span>@@T@@</span></div>')
    pie = (f'<div style="font:8pt Inter,sans-serif;color:{tk["txt2"]};width:100%;padding:0 20mm;display:flex;justify-content:space-between;'
           f'box-sizing:border-box"><span>Acceso a grado superior</span><span>Página <span class="pageNumber"></span> de <span class="totalPages"></span></span></div>')
    avisos = []
    with sync_playwright() as p:
        nav = p.chromium.launch()
        for nodos_src in secs:
            nodos = bloques(nodos_src)
            tit = next(n[1] for n in nodos if n[0] == "titulo")
            m = re.match(r"^(\d+)\.\s*(.*)$", tit)
            num, titulo = int(m.group(1)), m.group(2)
            cuerpo = render([n for n in nodos if n[0] != "titulo"])
            html = pagina(num, titulo, cuerpo)
            nombre = f"tema-{num:02d}-{NOMBRES[num]}"
            (salida / f"{nombre}.html").write_text(html, encoding="utf-8")
            pg = nav.new_page()
            pg.goto((salida / f"{nombre}.html").as_uri())
            pg.wait_for_timeout(300)
            desb = pg.evaluate("""() => [...document.querySelectorAll('.mp, .ds-table, figure svg')]
                .filter(e => e.scrollWidth > e.parentElement.clientWidth + 1)
                .map(e => e.className || e.tagName)""")
            if desb:
                avisos.append((nombre, desb))
            pg.pdf(path=str(salida / f"{nombre}.pdf"), prefer_css_page_size=True, print_background=True,
                   display_header_footer=True, header_template=cab.replace("@@T@@", escape(f"Tema {num} · {titulo}")),
                   footer_template=pie, tagged=True, outline=True)
            pg.close()
            print("OK", nombre)
        nav.close()
    for nombre, d in avisos:
        print("AVISO desbordamiento", nombre, d)


if __name__ == "__main__":
    main()
