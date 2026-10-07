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
