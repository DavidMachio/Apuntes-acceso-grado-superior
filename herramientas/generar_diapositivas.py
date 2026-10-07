#!/usr/bin/env python3
"""Genera diapositivas PDF horizontales (16:9) por tema a partir de los apuntes etiquetados.

Uso:
    python3 herramientas/generar_diapositivas.py matematicas/apuntes/apuntes-matematicas.md SALIDA [N ...]

Estructura: portada · de qué va el tema · fórmulas clave · conceptos y un ejemplo por diapositiva · resumen · cierre.
Reutiliza el análisis de generar_pdfs.py. Necesita pandoc y playwright (Chromium).
"""
import re
import sys
from html import escape
from pathlib import Path

from playwright.sync_api import sync_playwright

sys.path.insert(0, str(Path(__file__).parent))
import generar_pdfs as G  # noqa: E402
import infografias  # noqa: E402

RAIZ, CSS_DS = G.RAIZ, G.CSS_DS
MARRONES = {50: "#faf7f4", 100: "#f3ede6", 200: "#e4d9cc", 300: "#cdbba7", 400: "#a8927c", 500: "#84705c",
            600: "#6a5846", 700: "#504236", 800: "#382e26", 900: "#231c17"}

CSS = ":root{" + "".join(f"--marron-{k}:{v};" for k, v in MARRONES.items()) + """}
@page{size:1280px 720px;margin:0}
html,body{margin:0;background:var(--marron-50)}
body{font-family:var(--font-family-body);-webkit-print-color-adjust:exact;print-color-adjust:exact;color:var(--marron-900)}
.slide{--s:1;width:1280px;height:720px;position:relative;overflow:hidden;break-after:page;display:flex;flex-direction:column;background:var(--marron-50)}
.sl-head,.sl-foot{flex:none;display:flex;align-items:center;justify-content:space-between;padding:0 64px;font-size:19px;font-weight:600}
.sl-head{height:58px;background:linear-gradient(90deg,var(--color-primary-800) 0%,var(--color-primary-700) 30%,var(--color-primary-300) 100%);color:#fff}
.sl-head .r{color:var(--color-primary-900)}
.sl-foot{height:46px;background:linear-gradient(90deg,var(--color-primary-300) 0%,var(--color-primary-700) 70%,var(--color-primary-800) 100%);color:var(--color-primary-900);font-size:17px}
.sl-foot .r{color:#fff}
.sl-body{flex:1;min-height:0;padding:26px 64px 30px;overflow:hidden;font-size:calc(27px*var(--s));line-height:1.38;position:relative;display:flex;flex-direction:column}
.sl-body>*{flex-shrink:0}
.main{flex:1 1 auto;min-height:0;display:flex;flex-direction:column}.main>:first-child{margin-top:auto!important}.main>:last-child{margin-bottom:auto!important}
.eb{font-size:18px;font-weight:700;letter-spacing:.09em;text-transform:uppercase;color:var(--color-primary-700);margin:0 0 6px}
h2.t{font:700 calc(46px*var(--s))/1.1 var(--font-family-heading);margin:0 0 18px;color:var(--marron-900)}
.sl-body p{margin:0 0 16px;max-width:none}
.sl-body ul,.sl-body ol{margin:0 0 12px;padding-left:30px}.sl-body li{margin:0 0 8px}
.mf{display:flex;flex-wrap:wrap;justify-content:center;align-items:center;gap:12px 48px;margin:14px 0}
.mp{display:block}
math{font-family:"Latin Modern Math","DejaVu Math TeX Gyre",var(--font-family-heading);font-size:1.02em}
p math,li math,td math{font-size:1em}
.cb{flex:1;min-width:0}
.ds-callout{break-inside:avoid;margin:18px 0;font-size:1em;padding:18px 24px}
.ds-callout .ds-callout__t{font-size:.7em;line-height:1.3;margin-bottom:6px}
.ds-callout p:last-child{margin-bottom:0}
.resp{display:inline-block;background:var(--color-primary-100);border:2px solid var(--color-primary-500);border-radius:12px;padding:6px 16px;margin-top:8px}
figure{margin:8px 0;text-align:center}figure svg{max-height:290px;width:auto;max-width:100%}
figcaption{font-size:.62em;color:var(--marron-600)}
.ds-table{font-size:.85em}.ds-table th,.ds-table td{padding:8px 14px}
.enun{background:#fff;border:2px solid var(--marron-200);border-left:10px solid var(--color-primary-500);border-radius:16px;padding:16px 24px;margin:0 0 18px;font-size:1.06em;box-shadow:0 6px 18px rgba(56,46,38,.07)}
.enun p:last-child{margin:0}
.sol-t{font-size:.66em;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--marron-600);margin:4px 0 2px}
.cols{display:grid;grid-template-columns:1fr 1fr;gap:36px;align-items:center;margin:auto 0}
.card{background:#fff;border:2px solid var(--marron-200);border-radius:20px;padding:20px 26px;box-shadow:0 8px 22px rgba(56,46,38,.08)}
.chips{list-style:none;padding:0;margin:0;counter-reset:c}
.chips li{counter-increment:c;display:flex;align-items:center;gap:16px;background:#fff;border:2px solid var(--marron-200);border-radius:16px;padding:12px 20px;margin:0 0 12px;font-weight:600}
.chips li::before{content:counter(c);flex:none;width:40px;height:40px;border-radius:50%;background:var(--color-primary-500);color:var(--color-primary-900);display:grid;place-items:center;font-weight:700}
.grid{display:grid;grid-template-columns:1fr;gap:16px;flex:1;align-content:center}
.fc{background:#fff;border:2px solid var(--marron-200);border-top:8px solid var(--color-primary-500);border-radius:18px;padding:12px 22px 10px;display:flex;flex-direction:column;justify-content:center}
.fc .eb{margin:0}
.fc .mf{margin:6px 0 2px}
.rec li{font-size:.92em}
/* pasos de una solución */
.paso{display:flex;align-items:center;gap:20px;background:#fff;border:2px solid var(--marron-200);border-radius:16px;padding:10px 22px;margin:0 0 16px;box-shadow:0 4px 14px rgba(56,46,38,.06)}
.paso>.n{flex:none;width:38px;height:38px;border-radius:50%;background:var(--color-primary-500);color:var(--color-primary-900);display:grid;place-items:center;font-weight:700;font-size:.7em}
.paso>.c{flex:1;min-width:0}.paso .mf{margin:2px 0}
.enun{font-size:1.1em;font-weight:500}
.rec2{margin:0 0 18px;color:var(--marron-700);font-size:.88em}
.vis{display:grid;grid-template-columns:1.25fr 1fr;gap:36px;align-items:center;margin:auto 0}
.vis .card svg{width:100%;max-height:330px;height:auto;display:block}
/* ejemplos y resumen como explicación */
.lbl{font-size:.62em;font-weight:700;letter-spacing:.09em;text-transform:uppercase;color:var(--marron-600);margin:0 0 6px}
.bloque{background:#fff;border:2px solid var(--marron-200);border-radius:18px;padding:14px 26px;margin:0 0 16px;box-shadow:0 4px 14px rgba(56,46,38,.06)}
.bloque.preg{border-left:10px solid var(--color-primary-500);font-size:1.08em}
.bloque.preg p{margin:0}
.bloque.apl{background:var(--color-primary-50);border-color:var(--color-primary-300)}
.bloque .mf{margin:6px 0}
.rec2 b{color:var(--marron-800)}
.desc{font-size:1.12em;color:var(--marron-700);margin:0 0 22px;max-width:1000px}
.big{border-top:10px solid var(--color-primary-500);padding:34px 36px}
.big .mf{font-size:1.55em;margin:16px 0}
.rec li{font-size:1em;margin-bottom:16px}
.rcols{grid-template-columns:1.1fr 1fr;align-items:start}.rcols .bloque{margin:0}.rcols .bloque p{margin:0 0 6px}
/* colores de la materia: menta y marrón (sin magenta) */
.slide .ds-callout--definicion,.slide .ds-callout--important{background:var(--color-primary-100);border-color:var(--color-primary-600);color:var(--marron-900)}
.slide .ds-callout--tip{background:var(--marron-100);border-color:var(--marron-400);color:var(--marron-900)}
.slide .ds-callout--ejemplo{background:#fff;border-color:var(--color-primary-500);color:var(--marron-900)}
.slide .ds-callout--info,.slide .ds-callout--atencion{background:var(--marron-100);border-color:var(--marron-500);color:var(--marron-900)}
/* portadas */
.cover{background:linear-gradient(150deg,var(--color-primary-900) 0%,#1d2f26 55%,#14201a 100%);color:#fff;justify-content:center}
.cover::before{content:"";position:absolute;inset:0;opacity:.5;background-image:linear-gradient(rgba(255,255,255,.05) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.05) 1px,transparent 1px);background-size:48px 48px;mask-image:linear-gradient(#000,transparent 90%)}
.cover .marca{position:absolute;right:0;top:0;height:100%;width:auto}
.cover .in{position:relative;padding:0 96px;max-width:700px}
.cover .tag{display:inline-block;border:2px solid var(--color-primary-400);color:var(--color-primary-200);border-radius:999px;padding:6px 20px;font-size:19px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;margin-bottom:26px}
.cover h1{font:700 76px/1.05 var(--font-family-heading);margin:0 0 22px;color:#fff}
.cover .lead{font-size:30px;line-height:1.35;color:var(--color-primary-200);margin:0 0 34px}
.cover .pills{display:flex;gap:12px;flex-wrap:wrap}
.cover .pill{background:rgba(255,255,255,.1);border:1.5px solid rgba(255,255,255,.25);border-radius:999px;padding:8px 20px;font-size:20px;color:#fff}
"""

JS = """
const over=[];
document.querySelectorAll('.slide').forEach((sl,i)=>{const b=sl.querySelector('.sl-body');if(!b)return;
 let s=1.05;sl.style.setProperty('--s',s);
 const bad=()=>Math.max(0,...[...b.querySelectorAll('.paso,.enun,.ds-callout,.card,.fc,.resp,figure,p,li,math,.mf,.chips,.rec2')].map(e=>e.getBoundingClientRect().bottom))>b.getBoundingClientRect().bottom-28||[...b.querySelectorAll('.mp,.ds-table,.fc')].some(e=>e.scrollWidth>e.clientWidth+6||e.getBoundingClientRect().right>b.getBoundingClientRect().right-40);
 while(bad()&&s>0.84){s-=0.04;sl.style.setProperty('--s',s.toFixed(2));}
 if(bad())over.push(i);});
window.__over=over;
"""


# ------------------------------------------------------------- slides
class S:
    def __init__(self, tipo, **kw):
        self.tipo, self.kw = tipo, kw


def construir(nodos, num, titulo, meta=None):
    """Devuelve la lista de diapositivas de contenido y los datos para resumen."""
    cuerpo, destacadas, notas, subs = [], [], [], []
    sub, grupo, n_ej = None, [], 0

    def volcar():
        nonlocal grupo
        util = [g for g in grupo if g[0] != "destacada"] if grupo else []
        if grupo and (util or True):
            if util:
                cuerpo.append(S("concepto", sub=sub or titulo, nodos=grupo, num=num))
        grupo = []

    for nd in nodos:
        t = nd[0]
        if t == "h2":
            volcar(); sub = nd[1]; subs.append(sub)
        elif t == "ejemplo":
            volcar(); n_ej += 1
            em = (meta or {}).get("ejemplos", [])
            e = S("ejemplo", sub=sub, hijos=nd[1], n=n_ej, meta=em[n_ej - 1] if n_ej <= len(em) else None)
            if e.kw["meta"] and e.kw["meta"].get("pregunta") and len(e.kw["meta"].get("aplica", [])) + len(desarrollo_nodos(e)) >= 4:
                cuerpo.append(S("ejemplo", **{**e.kw, "parte": "plan"}))
                cuerpo.append(S("ejemplo", **{**e.kw, "parte": "desarrollo"}))
            else:
                cuerpo.append(e)
        else:
            if t == "destacada":
                destacadas.append((sub, nd[1], nd[2]))
            if t in ("nota", "destacado"):
                notas.append(nd[1])
            grupo.append(nd)
    volcar()
    return cuerpo, destacadas, notas, subs


def marco(i, total, num, titulo, cuerpo_html, clase=""):
    return (f'<section class="slide {clase}"><header class="sl-head"><span>Matemáticas aplicadas</span>'
            f'<span class="r">{escape(titulo)}</span></header><div class="sl-body">{cuerpo_html}</div>'
            '</section>')


def portada(num, total_t, titulo, resumen, ejercicios, formulas):
    pills = "".join(f'<span class="pill">{escape(x)}</span>' for x in
                    (f"{ejercicios} ejemplos", f"{formulas} fórmulas clave"))
    return (f'<section class="slide cover">{infografias.marca_agua(num)}<div class="in"><span class="tag">Matemáticas aplicadas</span>'
            f'<h1>{escape(titulo)}</h1><p class="lead">{escape(resumen)}</p><div class="pills">{pills}</div></div></section>')


def cierre(num, total_t, titulo, siguiente):
    sig = f"A continuación: tema {num + 1} · {siguiente}" if siguiente else "Has terminado el temario. ¡Ánimo con el examen!"
    return (f'<section class="slide cover">{infografias.marca_agua(num)}<div class="in"><span class="tag">Fin del tema</span>'
            f'<h1>¡Ahora, a practicar!</h1><p class="lead">Genera un examen de «{escape(titulo)}» en la web y comprueba lo que has aprendido.</p>'
            f'</div></section>')


def card_formula(sub, etiqueta, forms, una=False):
    et = escape(etiqueta.strip("¡!") if etiqueta else (sub or "Fórmula"))
    return (f'<div class="fc{" una" if una else ""}"><p class="eb">{et}</p>' + "".join(G.formula_bloque(f) for f in forms) + "</div>")


def html_formulas(destacadas, titulo_h, eb):
    cards = ""
    for k, (sub, et, forms) in enumerate(destacadas):
        cards += card_formula(sub, et or "", forms)
    return f'<p class="eb">{eb}</p><h2 class="t">{titulo_h}</h2><div class="grid">{cards}</div>'


def pasos(nodos):
    out, k = "", 0
    for nd in nodos:
        if nd[0] == "formula":
            k += 1
            out += f'<div class="paso"><span class="n">{k}</span><div class="c">{G.formula_bloque(nd[1])}</div></div>'
        else:
            out += G.render([nd], True)
    return out


def desarrollo_nodos(s):
    meta = s.kw.get("meta") or {}
    if meta.get("pasos"):
        nodos = [("formula", t) for t in meta["pasos"]]
        if meta.get("respuesta"):
            nodos.append(("p", "R. " + meta["respuesta"]))
        return nodos
    h = s.kw["hijos"]
    if h and h[0][0] == "p" and not re.search(r"(?:^|\s)R\.\s", h[0][1]):
        return h[1:]
    return h


def html_ejemplo(s):
    if (s.kw.get("meta") or {}).get("pregunta") and not s.kw.get("cont_old"):
        return html_ejemplo_meta(s)
    return html_ejemplo_old(s)


def html_ejemplo_meta(s):
    meta, n, parte = s.kw["meta"], s.kw["n"], s.kw.get("parte", "todo")
    tit = f"Ejemplo {n}" + (" · desarrollo" if parte == "desarrollo" else "")
    cab = f'<p class="eb">{escape(s.kw["sub"] or "")}</p><h2 class="t">{tit}</h2>'
    preg = f'<div class="bloque preg"><p class="lbl">Planteamiento</p><p>{G.texto(meta["pregunta"])}</p></div>'
    apl = ""
    if meta.get("aplica"):
        apl = ('<div class="bloque apl"><p class="lbl">Fórmulas que aplicamos</p>'
               + "".join(G.formula_bloque(f) for f in meta["aplica"]) + "</div>")
    dev = ""
    nodos = s.kw["dev"] if s.kw.get("dev") is not None else desarrollo_nodos(s)
    if nodos:
        dev = '<p class="sol-t">Desarrollo</p>' + pasos(nodos)
    if parte == "plan":
        cuerpo = preg + apl
    elif parte == "desarrollo":
        cuerpo = f'<p class="rec2"><b>Planteamiento.</b> {G.texto(meta["pregunta"])}</p>' + dev
    else:
        cuerpo = preg + apl + dev
    return cab + f'<div class="main">{cuerpo}</div>'


def html_ejemplo_old(s):
    hijos, n = s.kw["hijos"], s.kw["n"]
    titulo = f"Ejemplo {n}"
    if hijos and hijos[0][0] == "p":
        m = re.match(r"^(\d+)\.\s+(.*)$", hijos[0][1])
        if m:
            titulo = f"Ejercicio {m.group(1)}"; hijos = [("p", m.group(2))] + hijos[1:]
    cab = f'<p class="eb">{escape(s.kw["sub"] or "")}</p><h2 class="t">{titulo}</h2>'
    cola = lambda x: cab + f'<div class="main">{x}</div>'
    if s.kw.get("cont"):
        cab = cab.replace("</h2>", " <small>(sigue)</small></h2>")
    if len(hijos) > 1 and hijos[0][0] == "p" and not re.search(r"(?:^|\s)R\.\s", hijos[0][1]):
        return cola(f'<div class="enun">{G.parrafo(hijos[0][1])}</div><p class="sol-t">Solución</p>' + pasos(hijos[1:]))
    if s.kw.get("cont") and s.kw.get("enun"):
        return cola(f'<p class="rec2">{G.texto(s.kw["enun"])}</p>' + pasos(hijos))
    return cola(pasos(hijos))


USADOS = set()


def html_concepto(s):
    v = infografias.visual(s.kw["num"], s.kw["sub"]) if (s.kw["num"], s.kw["sub"]) not in USADOS and not s.kw.get("cont") else None
    if v:
        USADOS.add((s.kw["num"], s.kw["sub"]))
        return (f'<p class="eb">Concepto</p><h2 class="t">{escape(s.kw["sub"])}</h2><div class="main"><div class="vis"><div>'
                + G.render(s.kw["nodos"]) + f'</div><div class="card">{v}</div></div></div>')
    return f'<p class="eb">Concepto</p><h2 class="t">{escape(s.kw["sub"])}</h2><div class="main">' + G.render(s.kw["nodos"]) + '</div>'


def dividir(s):
    if s.tipo == "ejemplo" and s.kw.get("meta") and s.kw["meta"].get("pregunta"):
        parte = s.kw.get("parte", "todo")
        if parte == "todo":
            return [S("ejemplo", **{**s.kw, "parte": "plan"}), S("ejemplo", **{**s.kw, "parte": "desarrollo"})]
        if parte == "desarrollo":
            d = desarrollo_nodos(s) if s.kw.get("dev") is None else s.kw["dev"]
            if len(d) < 2:
                return [s]
            m = max(1, len(d) // 2)
            return [S("ejemplo", **{**s.kw, "dev": d[:m]}), S("ejemplo", **{**s.kw, "dev": d[m:]})]
        return [s]
    if s.tipo == "ejemplo":
        h = s.kw["hijos"]; mid = max(1, len(h) // 2)
        if len(h) < 2:
            return [s]
        enun = h[0][1] if h and h[0][0] == "p" else ""
        enun = re.sub(r"^(EJ\.\s*|\d+\.\s*)", "", enun)
        return [S("ejemplo", **{**s.kw, "hijos": h[:mid]}), S("ejemplo", **{**s.kw, "hijos": h[mid:], "cont": True, "enun": enun})]
    n = s.kw["nodos"]
    if len(n) < 2:
        return [s]
    mid = max(1, len(n) // 2)
    return [S("concepto", **{**s.kw, "nodos": n[:mid]}), S("concepto", **{**s.kw, "nodos": n[mid:], "cont": True})]


def html_slide(s):
    return html_ejemplo(s) if s.tipo == "ejemplo" else html_concepto(s)


def documento(num, titulo, resumen, total_t, siguiente, cuerpo, destacadas, notas, subs, n_ej, tit_doc):
    trozos = [destacadas[i:i + 3] for i in range(0, len(destacadas), 3)] or []
    paginas = []  # (html, clase)
    paginas.append(("COVER", ""))
    idx = "".join(f"<li>{escape(x)}</li>" for x in subs) or f"<li>{escape(titulo)}</li>"
    paginas.append((f'<p class="eb">En este tema</p><h2 class="t">Qué vas a aprender</h2><div class="main"><div class="cols"><ol class="chips">{idx}</ol>'
                    f'<div class="card">{infografias.infografia(num)}</div></div></div>', ""))
    for k, tr in enumerate(trozos):
        suf = f" ({k + 1}/{len(trozos)})" if len(trozos) > 1 else ""
        paginas.append((html_formulas(tr, "Fórmulas clave" + suf, "Para tener a mano"), ""))
    for s in cuerpo:
        paginas.append((s, ""))
    meta = METAS.get(str(num), {})
    fm = meta.get("formulas", [])
    if destacadas:
        for k, (sub, et, forms) in enumerate(destacadas):
            info = fm[k] if k < len(fm) else {}
            tit = info.get("titulo") or (et.strip("¡!") if et else (sub or "Fórmula"))
            desc = f'<p class="desc">{G.texto(info["descripcion"])}</p>' if info.get("descripcion") else ""
            tarjeta = '<div class="bloque big">' + "".join(G.formula_bloque(f) for f in forms) + "</div>"
            paginas.append((f'<p class="eb">Resumen</p><h2 class="t">{escape(tit)}</h2><div class="main">{desc}{tarjeta}</div>', ""))
    rec = meta.get("recordar") or notas
    if rec:
        li = "".join(f"<li>{G.texto(x)}</li>" for x in rec)
        ej = meta.get("recordar_ejemplo")
        if ej:
            tarjeta = ('<div class="bloque apl"><p class="lbl">Un ejemplo rápido</p>'
                       f'<p>{G.texto(ej["pregunta"])}</p>'
                       + "".join(G.formula_bloque(t) for t in ej["pasos"]) + "</div>")
            cuerpo_r = f'<div class="cols rcols"><ul class="rec">{li}</ul>{tarjeta}</div>'
        else:
            cuerpo_r = f'<ul class="rec">{li}</ul>'
        paginas.append((f'<p class="eb">Para llevarte</p><h2 class="t">Ideas para recordar</h2><div class="main">{cuerpo_r}</div>', ""))
    paginas.append(("END", ""))
    return paginas


def a_html(paginas, num, titulo, resumen, total_t, siguiente, n_ej, n_f):
    total = len(paginas)
    out = []
    for i, (c, clase) in enumerate(paginas, 1):
        if c == "COVER":
            out.append(portada(num, total_t, titulo, resumen, n_ej, n_f))
        elif c == "END":
            out.append(cierre(num, total_t, titulo, siguiente))
        else:
            html = c if isinstance(c, str) else html_slide(c)
            out.append(marco(i, total, num, titulo, html))
    return (f'<!DOCTYPE html><html lang="es" data-theme="light"><head><meta charset="utf-8"><title>Tema {num}: {escape(titulo)}</title>'
            f'<link rel="stylesheet" href="{(CSS_DS / "variables.css").as_uri()}"><link rel="stylesheet" href="{(CSS_DS / "componentes.css").as_uri()}">'
            f'<style>{CSS}</style></head><body>{"".join(out)}<script>{JS}</script></body></html>')


METAS = {}


def main():
    global METAS
    jf = Path(sys.argv[1]).with_name("diapositivas.json") if len(sys.argv) > 1 else None
    if jf and jf.exists():
        import json
        METAS = json.loads(jf.read_text(encoding="utf-8"))
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    md, salida = Path(sys.argv[1]), Path(sys.argv[2])
    solo = {int(x) for x in sys.argv[3:]}
    salida.mkdir(parents=True, exist_ok=True)
    secs = G.secciones(md.read_text(encoding="utf-8").splitlines())
    total_t = len(secs)
    resumenes = {}
    try:
        js = (RAIZ / "matematicas/datos/temario.js").read_text(encoding="utf-8")
        for m in re.finditer(r'titulo:\s*"([^"]+)",\s*resumen:\s*"([^"]+)"', js):
            resumenes[m.group(1)] = m.group(2)
    except OSError:
        pass
    temas = []
    for src in secs:
        nodos = G.bloques(src)
        tit = next(n[1] for n in nodos if n[0] == "titulo")
        m = re.match(r"^(\d+)\.\s*(.*)$", tit)
        temas.append((int(m.group(1)), m.group(2), [n for n in nodos if n[0] != "titulo"]))
    with sync_playwright() as p:
        nav = p.chromium.launch()
        for num, titulo, nodos in temas:
            if solo and num not in solo:
                continue
            meta = METAS.get(str(num), {})
            cuerpo, destacadas, notas, subs = construir(nodos, num, titulo, meta)
            resumen = resumenes.get(titulo) or f"Apuntes del tema {num}"
            siguiente = temas[num][1] if num < total_t else None
            for _ in range(4):
                USADOS.clear()
                paginas = documento(num, titulo, resumen, total_t, siguiente, cuerpo, destacadas, notas, subs, 0, "")
                n_ej = len({s.kw['n'] for s in cuerpo if s.tipo == 'ejemplo'})
                html = a_html(paginas, num, titulo, resumen, total_t, siguiente, n_ej, len(destacadas))
                nombre = f"tema-{num:02d}-{G.NOMBRES[num]}"
                f = salida / f"{nombre}.html"
                f.write_text(html, encoding="utf-8")
                pg = nav.new_page(viewport={"width": 1280, "height": 720})
                pg.goto(f.as_uri()); pg.wait_for_timeout(300)
                over = pg.evaluate("window.__over")
                pg.close()
                if not over:
                    break
                nuevos = []
                # los índices de `over` son posiciones de diapositiva; solo se dividen las de cuerpo
                pos = {id(c): i for i, (c, _) in enumerate(paginas)}
                for s in cuerpo:
                    nuevos += dividir(s) if pos.get(id(s)) in over else [s]
                if len(nuevos) == len(cuerpo):
                    break
                cuerpo = nuevos
            pg = nav.new_page(viewport={"width": 1280, "height": 720})
            pg.goto(f.as_uri()); pg.wait_for_timeout(300)
            over = pg.evaluate("window.__over")
            pg.pdf(path=str(salida / f"{nombre}.pdf"), width="1280px", height="720px", print_background=True,
                   prefer_css_page_size=True, tagged=True, outline=True)
            print("OK", nombre, len(paginas), "diapositivas", "· desbordan:", over)
            pg.close()
        nav.close()


if __name__ == "__main__":
    main()
