/* Cartel de cada materia (estilo de las portadas de los PDF): fondo oscuro, marca de agua y datos del curso.
   El texto del curso sale de SITIO.curso (datos/sitio.js). Los colores salen de los tokens del sistema. */
(function () {
  const esc = s => String(s).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  const T = (x, y, s, size, rot) => '<text x="' + x + '" y="' + y + '" font-size="' + size + '" transform="rotate(' + (rot || 0) + ' ' + x + ' ' + y + ')">' + esc(s) + "</text>";

  // Marcas de agua: operaciones y cuentas / letras y frases
  const MARCAS = {
    matematicas: T(330, 120, "%", 190, -8) + T(40, 250, "€", 150, 10) + T(300, 330, "×", 120, 0) + T(150, 90, "+", 90, 0) +
      T(240, 215, "÷", 100, 0) + T(20, 120, "=", 90, -10) + T(345, 215, "√", 90, 8) + T(110, 335, "π", 80, -6) +
      T(250, 60, "25 · 4 = 100", 20, 0) + T(30, 190, "21 %", 24, -6) +
      '<g fill="none" stroke="currentColor" stroke-width="5" opacity=".9"><rect x="290" y="250" width="22" height="50"/><rect x="320" y="220" width="22" height="80"/><rect x="350" y="180" width="22" height="120"/></g>',
    lengua: T(300, 150, "Aa", 170, -6) + T(30, 120, "¿?", 120, 8) + T(40, 270, "«»", 110, 0) + T(330, 290, "ñ", 130, 6) +
      T(160, 60, "¡!", 80, -8) + T(190, 210, "—", 100, 0) +
      T(30, 330, "Había una vez…", 22, -4) + T(210, 245, "sujeto + predicado", 19, 0) + T(220, 330, "ortografía · gramática", 17, 0)
  };
  const TEXTO = {
    matematicas: { titulo: "Matemáticas", sub: "Prueba de acceso a grado superior" },
    lengua: { titulo: "Lengua", sub: "Prueba de acceso a grado superior" }
  };

  document.querySelectorAll("[data-cartel]").forEach(el => {
    const id = el.getAttribute("data-cartel");
    const t = TEXTO[id]; if (!t) return;
    el.innerHTML =
      '<svg class="cartel__marca" viewBox="0 0 400 360" preserveAspectRatio="xMaxYMid slice" fill="currentColor" focusable="false">' + MARCAS[id] + "</svg>" +
      '<div class="cartel__texto"><span class="cartel__pill">' + esc((typeof SITIO !== "undefined" && SITIO.curso) || "") + "</span>" +
      "<strong>" + esc(t.titulo) + "</strong><span>" + esc(t.sub) + "</span></div>";
  });
})();
