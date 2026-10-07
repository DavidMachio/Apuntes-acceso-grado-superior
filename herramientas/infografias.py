"""Infografías de las diapositivas (SVG con variables del design system) y marca de agua de las portadas."""
from html import escape

BARRAS_T1 = [("IVA", "+21 %", 121, "sube"), ("Comisión", "−5 %", 95, "baja"), ("IRPF", "−15 %", 85, "baja")]


def _moneda(x, y, r=17):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="var(--color-accent3-500)" stroke="var(--marron-500)" stroke-width="2"/>'
            f'<text x="{x}" y="{y + 6}" text-anchor="middle" font-size="{r}" font-weight="700" fill="var(--marron-700)">€</text>')


def tema1():
    """100 € de partida y qué pasa con IVA, comisión e IRPF."""
    x0, esc = 150, 2.6
    filas = ""
    for i, (nombre, delta, valor, tipo) in enumerate(BARRAS_T1):
        y = 120 + i * 78
        color = "var(--color-primary-600)" if tipo == "sube" else "var(--marron-400)"
        filas += (f'<text x="0" y="{y + 30}" font-size="22" font-weight="700" fill="var(--marron-800)">{escape(nombre)}</text>'
                  f'<rect x="{x0}" y="{y}" width="{valor * esc:.0f}" height="46" rx="10" fill="{color}"/>'
                  f'<text x="{x0 + 16}" y="{y + 31}" font-size="22" font-weight="700" fill="#fff">{valor} €</text>'
                  f'<text x="{x0 + valor * esc + 12:.0f}" y="{y + 31}" font-size="22" font-weight="700" fill="var(--marron-700)">{escape(delta)}</text>')
    return (f'<svg viewBox="0 0 560 380" role="img" aria-label="Qué pasa con 100 euros según el impuesto o la comisión">'
            f'<text x="0" y="40" font-size="26" font-weight="700" fill="var(--marron-900)">Empiezas con 100 €</text>'
            + _moneda(300, 32) + _moneda(326, 32) + _moneda(352, 32) +
            f'<line x1="{x0 + 100 * esc:.0f}" y1="92" x2="{x0 + 100 * esc:.0f}" y2="350" stroke="var(--marron-500)" stroke-width="2" stroke-dasharray="6 6"/>'
            f'<text x="{x0 + 100 * esc:.0f}" y="82" text-anchor="middle" font-size="16" fill="var(--marron-600)">100 €</text>'
            + filas +
            '<text x="0" y="372" font-size="16" fill="var(--marron-600)">Multiplicar por 1,21 = sumar el 21 % de golpe</text></svg>')


def generica(simbolo="%"):
    return (f'<svg viewBox="0 0 560 380" role="img" aria-label="Ilustración"><circle cx="280" cy="190" r="150" fill="var(--color-primary-200)"/>'
            f'<text x="280" y="250" text-anchor="middle" font-size="190" font-weight="700" fill="var(--color-primary-800)">{escape(simbolo)}</text></svg>')


def infografia(num):
    return {1: tema1}.get(num, generica)()


def marca_agua(num):
    """Símbolos de cuentas grandes y claros para el fondo de las portadas."""
    s = "var(--color-primary-300)"
    return f'''<svg class="marca" viewBox="0 0 580 720" aria-hidden="true" fill="none" stroke="{s}" stroke-width="6" stroke-linecap="round">
<g>
<text x="230" y="360" font-size="400" font-weight="700" fill="{s}" stroke="none" opacity=".16">%</text>
<text x="10" y="690" font-size="210" font-weight="700" fill="{s}" stroke="none" opacity=".14">€</text>
<text x="400" y="680" font-size="160" font-weight="700" fill="{s}" stroke="none" opacity=".14">×</text>
<text x="140" y="262" font-size="120" font-weight="700" fill="{s}" stroke="none" opacity=".13">+</text>
<rect x="40" y="400" width="40" height="100" rx="6" opacity=".28"/><rect x="100" y="350" width="40" height="150" rx="6" opacity=".28"/><rect x="160" y="290" width="40" height="210" rx="6" opacity=".28"/>
<path d="M60 90 A70 70 0 1 1 130 160 L60 160 Z" opacity=".28"/>
<path d="M300 540 l40 -40 l40 24 l60 -70" opacity=".32"/>
</g></svg>'''


def waffle(parte=21, total=100, etiqueta="21 de cada 100"):
    """Cuadrícula 10×10: `parte` casillas coloreadas."""
    celdas = ""
    for i in range(total):
        f, c = divmod(i, 10)
        col = "var(--color-primary-500)" if i < parte else "var(--marron-200)"
        celdas += f'<rect x="{c * 34}" y="{f * 34}" width="30" height="30" rx="6" fill="{col}"/>'
    return (f'<svg viewBox="0 0 340 392" role="img" aria-label="{escape(etiqueta)}">{celdas}'
            f'<text x="170" y="378" text-anchor="middle" font-size="26" font-weight="700" fill="var(--marron-800)">{escape(etiqueta)}</text></svg>')


def cascada(pasos, titulo=""):
    """Barras en cascada: pasos = [(nombre, valor, 'total'|'resta')]. Valores en €."""
    maxv = max(v for _, v, t in pasos if t == "total")
    h, base, x = 230, 290, 20
    out, nivel = "", 0
    for nombre, v, tipo in pasos:
        alto = v / maxv * h
        if tipo == "total":
            nivel = v if nivel == 0 else nivel
            y, col = base - alto, "var(--color-primary-600)" if nombre != "Neto" else "var(--color-primary-800)"
            if nombre == "Neto":
                nivel = v
        else:
            y, col = base - nivel / maxv * h, "var(--marron-400)"
            nivel -= v
        out += (f'<rect x="{x}" y="{y:.0f}" width="96" height="{alto:.0f}" rx="8" fill="{col}"/>'
                f'<text x="{x + 48}" y="{y - 10:.0f}" text-anchor="middle" font-size="22" font-weight="700" fill="var(--marron-800)">'
                f'{"−" if tipo == "resta" else ""}{v:,} €</text>'.replace(",", "."))
        out += f'<text x="{x + 48}" y="{base + 30}" text-anchor="middle" font-size="19" fill="var(--marron-700)">{escape(nombre)}</text>'
        x += 116
    return (f'<svg viewBox="0 0 {x} 335" role="img" aria-label="{escape(titulo)}">'
            f'<line x1="0" y1="{base}" x2="{x}" y2="{base}" stroke="var(--marron-300)" stroke-width="3"/>{out}</svg>')


VISUALES = {
    (1, "IVA"): lambda: waffle(21, 100, "21 de cada 100"),
    (1, "IRPF"): lambda: cascada([("Bruto", 3000, "total"), ("Retención", 450, "resta"), ("Cotización", 300, "resta"), ("Neto", 2250, "total")],
                                 "De 3.000 € brutos a 2.250 € netos"),
}


def visual(num, sub):
    for (n, pref), f in VISUALES.items():
        if n == num and sub and sub.startswith(pref):
            return f()
    return None


# ---------------------------------------------------------------- infografías por tema (2-10)
def _t(x, y, s, size=20, w=600, fill="var(--marron-800)", anchor="start"):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{w}" fill="{fill}" text-anchor="{anchor}">{escape(s)}</text>'


def _svg(cuerpo, etiqueta):
    return f'<svg viewBox="0 0 560 380" role="img" aria-label="{escape(etiqueta)}">{cuerpo}</svg>'


def _barras_v(datos, x0=40, base=300, alto=210, ancho=90, sep=40, vmax=None, colores=None, fmt=None):
    vmax = vmax or max(v for _, v in datos)
    out = ""
    for i, (nombre, v) in enumerate(datos):
        x = x0 + i * (ancho + sep)
        h = v / vmax * alto
        col = (colores or ["var(--color-primary-500)"] * len(datos))[i]
        out += (f'<rect x="{x}" y="{base - h:.0f}" width="{ancho}" height="{h:.0f}" rx="10" fill="{col}"/>'
                + _t(x + ancho / 2, base - h - 10, fmt(v) if fmt else str(v), 21, 700, anchor="middle")
                + _t(x + ancho / 2, base + 28, nombre, 18, 500, "var(--marron-700)", "middle"))
    return out + f'<line x1="{x0 - 15}" y1="{base}" x2="540" y2="{base}" stroke="var(--marron-300)" stroke-width="3"/>'


def tema2():
    c = ["var(--color-primary-500)", "var(--color-primary-700)", "var(--marron-400)"]
    return _svg(_t(0, 36, "Sube un 40 % y baja un 40 %", 26, 700, "var(--marron-900)")
                + _barras_v([("Inicio", 200), ("Sube 40 %", 280), ("Baja 40 %", 168)], 60, 320, 230, 110, 50, 300, c, lambda v: f"{v} €")
                + _t(280, 372, "No vuelves a los 200 €", 17, 500, "var(--marron-600)", "middle"), "Subir y bajar un 40 % no devuelve al inicio")


def tema3():
    celdas = ""
    for i in range(20):
        col = "var(--color-primary-500)" if i < 5 else "var(--marron-200)"
        celdas += f'<rect x="{10 + i * 26}" y="150" width="22" height="80" rx="6" fill="{col}"/>'
    return _svg(_t(0, 40, "5 de 20 alumnos son zurdos", 26, 700, "var(--marron-900)") + celdas
                + _t(10, 275, "5 / 20 × 100 = 25 %", 34, 700, "var(--color-primary-800)")
                + _t(10, 320, "Parte entre total, por 100", 19, 500, "var(--marron-600)"), "5 de 20 es el 25 %")


def tema4():
    c = ["var(--color-primary-500)", "var(--marron-400)"]
    return _svg(_t(0, 36, "Del inicio de mes a mitad de mes", 26, 700, "var(--marron-900)")
                + _barras_v([("Inicio", 7000), ("Mitad de mes", 6200)], 60, 310, 220, 130, 70, 7000, c, lambda v: f"{v:,} €".replace(",", "."))
                + _t(420, 150, "−800 €", 30, 700, "var(--marron-700)", "middle") + _t(420, 182, "−11,43 %", 24, 600, "var(--marron-600)", "middle"), "Variación absoluta y porcentual")


def tema5():
    pts = [(60 + i * 110, 300 - (v - 1000) / 240 * 190) for i, v in enumerate([1000, 1060, 1120, 1180, 1240])]
    linea = "M" + " L".join(f"{x},{y:.0f}" for x, y in pts)
    puntos = "".join(f'<circle cx="{x}" cy="{y:.0f}" r="9" fill="var(--color-primary-600)"/>' + _t(x, y - 18, f"{1000 + i * 60} €", 18, 700, anchor="middle")
                     + _t(x, 335, f"{i} años" if i != 1 else "1 año", 16, 500, "var(--marron-600)", "middle") for i, (x, y) in enumerate(pts))
    return _svg(_t(0, 36, "1.000 € al 6 % simple: +60 € cada año", 24, 700, "var(--marron-900)")
                + f'<path d="{linea}" fill="none" stroke="var(--color-primary-500)" stroke-width="6" stroke-linecap="round"/>' + puntos
                + _t(280, 372, "Sube siempre lo mismo: línea recta", 17, 500, "var(--marron-600)", "middle"), "Interés simple: crecimiento lineal")


def tema6():
    comp = [1000, 1050, 1102.5, 1157.63]
    simp = [1000, 1050, 1100, 1150]
    xs = [70 + i * 140 for i in range(4)]
    y = lambda v: 310 - (v - 1000) / 170 * 200
    barras = "".join(f'<rect x="{x - 36}" y="{y(v):.0f}" width="72" height="{310 - y(v):.0f}" rx="9" fill="var(--color-primary-500)"/>'
                     + _t(x, y(v) - 10, f"{v:,.2f}".replace(",", " ").replace(".", ",") if i == 3 else f"{v:,.0f}".replace(",", "."), 17, 700, anchor="middle")
                     + _t(x, 338, f"{i} años" if i != 1 else "1 año", 16, 500, "var(--marron-600)", "middle") for i, (x, v) in enumerate(zip(xs, comp)))
    rec = "M" + " L".join(f"{x},{y(v):.0f}" for x, v in zip(xs, simp))
    return _svg(_t(0, 36, "1.000 € al 5 %: compuesto frente a simple", 24, 700, "var(--marron-900)") + barras
                + f'<path d="{rec}" fill="none" stroke="var(--marron-500)" stroke-width="4" stroke-dasharray="8 8"/>'
                + _t(280, 372, "Línea discontinua: interés simple", 17, 500, "var(--marron-600)", "middle"), "Interés compuesto frente a interés simple")


def tema7():
    import math
    ejes = ('<line x1="40" y1="320" x2="540" y2="320" stroke="var(--marron-400)" stroke-width="3"/>'
            '<line x1="40" y1="320" x2="40" y2="50" stroke="var(--marron-400)" stroke-width="3"/>')
    directa = 'M40 320 L260 110'
    inv = "M" + " L".join(f"{300 + i * 12},{320 - 190 * (1 / (0.5 + i * 0.22)) / 2:.0f}" for i in range(0, 19))
    inv = "M" + " L".join(f"{290 + (x * 14)},{320 - 240 / (1 + x * 0.55):.0f}" for x in range(0, 18))
    return _svg(ejes + f'<path d="{directa}" fill="none" stroke="var(--color-primary-600)" stroke-width="7" stroke-linecap="round"/>'
                + f'<path d="{inv}" fill="none" stroke="var(--marron-500)" stroke-width="7" stroke-linecap="round"/>'
                + _t(60, 90, "Directa: sube una, sube la otra", 18, 700, "var(--color-primary-800)")
                + _t(300, 120, "Inversa: sube una, baja la otra", 18, 700, "var(--marron-700)")
                + _t(290, 364, "k = y / x", 20, 700, "var(--color-primary-800)", "end") + _t(300, 364, "k = x · y", 20, 700, "var(--marron-700)"), "Proporcionalidad directa e inversa")


def tema8():
    return _svg(_t(0, 36, "Una ecuación es una balanza", 26, 700, "var(--marron-900)")
                + '<line x1="80" y1="130" x2="480" y2="130" stroke="var(--marron-600)" stroke-width="8" stroke-linecap="round"/>'
                + '<polygon points="280,130 250,320 310,320" fill="var(--marron-300)"/>'
                + '<rect x="70" y="140" width="190" height="64" rx="12" fill="var(--color-primary-200)" stroke="var(--color-primary-600)" stroke-width="3"/>'
                + '<rect x="300" y="140" width="190" height="64" rx="12" fill="var(--color-primary-200)" stroke="var(--color-primary-600)" stroke-width="3"/>'
                + _t(165, 183, "3x + 1", 30, 700, "var(--marron-900)", "middle") + _t(395, 183, "4", 30, 700, "var(--marron-900)", "middle")
                + _t(280, 262, "Quita 1 a cada lado", 20, 600, "var(--marron-700)", "middle")
                + _t(280, 296, "3x = 3  →  x = 1", 26, 700, "var(--color-primary-800)", "middle"), "Despejar es mantener la balanza equilibrada")


def tema9():
    datos = [("Fútbol", 12, "0,30"), ("Baloncesto", 10, "0,25"), ("Natación", 8, "0,20"), ("Tenis", 6, "0,15"), ("Ciclismo", 4, "0,10")]
    out = _t(0, 36, "Deporte favorito de 40 personas", 26, 700, "var(--marron-900)")
    out += _t(330, 76, "FA", 16, 700, "var(--marron-600)", "middle") + _t(420, 76, "FR", 16, 700, "var(--marron-600)", "middle") + _t(500, 76, "%", 16, 700, "var(--marron-600)", "middle")
    for i, (n, v, fr) in enumerate(datos):
        y = 92 + i * 54
        out += (_t(0, y + 28, n, 19, 600) + f'<rect x="120" y="{y}" width="{v * 14}" height="38" rx="9" fill="var(--color-primary-500)"/>'
                + _t(330, y + 27, str(v), 19, 700, anchor="middle") + _t(420, y + 27, fr, 19, 600, anchor="middle") + _t(500, y + 27, f"{int(float(fr.replace(',', '.')) * 100)} %", 19, 600, anchor="middle"))
    return _svg(out + _t(0, 372, "FR = FA / total   ·   % = FR × 100", 18, 600, "var(--marron-600)"), "Frecuencias absolutas, relativas y porcentajes")


def tema10():
    import math
    barras = "".join(f'<rect x="{30 + i * 34}" y="{250 - h}" width="26" height="{h}" rx="5" fill="var(--color-primary-500)"/>' for i, h in enumerate([90, 150, 60, 120]))
    cx, cy, r = 280, 200, 78
    ang = 0
    sect = ""
    for frac, col in [(.5, "var(--color-primary-500)"), (.3, "var(--color-primary-700)"), (.2, "var(--marron-400)")]:
        a0, a1 = ang * 2 * math.pi - math.pi / 2, (ang + frac) * 2 * math.pi - math.pi / 2
        x0, y0, x1, y1 = cx + r * math.cos(a0), cy + r * math.sin(a0), cx + r * math.cos(a1), cy + r * math.sin(a1)
        sect += f'<path d="M{cx},{cy} L{x0:.1f},{y0:.1f} A{r},{r} 0 {1 if frac > .5 else 0} 1 {x1:.1f},{y1:.1f} Z" fill="{col}" stroke="#fff" stroke-width="3"/>'
        ang += frac
    lin = "M400,250 L440,200 L480,225 L520,140"
    return _svg(_t(0, 36, "Tres gráficas, tres usos", 26, 700, "var(--marron-900)") + barras
                + '<line x1="20" y1="250" x2="170" y2="250" stroke="var(--marron-300)" stroke-width="3"/>' + sect
                + f'<path d="{lin}" fill="none" stroke="var(--color-primary-600)" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>'
                + '<line x1="390" y1="250" x2="540" y2="250" stroke="var(--marron-300)" stroke-width="3"/>'
                + _t(100, 290, "Barras", 22, 700, anchor="middle") + _t(100, 318, "comparar", 17, 500, "var(--marron-600)", "middle")
                + _t(280, 316, "Sectores", 22, 700, anchor="middle") + _t(280, 344, "partes de un total", 17, 500, "var(--marron-600)", "middle")
                + _t(465, 290, "Líneas", 22, 700, anchor="middle") + _t(465, 318, "evolución", 17, 500, "var(--marron-600)", "middle"), "Barras, sectores y líneas")


def infografia(num):  # noqa: F811  (sustituye a la versión inicial)
    return {1: tema1, 2: tema2, 3: tema3, 4: tema4, 5: tema5, 6: tema6, 7: tema7, 8: tema8, 9: tema9, 10: tema10}.get(num, generica)()


# ---------------------------------------------------------------- visuales de diapositivas de concepto
import math as _m

_P6, _P3, _P8 = "var(--color-primary-600)", "var(--color-primary-300)", "var(--color-primary-800)"
_M4, _M2, _M7 = "var(--marron-400)", "var(--marron-200)", "var(--marron-700)"


def _flecha(x1, y, x2, col=_M7):
    return (f'<line x1="{x1}" y1="{y}" x2="{x2 - 8}" y2="{y}" stroke="{col}" stroke-width="4" stroke-linecap="round"/>'
            f'<polygon points="{x2},{y} {x2 - 14},{y - 8} {x2 - 14},{y + 8}" fill="{col}"/>')


def _caja(x, y, w, h, txt, col=_P6, tc="#fff", size=24):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{col}"/>'
            + _t(x + w / 2, y + h / 2 + size / 3, txt, size, 700, tc, "middle"))


def v_tasas():
    papelera = (f'<rect x="60" y="120" width="90" height="110" rx="10" fill="{_M4}"/>'
                f'<rect x="50" y="100" width="110" height="16" rx="6" fill="{_M7}"/><rect x="90" y="86" width="30" height="14" rx="5" fill="{_M7}"/>'
                + "".join(f'<rect x="{x}" y="132" width="8" height="86" rx="4" fill="{_M2}"/>' for x in (80, 101, 122)))
    casa = (f'<polygon points="380,150 450,90 520,150" fill="{_P8}"/><rect x="395" y="150" width="110" height="80" fill="{_P6}"/>'
            f'<rect x="436" y="180" width="28" height="50" rx="4" fill="#fff"/>')
    return _svg(papelera + casa
                + _t(105, 275, "Basura", 24, 700, anchor="middle") + _t(105, 305, "tasa fija", 22, 500, _M7, "middle")
                + _t(105, 335, "siempre igual", 19, 500, _M7, "middle")
                + _t(450, 275, "IBI", 24, 700, anchor="middle") + _t(450, 305, "porcentaje", 22, 500, _M7, "middle")
                + _t(450, 335, "según el valor", 19, 500, _M7, "middle")
                + f'<line x1="280" y1="90" x2="280" y2="340" stroke="{_M2}" stroke-width="3" stroke-dasharray="8 8"/>', "Tasa fija frente a porcentaje")


def v_t1_empezar():
    return _svg(_t(40, 70, "Precio", 22, 600, _M7) + f'<rect x="40" y="90" width="480" height="64" rx="12" fill="{_M2}"/>'
                + _t(280, 132, "300 €", 28, 700, anchor="middle")
                + _t(40, 215, "Pagas el 80 %", 22, 600, _M7) + f'<rect x="40" y="235" width="384" height="64" rx="12" fill="{_P6}"/>'
                + f'<rect x="424" y="235" width="96" height="64" rx="12" fill="none" stroke="{_M4}" stroke-width="3" stroke-dasharray="7 6"/>'
                + _t(232, 277, "240 €", 28, 700, "#fff", "middle") + _t(472, 277, "−20 %", 22, 700, _M7, "middle"),
                "300 € con un 20 % de descuento son 240 €")


def v_t2_empezar():
    f1 = (_caja(20, 60, 130, 70, "Ci", _M4) + _flecha(160, 95, 280) + _t(220, 78, "× (1 + p)", 21, 700, _P8, "middle")
          + _caja(290, 60, 130, 70, "Cf", _P6) + _t(470, 106, "sube", 24, 700, _P6, "middle"))
    f2 = (_caja(20, 240, 130, 70, "Ci", _M4) + _flecha(160, 275, 280) + _t(220, 258, "× (1 − p)", 21, 700, _M7, "middle")
          + _caja(290, 240, 130, 70, "Cf", _M7) + _t(470, 286, "baja", 24, 700, _M7, "middle"))
    return _svg(f1 + f2 + f'<line x1="20" y1="185" x2="540" y2="185" stroke="{_M2}" stroke-width="3"/>', "Aumento y disminución porcentual")


def v_t3_empezar():
    return _svg(_t(40, 60, "Total (t) = 100 %", 22, 700, _M7) + f'<rect x="40" y="80" width="480" height="70" rx="14" fill="{_M2}"/>'
                + f'<rect x="40" y="80" width="190" height="70" rx="14" fill="{_P6}"/>'
                + _t(135, 125, "c", 30, 700, "#fff", "middle") + _t(380, 125, "resto", 22, 600, _M7, "middle")
                + _t(280, 230, "p = c / t × 100", 34, 700, _P8, "middle")
                + _t(280, 285, "¿qué parte del total es c?", 22, 500, _M7, "middle")
                + f'<path d="M135 158 L135 190 M135 190 L280 190" stroke="{_P6}" stroke-width="0"/>', "Parte frente al total")


def v_t4_empezar():
    return _svg(_barras_v([("Ci", 120), ("Cf", 190)], x0=70, ancho=110, sep=90, vmax=190, alto=200,
                          colores=[_M4, _P6], fmt=lambda v: "")
                + f'<rect x="340" y="{300 - 200:.0f}" width="110" height="{70 / 190 * 200:.0f}" rx="10" fill="none" stroke="{_P8}" stroke-width="3" stroke-dasharray="7 6"/>'
                + f'<rect x="340" y="100" width="110" height="74" rx="10" fill="{_P3}"/>'
                + _t(395, 146, "VA", 28, 700, _P8, "middle") + _t(330, 80, "variación = Cf − Ci", 20, 600, _M7, "middle")
                + _t(125, 285, "", 10), "Variación entre la cantidad inicial y la final")


def v_t5_empezar():
    out = ""
    for i in range(4):
        x = 30 + i * 125
        out += (f'<rect x="{x}" y="170" width="100" height="130" rx="8" fill="{_M4}"/>'
                f'<rect x="{x}" y="{170 - 38 * (i + 1) if i else 132}" width="100" height="{38 * (i + 1) if i else 38}" rx="8" fill="{_P6}"/>'
                + _t(x + 50, 322, f"Año {i + 1}", 18, 500, _M7, "middle"))
    out = ""
    for i in range(4):
        x = 30 + i * 125
        out += f'<rect x="{x}" y="210" width="100" height="90" rx="8" fill="{_M4}"/>'
        for k in range(i + 1):
            out += f'<rect x="{x}" y="{210 - (k + 1) * 34}" width="100" height="30" rx="6" fill="{_P6}"/>'
        out += _t(x + 50, 326, f"Año {i + 1}", 18, 500, _M7, "middle")
    return _svg(out + _t(280, 36, "Cada año se suma el mismo interés", 22, 700, _P8, "middle")
                + _t(80, 262, "capital", 18, 700, "#fff", "middle") + _t(60, 175, "", 10), "Interés simple: crece igual cada año")


def v_t5_unidades():
    cx, cy, r = 150, 190, 100
    sector = f'<path d="M{cx} {cy} L{cx} {cy - r} A{r} {r} 0 0 1 {cx} {cy + r} Z" fill="{_P6}"/>'
    marcas = "".join(f'<line x1="{cx + (r - 8) * _m.sin(_m.radians(a)):.1f}" y1="{cy - (r - 8) * _m.cos(_m.radians(a)):.1f}" '
                     f'x2="{cx + r * _m.sin(_m.radians(a)):.1f}" y2="{cy - r * _m.cos(_m.radians(a)):.1f}" stroke="{_M7}" stroke-width="3"/>'
                     for a in range(0, 360, 30))
    return _svg(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{_M2}" stroke="{_M7}" stroke-width="4"/>{sector}{marcas}'
                + _t(cx, 330, "6 de 12 meses", 22, 700, _M7, "middle")
                + _t(400, 160, "6 meses", 26, 600, _M7, "middle") + _t(400, 205, "= 6 / 12", 28, 700, _M7, "middle")
                + _t(400, 260, "= 0,5 años", 32, 700, _P8, "middle"), "Seis meses son medio año")


def v_t6_empezar():
    ci, out = 100, ""
    for i in range(5):
        x = 30 + i * 100
        cf = 100 * 1.25 ** i
        h = cf * 1.0
        ih = 25 * 1.25 ** (i - 1) if i else 0
        out += f'<rect x="{x}" y="{300 - 100:.0f}" width="80" height="100" rx="8" fill="{_M4}"/>'
        if i:
            out += f'<rect x="{x}" y="{300 - h:.0f}" width="80" height="{h - 100:.0f}" rx="8" fill="{_P6}"/>'
        out += _t(x + 40, 326, f"Año {i}", 20, 500, _M7, "middle")
    return _svg(out + _t(280, 40, "El interés también genera interés", 22, 700, _P8, "middle")
                + _t(70, 292, "Ci", 24, 700, "#fff", "middle"), "Interés compuesto: crece cada vez más")


def v_t7_numerica():
    return _svg(_t(140, 120, "3", 54, 700, _P8, "middle") + f'<line x1="100" y1="140" x2="180" y2="140" stroke="{_M7}" stroke-width="5"/>'
                + _t(140, 205, "5", 54, 700, _P8, "middle") + _t(280, 175, "=", 56, 700, _M7, "middle")
                + _t(420, 120, "6", 54, 700, _P8, "middle") + f'<line x1="380" y1="140" x2="460" y2="140" stroke="{_M7}" stroke-width="5"/>'
                + _t(420, 205, "10", 54, 700, _P8, "middle")
                + f'<path d="M175 100 L385 195" stroke="{_P6}" stroke-width="4" stroke-linecap="round" fill="none"/>'
                + f'<path d="M175 195 L385 100" stroke="{_P6}" stroke-width="4" stroke-linecap="round" fill="none"/>'
                + _t(280, 290, "3 · 10 = 5 · 6", 32, 700, _P8, "middle") + _t(280, 328, "productos cruzados iguales", 20, 500, _M7, "middle"),
                "Productos cruzados")


def _ejes(extra, etx="", ety=""):
    return (f'<line x1="60" y1="320" x2="530" y2="320" stroke="{_M7}" stroke-width="4"/><line x1="60" y1="320" x2="60" y2="40" stroke="{_M7}" stroke-width="4"/>'
            + extra + _t(530, 350, etx, 18, 600, _M7, "end") + _t(70, 40, ety, 18, 600, _M7))


def v_t7_directa():
    pts = [(1, 300), (2, 600), (3, 900), (4, 1200)]
    px = [(60 + x * 100, 320 - y / 1200 * 260) for x, y in pts]
    s = f'<polyline points="60,320 {" ".join(f"{a},{b:.0f}" for a, b in px)}" fill="none" stroke="{_P6}" stroke-width="5" stroke-linecap="round"/>'
    s += "".join(f'<circle cx="{a}" cy="{b:.0f}" r="9" fill="{_P8}"/>' for a, b in px)
    return _svg(_ejes(s, "kg", "€") + _t(90, 80, "si uno se duplica,", 22, 600, _M7) + _t(90, 108, "el otro también", 22, 600, _M7), "Proporcionalidad directa: recta")


def v_t7_inversa():
    pts = [(1, 12), (2, 6), (3, 4), (4, 3), (6, 2), (12, 1)]
    px = [(60 + x * 38, 320 - y / 12 * 250) for x, y in pts]
    curva = " ".join(f"{60 + x * 38:.0f},{320 - (12 / x) / 12 * 250:.0f}" for x in [i / 4 for i in range(4, 49)])
    s = f'<polyline points="{curva}" fill="none" stroke="{_P6}" stroke-width="5" stroke-linecap="round"/>'
    s += "".join(f'<circle cx="{a:.0f}" cy="{b:.0f}" r="9" fill="{_P8}"/>' for a, b in px[:4])
    return _svg(_ejes(s, "obreros", "días") + _t(250, 150, "si uno se duplica,", 22, 600, _M7) + _t(250, 178, "el otro se reduce a la mitad", 22, 600, _M7), "Proporcionalidad inversa: curva")


def v_t9_empezar():
    celdas = ""
    for r in range(4):
        for c in range(4):
            col = _P6 if r == 0 else (_M2 if c else _P3)
            celdas += f'<rect x="{140 + c * 100}" y="{70 + r * 52}" width="96" height="48" rx="8" fill="{col}"/>'
    celdas += f'<rect x="{140 + 100}" y="{70 + 52}" width="96" height="48" rx="8" fill="{_M4}" stroke="{_P8}" stroke-width="4"/>'
    return _svg(celdas + _t(290, 40, "Título de la tabla", 22, 700, _P8, "middle")
                + _t(190, 62, "", 10) + _t(20, 190, "filas", 20, 700, _M7) + _t(300, 300, "columnas", 20, 700, _M7, "middle")
                + _t(440, 340, "celda", 20, 700, _P8, "middle") + _t(330, 340, "", 10)
                + _t(190, 330, "encabezado", 20, 700, _P8, "middle")
                + f'<path d="M345 232 L420 322" stroke="{_P8}" stroke-width="2" fill="none"/>'
                + f'<path d="M190 105 L190 310" stroke="{_P8}" stroke-width="0" fill="none"/>', "Partes de una tabla")


def v_t10_sectores():
    datos = [(40, _P6), (25, _P3), (20, _M4), (15, _M7)]
    cx, cy, r, a0, out = 170, 190, 135, 0, ""
    for v, col in datos:
        a1 = a0 + v * 3.6
        x0, y0 = cx + r * _m.sin(_m.radians(a0)), cy - r * _m.cos(_m.radians(a0))
        x1, y1 = cx + r * _m.sin(_m.radians(a1)), cy - r * _m.cos(_m.radians(a1))
        out += f'<path d="M{cx} {cy} L{x0:.1f} {y0:.1f} A{r} {r} 0 {1 if v > 50 else 0} 1 {x1:.1f} {y1:.1f} Z" fill="{col}" stroke="#fff" stroke-width="4"/>'
        am = _m.radians((a0 + a1) / 2)
        out += _t(cx + 0.62 * r * _m.sin(am), cy - 0.62 * r * _m.cos(am) + 8, f"{v} %", 22, 700, "#fff" if col != _P3 else _P8, "middle")
        a0 = a1
    return _svg(out + _t(430, 160, "Las partes", 26, 700, _M7, "middle") + _t(430, 200, "suman", 26, 700, _M7, "middle")
                + _t(430, 258, "100 %", 44, 700, _P8, "middle"), "Gráfica de sectores")


def v_t10_lineas():
    ys = [250, 215, 225, 150, 120, 70]
    xs = [70 + i * 88 for i in range(6)]
    s = "".join(f'<line x1="60" y1="{y}" x2="530" y2="{y}" stroke="{_M2}" stroke-width="2"/>' for y in (80, 140, 200, 260))
    s += f'<polyline points="{" ".join(f"{x},{y}" for x, y in zip(xs, ys))}" fill="none" stroke="{_P6}" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"/>'
    s += "".join(f'<circle cx="{x}" cy="{y}" r="9" fill="{_P8}"/>' for x, y in zip(xs, ys))
    s += "".join(_t(x, 345, m, 18, 500, _M7, "middle") for x, m in zip(xs, ["Ene", "Feb", "Mar", "Abr", "May", "Jun"]))
    return _svg(s + _t(60, 40, "Evolución en el tiempo", 22, 700, _P8) + f'<line x1="60" y1="300" x2="530" y2="300" stroke="{_M7}" stroke-width="4"/>', "Gráfica de líneas")


VISUALES.update({
    (1, "Tasas"): v_tasas, (1, "Para empezar"): v_t1_empezar, (2, "Para empezar"): v_t2_empezar,
    (3, "Para empezar"): v_t3_empezar, (4, "Para empezar"): v_t4_empezar, (5, "Para empezar"): v_t5_empezar,
    (5, "¡Ojo"): v_t5_unidades, (6, "Para empezar"): v_t6_empezar, (7, "Proporcionalidad numérica"): v_t7_numerica,
    (7, "Proporcionalidad directa"): v_t7_directa, (7, "Proporcionalidad inversa"): v_t7_inversa,
    (9, "Para empezar"): v_t9_empezar, (10, "Gráfica de sectores"): v_t10_sectores, (10, "Gráfica de líneas"): v_t10_lineas,
})
