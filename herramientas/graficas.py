"""Gráficas SVG sencillas con los colores del design system (variables CSS)."""
import math
from html import escape

FONT = "font-family:var(--font-family-body)"
W, H = 520, 250


def fmt(n, dec=None):
    if dec is None:
        dec = 0 if abs(n - round(n)) < 1e-9 else (2 if abs(n * 10 - round(n * 10)) > 1e-9 else 1)
    s = f"{n:,.{dec}f}"
    return s.replace(",", "_").replace(".", ",").replace("_", ".")


def pct(n):
    return fmt(n) + " %"


def ticks(lo, hi, n=5):
    span = hi - lo or 1
    raw = span / (n - 1)
    mag = 10 ** math.floor(math.log10(raw))
    step = min((s * mag for s in (1, 2, 2.5, 5, 10) if s * mag >= raw), default=raw)
    a = math.floor(lo / step + 1e-9) * step
    b = math.ceil(hi / step - 1e-9) * step
    out, v = [], a
    while v <= b + 1e-9:
        out.append(round(v, 6))
        v += step
    return out


def wrap(inner, label, w=W, h=H):
    return (f'<svg class="grafica" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(label)}" '
            f'xmlns="http://www.w3.org/2000/svg" style="{FONT}">{inner}</svg>')


def axes(ys, y0, y1, ml, mr, mt, mb, ylabel, w=W, h=H):
    out = []
    ph = h - mt - mb

    def Y(v):
        return mt + ph * (1 - (v - y0) / (y1 - y0))
    for t in ys:
        out.append(f'<line x1="{ml}" x2="{w-mr}" y1="{Y(t):.1f}" y2="{Y(t):.1f}" stroke="var(--color-border-default)" stroke-width="1"/>')
        out.append(f'<text x="{ml-8}" y="{Y(t)+4:.1f}" text-anchor="end" font-size="12" fill="var(--color-text-secondary)">{fmt(t)}</text>')
    out.append(f'<line x1="{ml}" x2="{w-mr}" y1="{h-mb}" y2="{h-mb}" stroke="var(--color-border-strong)" stroke-width="1.5"/>')
    if ylabel:
        out.append(f'<text transform="translate(14 {mt+ph/2:.0f}) rotate(-90)" text-anchor="middle" font-size="12" fill="var(--color-text-secondary)">{escape(ylabel)}</text>')
    return "".join(out), Y


def barras(cats, vals, ylabel, alt):
    ml, mr, mt, mb = 56, 14, 22, 36
    ys = ticks(0, max(vals))
    inner, Y = axes(ys, 0, ys[-1], ml, mr, mt, mb, ylabel)
    band = (W - ml - mr) / len(cats)
    bw = min(band * 0.58, 90)
    parts = [inner]
    for i, (c, v) in enumerate(zip(cats, vals)):
        x = ml + band * i + (band - bw) / 2
        y = Y(v)
        parts.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bw:.1f}" height="{H-mb-y:.1f}" rx="3" fill="var(--data-cat-1)"/>')
        parts.append(f'<text x="{x+bw/2:.1f}" y="{y-6:.1f}" text-anchor="middle" font-size="13" font-weight="600" fill="var(--color-text-primary)">{fmt(v)}</text>')
        parts.append(f'<text x="{x+bw/2:.1f}" y="{H-mb+20}" text-anchor="middle" font-size="12.5" fill="var(--color-text-primary)">{escape(c)}</text>')
    return wrap("".join(parts), alt)


def lineas(xs, vals, ylabel, alt, cero=False, dec=None):
    ml, mr, mt, mb = 62, 22, 30, 36
    lo, hi = (0 if cero else min(vals)), max(vals)
    pad = (hi - lo) * 0.1 or 1
    ys = ticks(lo if cero else lo - pad, hi + pad)
    inner, Y = axes(ys, ys[0], ys[-1], ml, mr, mt, mb, ylabel)
    n = len(xs)
    step = (W - ml - mr) / n
    px = [ml + step * (i + 0.5) for i in range(n)]
    pts = " ".join(f"{px[i]:.1f},{Y(vals[i]):.1f}" for i in range(n))
    parts = [inner, f'<polyline points="{pts}" fill="none" stroke="var(--data-cat-1)" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/>']
    for i in range(n):
        nb = [vals[j] for j in (i - 1, i + 1) if 0 <= j < n]
        abajo = all(vals[i] < v for v in nb)
        ty = Y(vals[i]) + (20 if abajo else -10)
        parts.append(f'<circle cx="{px[i]:.1f}" cy="{Y(vals[i]):.1f}" r="4.5" fill="var(--data-cat-1)" stroke="var(--color-bg-page)" stroke-width="2"/>')
        parts.append(f'<text x="{px[i]:.1f}" y="{ty:.1f}" text-anchor="middle" font-size="13" font-weight="600" fill="var(--color-text-primary)">{fmt(vals[i], dec)}</text>')
        parts.append(f'<text x="{px[i]:.1f}" y="{H-mb+20}" text-anchor="middle" font-size="12.5" fill="var(--color-text-primary)">{escape(str(xs[i]))}</text>')
    return wrap("".join(parts), alt)


def sectores(etiquetas, valores, alt):
    total = sum(valores)
    cx, cy, r = 130, 125, 105
    parts, ang = [], -math.pi / 2
    for i, v in enumerate(valores):
        a2 = ang + 2 * math.pi * v / total
        k = i % 6 + 1
        x1, y1 = cx + r * math.cos(ang), cy + r * math.sin(ang)
        x2, y2 = cx + r * math.cos(a2), cy + r * math.sin(a2)
        large = 1 if a2 - ang > math.pi else 0
        parts.append(f'<path d="M{cx},{cy} L{x1:.1f},{y1:.1f} A{r},{r} 0 {large} 1 {x2:.1f},{y2:.1f} Z" fill="var(--data-cat-{k})" stroke="var(--color-bg-page)" stroke-width="3"/>')
        p = 100 * v / total
        if p >= 8:
            m = (ang + a2) / 2
            parts.append(f'<text x="{cx+r*0.64*math.cos(m):.1f}" y="{cy+r*0.64*math.sin(m)+5:.1f}" text-anchor="middle" font-size="14" font-weight="600" fill="var(--data-cat-{k}-ink)">{pct(round(p,2))}</text>')
        ang = a2
    ly = cy - 14 * len(valores) / 2 * 1.4 + 8
    for i, (e, v) in enumerate(zip(etiquetas, valores)):
        k = i % 6 + 1
        y = ly + i * 28
        parts.append(f'<rect x="270" y="{y-11:.1f}" width="14" height="14" rx="3" fill="var(--data-cat-{k})"/>')
        parts.append(f'<text x="292" y="{y:.1f}" font-size="13.5" fill="var(--color-text-primary)">{escape(e)} · {pct(round(100*v/total,2))}</text>')
    return wrap("".join(parts), alt)


def _panel(ox, titulo, pts, curva, xmax, ymax, xl, yl, xt, yt):
    pw, ph, t, b = 190, 150, 34, 0
    oy = 40
    X = lambda v: ox + pw * v / xmax
    Yv = lambda v: oy + ph * (1 - v / ymax)
    o = [f'<text x="{ox}" y="18" font-size="13.5" font-weight="600" fill="var(--color-text-primary)">{escape(titulo)}</text>']
    for t_ in yt:
        o.append(f'<line x1="{ox}" x2="{ox+pw}" y1="{Yv(t_):.1f}" y2="{Yv(t_):.1f}" stroke="var(--color-border-default)"/>')
        o.append(f'<text x="{ox-6}" y="{Yv(t_)+4:.1f}" text-anchor="end" font-size="11" fill="var(--color-text-secondary)">{fmt(t_)}</text>')
    for t_ in xt:
        o.append(f'<text x="{X(t_):.1f}" y="{oy+ph+16}" text-anchor="middle" font-size="11" fill="var(--color-text-secondary)">{fmt(t_)}</text>')
    o.append(f'<line x1="{ox}" x2="{ox+pw}" y1="{oy+ph}" y2="{oy+ph}" stroke="var(--color-border-strong)" stroke-width="1.5"/>')
    o.append(f'<line x1="{ox}" x2="{ox}" y1="{oy}" y2="{oy+ph}" stroke="var(--color-border-strong)" stroke-width="1.5"/>')
    o.append(f'<text x="{ox+pw/2}" y="{oy+ph+34}" text-anchor="middle" font-size="12" fill="var(--color-text-secondary)">{escape(xl)}</text>')
    o.append(f'<text x="{ox}" y="{oy-6}" font-size="12" fill="var(--color-text-secondary)">{escape(yl)}</text>')
    o.append('<polyline points="%s" fill="none" stroke="var(--data-cat-1)" stroke-width="2.5" stroke-linecap="round"/>' % " ".join(f"{X(x):.1f},{Yv(y):.1f}" for x, y in curva))
    for x, y in pts:
        o.append(f'<circle cx="{X(x):.1f}" cy="{Yv(y):.1f}" r="4" fill="var(--data-cat-1)" stroke="var(--color-bg-page)" stroke-width="2"/>')
    return "".join(o)


def proporcionalidad():
    d = _panel(52, "Directa: k = y / x", [(1, 300), (2, 600), (3, 900), (4, 1200), (10, 3000)],
               [(0, 0), (10, 3000)], 10, 3000, "Libros a imprimir", "Folios", [0, 2, 4, 6, 8, 10], [0, 1000, 2000, 3000])
    i = _panel(298, "Inversa: k = x · y", [(x, 60 / x) for x in range(1, 7)],
               [(0.9 + j * 0.0525, 60 / (0.9 + j * 0.0525)) for j in range(0, 98)], 6, 70, "Nº de trabajadores", "Horas", [1, 2, 3, 4, 5, 6], [0, 20, 40, 60])
    return wrap(d + i, "Dos gráficas: la proporcionalidad directa es una recta que sale del origen (300 folios por libro); la inversa es una curva que baja (60 horas entre el número de trabajadores)")


def regla_de_tres():
    w, h = 340, 190
    c = lambda x, y, t, k=False: (f'<circle cx="{x}" cy="{y}" r="24" fill="{"var(--color-bg-surface)" if not k else "var(--color-bg-page)"}" '
                                  f'stroke="var(--color-border-strong)" stroke-width="1.5"{"" if not k else " stroke-dasharray=\"4 3\""}/>'
                                  f'<text x="{x}" y="{y+6}" text-anchor="middle" font-size="19" font-weight="600" fill="var(--color-text-primary)"{"" if t != "x" else " font-style=\"italic\""}>{t}</text>')
    o = ['<line x1="66" y1="95" x2="114" y2="95" stroke="var(--color-text-primary)" stroke-width="1.5"/>',
         '<line x1="206" y1="95" x2="254" y2="95" stroke="var(--color-text-primary)" stroke-width="1.5"/>',
         '<line x1="90" y1="140" x2="230" y2="50" stroke="var(--data-cat-1)" stroke-width="3"/>',
         '<line x1="90" y1="50" x2="230" y2="140" stroke="var(--data-cat-2)" stroke-width="2.5" stroke-dasharray="6 5"/>',
         '<rect x="146" y="80" width="28" height="30" rx="4" fill="var(--color-bg-page)"/>',
         '<text x="160" y="103" text-anchor="middle" font-size="22" fill="var(--color-text-primary)">=</text>',
         c(90, 50, "4", True), c(230, 50, "8"), c(90, 140, "7"), c(230, 140, "x", True),
         '<text x="292" y="26" text-anchor="middle" font-size="12.5" font-weight="600" fill="var(--color-text-primary)">multiplica</text>',
         '<text x="292" y="42" text-anchor="middle" font-size="12" fill="var(--color-text-secondary)">7 × 8</text>',
         '<text x="36" y="26" text-anchor="middle" font-size="12.5" font-weight="600" fill="var(--data-cat-2)">divide</text>',
         '<text x="36" y="42" text-anchor="middle" font-size="12" fill="var(--color-text-secondary)">entre 4</text>']
    return wrap("".join(o), "Regla de tres en cruz: en 4/7 = 8/x se multiplica 7 por 8 y se divide entre 4", w, h)


# nombre del archivo en los apuntes -> (título, figura)
def catalogo():
    return {
        "barras_coches": ("Coches estacionados según su marca", barras(["SEAT", "Mercedes", "BMW", "Otros"], [7, 4, 1, 5], "Frecuencia absoluta", "Barras: SEAT 7, Mercedes 4, BMW 1, Otros 5")),
        "barras_flores": ("Flores", barras(["Tulipanes", "Gardenias", "Rosas"], [500, 1500, 2000], "Número de flores", "Barras: tulipanes 500, gardenias 1.500, rosas 2.000")),
        "barras_comidas": ("Comida favorita", barras(["Macarrones", "Cocido", "Lubina", "Pisto", "Otra"], [8, 10, 5, 7, 12], "Personas", "Barras: macarrones 8, cocido 10, lubina 5, pisto 7, otra 12")),
        "sectores_calif": ("Calificaciones del alumnado", sectores(["Insuficiente", "Suficiente", "Bien", "Notable", "Sobresaliente"], [25, 25, 12.5, 25, 12.5], "Sectores: insuficiente 25 %, suficiente 25 %, bien 12,5 %, notable 25 %, sobresaliente 12,5 %")),
        "sectores_coches_color": ("Coches según su color", sectores(["Negros", "Blancos", "Verdes"], [5, 10, 5], "Sectores: negros 25 %, blancos 50 %, verdes 25 %")),
        "sectores_mates": ("Reparto del alumnado", sectores(["Matemáticas", "Otros", "Suspensos"], [100 / 3, 100 / 6, 50], "Sectores: matemáticas 33,33 %, otros 16,67 %, suspensos 50 %")),
        "sectores_tercios": ("Vehículos", sectores(["Motos", "Bicis", "Coches"], [1, 1, 1], "Sectores: motos, bicis y coches, un tercio cada uno")),
        "lineas_temp": ("Temperatura por día", lineas(["18/9", "19/9", "20/9", "21/9", "22/9", "23/9"], [37, 28, 37, 31, 42, 55], "°C", "Líneas: temperatura de 37, 28, 37, 31, 42 y 55 grados del 18 al 23 de septiembre", cero=True)),
        "lineas_peso": ("Bajada de peso por años", lineas([2019, 2020, 2021, 2022, 2023, 2024], [90, 86, 82, 78, 71, 66], "kg", "Líneas: peso de 90, 86, 82, 78, 71 y 66 kilos entre 2019 y 2024")),
        "lineas_alquiler": ("Precio medio mensual del alquiler", lineas([2021, 2022, 2023, 2024, 2025], [650, 680, 750, 790, 820], "€ al mes", "Líneas: alquiler de 650, 680, 750, 790 y 820 euros entre 2021 y 2025")),
        "lineas_1980": ("Evolución 1980–1995", lineas([1980, 1985, 1990, 1995], [1500, 1750, 1250, 1750], "Valor", "Líneas: 1.500 en 1980, 1.750 en 1985, 1.250 en 1990 y 1.750 en 1995")),
        "lineas_camiones": ("Camiones descargados", lineas([2019, 2020, 2021, 2022, 2023, 2024, 2025], [100000, 115000, 95000, 120000, 105000, 90000, 125000], "Camiones", "Líneas: camiones descargados, de 100.000 en 2019 a 125.000 en 2025")),
        "proporcionalidad": ("Proporcionalidad directa e inversa", proporcionalidad()),
        "regla-de-tres": ("Regla de tres en cruz", regla_de_tres()),
    }
