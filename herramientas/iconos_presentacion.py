"""Infografías (SVG) para los ejercicios de las presentaciones. Los colores salen de las variables del design system:
--slide-accent (color de la materia), --color-neutral-900 (negro), --color-neutral-0 (blanco)."""

AC = "var(--slide-accent)"
DK = "var(--color-neutral-900)"
WH = "var(--color-neutral-0)"
GR = "var(--color-neutral-300)"


def _svg(cuerpo, vb="0 0 280 200"):
    return f'<svg class="ds-slide__info" viewBox="{vb}" aria-hidden="true">{cuerpo}</svg>'


def _doc(titulo, filas, total):
    f = "".join(f'<text x="92" y="{78 + 24 * i}" font-size="13" fill="{DK}">{a}</text><text x="196" y="{78 + 24 * i}" font-size="13" text-anchor="end" fill="{DK}" font-weight="700">{b}</text><line x1="92" x2="196" y1="{84 + 24 * i}" y2="{84 + 24 * i}" stroke="{GR}"/>' for i, (a, b) in enumerate(filas))
    return _svg(
        f'<rect x="76" y="14" width="140" height="176" rx="12" fill="{WH}" stroke="{DK}" stroke-width="3"/>'
        f'<rect x="76" y="14" width="140" height="34" rx="12" fill="{DK}"/><rect x="76" y="34" width="140" height="14" fill="{DK}"/>'
        f'<text x="92" y="38" font-size="15" font-weight="800" fill="{AC}" letter-spacing="2">{titulo}</text>{f}'
        f'<rect x="88" y="150" width="116" height="30" rx="8" fill="{AC}"/><text x="98" y="171" font-size="14" font-weight="800" fill="{DK}">{total}</text><text x="196" y="171" font-size="18" font-weight="800" text-anchor="end" fill="{DK}">?</text>'
        , vb="66 6 160 192")


ICONOS = {
    "portatil": _svg(
        f'<rect x="52" y="22" width="176" height="116" rx="12" fill="{DK}"/><rect x="62" y="32" width="156" height="96" rx="6" fill="{AC}"/>'
        f'<rect x="76" y="48" width="70" height="10" rx="5" fill="{DK}" opacity=".85"/><rect x="76" y="66" width="108" height="8" rx="4" fill="{WH}" opacity=".8"/><rect x="76" y="82" width="90" height="8" rx="4" fill="{WH}" opacity=".8"/>'
        f'<circle cx="190" cy="104" r="18" fill="{DK}"/><text x="190" y="110" font-size="17" font-weight="800" text-anchor="middle" fill="{AC}">%</text>'
        f'<path d="M24 150h232l-10 18a10 10 0 0 1-9 6H43a10 10 0 0 1-9-6z" fill="{DK}"/><rect x="108" y="150" width="64" height="8" rx="4" fill="{GR}"/>'),
    "factura": _doc("FACTURA", [("Base", "···"), ("IVA 21 %", "···")], "TOTAL"),
    "nomina": _doc("NÓMINA", [("Bruto", "···"), ("Retenciones", "···")], "NETO"),
    "etiqueta": _svg(
        f'<path d="M40 100 120 20h100a14 14 0 0 1 14 14v100L154 214 40 114z" transform="translate(0 -20) scale(.95)" fill="{AC}" stroke="{DK}" stroke-width="4" stroke-linejoin="round"/>'
        f'<circle cx="198" cy="52" r="10" fill="{WH}" stroke="{DK}" stroke-width="3"/>'
        f'<text x="140" y="124" font-size="64" font-weight="800" text-anchor="middle" fill="{DK}" transform="rotate(-38 140 110)">%</text>'),
    "grafica": _svg(
        f'<rect x="36" y="20" width="208" height="160" rx="14" fill="{WH}" stroke="{DK}" stroke-width="3"/>'
        f'<rect x="58" y="120" width="34" height="42" rx="6" fill="{GR}"/><rect x="104" y="96" width="34" height="66" rx="6" fill="{AC}"/><rect x="150" y="74" width="34" height="88" rx="6" fill="{AC}"/><rect x="196" y="46" width="34" height="116" rx="6" fill="{DK}"/>'
        f'<path d="M58 100 112 76l38-16 52-24" fill="none" stroke="{DK}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/><path d="m190 32 14 2-2 14" fill="none" stroke="{DK}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>'),
    "casa": _svg(
        f'<rect x="60" y="92" width="160" height="96" rx="8" fill="{WH}" stroke="{DK}" stroke-width="3"/>'
        f'<path d="M40 100 140 22l100 78z" fill="{AC}" stroke="{DK}" stroke-width="4" stroke-linejoin="round"/>'
        f'<rect x="120" y="128" width="40" height="60" rx="6" fill="{DK}"/><rect x="76" y="112" width="32" height="30" rx="5" fill="{AC}" stroke="{DK}" stroke-width="3"/><rect x="172" y="112" width="32" height="30" rx="5" fill="{AC}" stroke="{DK}" stroke-width="3"/>'
        f'<rect x="168" y="42" width="22" height="34" fill="{DK}"/>'),
    "escritura": _svg(
        f'<rect x="64" y="12" width="152" height="176" rx="12" fill="{WH}" stroke="{DK}" stroke-width="3"/>'
        f'<rect x="80" y="30" width="72" height="10" rx="5" fill="{DK}"/><rect x="80" y="52" width="120" height="7" rx="3.5" fill="{GR}"/><rect x="80" y="68" width="104" height="7" rx="3.5" fill="{GR}"/><rect x="80" y="84" width="112" height="7" rx="3.5" fill="{GR}"/>'
        f'<path d="M92 150V122l24-18 24 18v28z" fill="{AC}" stroke="{DK}" stroke-width="3" stroke-linejoin="round"/><circle cx="184" cy="150" r="22" fill="{DK}"/><text x="184" y="158" font-size="22" font-weight="800" text-anchor="middle" fill="{AC}">%</text>'),
    "billetes": _svg(
        f'<rect x="40" y="62" width="180" height="104" rx="12" fill="{GR}" stroke="{DK}" stroke-width="3" transform="rotate(-6 130 114)"/>'
        f'<rect x="60" y="40" width="180" height="104" rx="12" fill="{AC}" stroke="{DK}" stroke-width="3"/>'
        f'<circle cx="150" cy="92" r="30" fill="{WH}" stroke="{DK}" stroke-width="3"/><text x="150" y="104" font-size="34" font-weight="800" text-anchor="middle" fill="{DK}">€</text>'
        f'<circle cx="84" cy="64" r="6" fill="{DK}"/><circle cx="216" cy="120" r="6" fill="{DK}"/>'
        f'<path d="M250 40l-16 24 14-2z M236 22v26" fill="none" stroke="{DK}" stroke-width="0"/>'),
    "abono": _svg(
        f'<rect x="34" y="40" width="212" height="120" rx="16" fill="{AC}" stroke="{DK}" stroke-width="3"/>'
        f'<rect x="34" y="62" width="212" height="26" fill="{DK}"/>'
        f'<rect x="52" y="108" width="44" height="32" rx="6" fill="{WH}" stroke="{DK}" stroke-width="3"/><path d="M52 124h44M74 108v32" stroke="{DK}" stroke-width="2"/>'
        f'<text x="228" y="140" font-size="34" font-weight="800" text-anchor="end" fill="{DK}">€</text>'
        f'<rect x="110" y="112" width="60" height="8" rx="4" fill="{DK}" opacity=".8"/><rect x="110" y="128" width="40" height="8" rx="4" fill="{DK}" opacity=".5"/>'),
    "maletin": _svg(
        f'<path d="M100 66V50a12 12 0 0 1 12-12h56a12 12 0 0 1 12 12v16" fill="none" stroke="{DK}" stroke-width="6"/>'
        f'<rect x="36" y="64" width="208" height="116" rx="16" fill="{DK}"/><rect x="36" y="104" width="208" height="8" fill="{AC}"/>'
        f'<rect x="124" y="94" width="32" height="30" rx="6" fill="{AC}"/>'
        f'<circle cx="214" cy="52" r="26" fill="{AC}" stroke="{DK}" stroke-width="3"/><text x="214" y="62" font-size="28" font-weight="800" text-anchor="middle" fill="{DK}">%</text>'),
}
