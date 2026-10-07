/* =====================================================================
   FÓRMULAS — convierte texto con fórmulas entre signos $ … $ en HTML.
   Entiende un subconjunto sencillo de LaTeX (el mismo que se usa en datos/preguntas.js):
     \frac{a}{b}   fracción        x^2  x^{10}  potencia       x_v  subíndice
     \sqrt{…}      raíz            \cdot \times \pi \approx \le \ge \neq \pm …  símbolos
   No necesita ninguna librería externa y se imprime bien en PDF.
   ===================================================================== */
const MATE = (function () {
  const SIMBOLOS = {
    cdot: "·", times: "×", div: "÷", pm: "±", pi: "π", approx: "≈", neq: "≠", le: "≤", ge: "≥",
    infty: "∞", alpha: "α", beta: "β", theta: "θ", sigma: "σ", mu: "μ", Delta: "Δ", rightarrow: "→", degree: "°"
  };

  function esc(s) {
    return String(s).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  }

  // Lee un grupo { … } que empieza en s[i] y devuelve [contenido, índice siguiente]
  function grupo(s, i) {
    if (s[i] !== "{") return [s[i] || "", i + 1];
    let nivel = 0;
    for (let j = i; j < s.length; j++) {
      if (s[j] === "{") nivel++;
      else if (s[j] === "}") { nivel--; if (nivel === 0) return [s.slice(i + 1, j), j + 1]; }
    }
    return [s.slice(i + 1), s.length];
  }

  function formula(s) {
    let salida = "", i = 0;
    while (i < s.length) {
      const c = s[i];
      if (c === "\\") {
        let j = i + 1;
        while (j < s.length && /[a-zA-Z]/.test(s[j])) j++;
        const nombre = s.slice(i + 1, j);
        if (nombre === "") { salida += esc(s[i + 1] || ""); i += 2; continue; }   // \% \{ \$ …
        i = j;
        if (nombre === "frac") {
          const [a, k] = grupo(s, i); const [b, k2] = grupo(s, k); i = k2;
          salida += '<span class="fr"><span class="fr__n">' + formula(a) + '</span><span class="fr__d">' + formula(b) + "</span></span>";
        } else if (nombre === "sqrt") {
          const [a, k] = grupo(s, i); i = k;
          salida += '<span class="rz"><span class="rz__s">√</span><span class="rz__c">' + formula(a) + "</span></span>";
        } else if (SIMBOLOS[nombre]) {
          salida += SIMBOLOS[nombre];
        } else {
          salida += esc(nombre);
        }
        continue;
      }
      if (c === "^" || c === "_") {
        const [a, k] = grupo(s, i + 1); i = k;
        salida += (c === "^" ? "<sup>" : "<sub>") + formula(a) + (c === "^" ? "</sup>" : "</sub>");
        continue;
      }
      if (c === "{") { const [a, k] = grupo(s, i); salida += formula(a); i = k; continue; }
      salida += /[a-zA-Z]/.test(c) ? "<i>" + c + "</i>" : esc(c);   // variables en cursiva
      i++;
    }
    return salida;
  }

  // Texto con fórmulas entre $…$ (usa \$ para un signo de dólar literal)
  function texto(s) {
    const partes = String(s).replace(/\\\$/g, "\u0000").split("$");
    return partes.map((p, n) => {
      const t = p.replace(/\u0000/g, "$");
      return n % 2 === 1 ? '<span class="mate">' + formula(t) + "</span>" : esc(t);
    }).join("");
  }

  return { texto, formula };
})();
