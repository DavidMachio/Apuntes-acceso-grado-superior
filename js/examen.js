/* =====================================================================
   GENERADOR DE EXAMEN
   · Elige preguntas del banco (datos/preguntas.js) según los temas, el número y el tipo.
   · Cada examen tiene un CÓDIGO que contiene esa configuración y una semilla aleatoria:
     con el mismo código siempre sale el mismo examen (y sus soluciones).
   · Se imprime (o se guarda como PDF) desde el navegador, en tamaño A4.
   ===================================================================== */
(function () {
  const { esc, ic } = DS;
  const LETRAS = "ABCDE";
  const ALFABETO = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789";   // sin O, 0, I, 1 para evitar confusiones
  const PUNTOS_TEST = 1, PUNTOS_CALCULO = 2;
  const MIN_TEST = 2, MIN_CALCULO = 8;                   // minutos orientativos por pregunta
  const REGEX_CODIGO = /^(\d+)-(\d+(?:\.\d+)*)-(\d+)-([MTP])-([A-Z0-9]{5})$/;

  // Temas que tienen preguntas en el banco
  const disponibles = MODULOS
    .map((m, i) => ({ num: i + 1, titulo: m.titulo, preguntas: PREGUNTAS[i + 1] || [] }))
    .filter(m => m.preguntas.length > 0);

  const el = id => document.getElementById(id);
  const formExamen = el("form-examen"), formCodigo = el("form-codigo");
  const tituloBase = document.title;
  let examenActual = null;

  /* ---------------- Números aleatorios reproducibles ---------------- */
  function crearRng(semilla) {
    let h = 1779033703 ^ semilla.length;
    for (let i = 0; i < semilla.length; i++) {
      h = Math.imul(h ^ semilla.charCodeAt(i), 3432918353);
      h = (h << 13) | (h >>> 19);
    }
    let a = Math.imul(h ^ (h >>> 16), 2246822507);
    a = Math.imul(a ^ (a >>> 13), 3266489909);
    a = (a ^ (a >>> 16)) >>> 0;
    return function () {
      a |= 0; a = (a + 0x6D2B79F5) | 0;
      let t = Math.imul(a ^ (a >>> 15), 1 | a);
      t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }
  function barajar(lista, rng) {
    const a = lista.slice();
    for (let i = a.length - 1; i > 0; i--) {
      const j = Math.floor(rng() * (i + 1));
      const t = a[i]; a[i] = a[j]; a[j] = t;
    }
    return a;
  }
  function nuevaSemilla() {
    let s = "";
    for (let i = 0; i < 5; i++) s += ALFABETO[Math.floor(Math.random() * ALFABETO.length)];
    return s;
  }

  /* ---------------- Código del examen ---------------- */
  function crearCodigo(c) {
    return [BANCO_VERSION, c.modulos.join("."), c.n, c.tipo, c.semilla].join("-");
  }
  function leerCodigo(texto) {
    const m = REGEX_CODIGO.exec(String(texto).trim().toUpperCase());
    if (!m) return { error: "El código no tiene el formato correcto. Cópialo tal como aparece en el examen." };
    const modulos = m[2].split(".").map(Number);
    const validos = disponibles.map(d => d.num);
    if (modulos.some(n => validos.indexOf(n) === -1)) return { error: "El código incluye temas que no existen en este temario." };
    const n = Number(m[3]);
    if (n < 1) return { error: "El código no es válido." };
    return { cfg: { version: Number(m[1]), modulos: modulos, n: n, tipo: m[4], semilla: m[5] } };
  }

  /* ---------------- Elección de preguntas ---------------- */
  function construir(cfg) {
    const rng = crearRng(cfg.semilla);

    function reunir(tipo) {
      const lista = [];
      cfg.modulos.forEach(num => {
        (PREGUNTAS[num] || []).forEach(p => { if (p.tipo === tipo) lista.push(Object.assign({}, p, { modulo: num })); });
      });
      return lista;
    }
    const pTest = reunir("test"), pCalc = reunir("calculo");

    // Cuántas de cada tipo
    let nTest = 0, nCalc = 0;
    if (cfg.tipo === "T") nTest = Math.min(cfg.n, pTest.length);
    else if (cfg.tipo === "P") nCalc = Math.min(cfg.n, pCalc.length);
    else {
      nTest = Math.min(Math.round(cfg.n * 0.7), pTest.length);
      nCalc = Math.min(cfg.n - nTest, pCalc.length);
      let falta = cfg.n - nTest - nCalc;
      if (falta > 0) { nTest = Math.min(nTest + falta, pTest.length); falta = cfg.n - nTest - nCalc; }
      if (falta > 0) nCalc = Math.min(nCalc + falta, pCalc.length);
    }

    // Reparte las preguntas entre los temas por turnos, para que todos estén representados
    function elegir(pool, k) {
      const porModulo = {};
      pool.forEach(p => { (porModulo[p.modulo] = porModulo[p.modulo] || []).push(p); });
      const orden = barajar(Object.keys(porModulo), rng);
      const colas = {};
      orden.forEach(m => { colas[m] = barajar(porModulo[m], rng); });
      const elegidas = [];
      while (elegidas.length < k) {
        let avanzo = false;
        for (let i = 0; i < orden.length && elegidas.length < k; i++) {
          if (colas[orden[i]].length) { elegidas.push(colas[orden[i]].shift()); avanzo = true; }
        }
        if (!avanzo) break;
      }
      return elegidas.sort((a, b) => a.modulo - b.modulo);
    }

    const tests = elegir(pTest, nTest).map(p => {
      const orden = barajar(p.opciones.map((_, i) => i), rng);
      return Object.assign({}, p, {
        opciones: orden.map(i => p.opciones[i]),
        correcta: orden.indexOf(p.correcta),
        puntos: p.puntos || PUNTOS_TEST
      });
    });
    const calculos = elegir(pCalc, nCalc).map(p => Object.assign({}, p, { puntos: p.puntos || PUNTOS_CALCULO }));

    let n = 0;
    tests.forEach(p => { p.numero = ++n; });
    calculos.forEach(p => { p.numero = ++n; });

    const puntos = tests.concat(calculos).reduce((s, p) => s + p.puntos, 0);
    const minutos = Math.max(5, Math.round((tests.length * MIN_TEST + calculos.length * MIN_CALCULO) / 5) * 5);
    return { cfg: cfg, codigo: crearCodigo(cfg), tests: tests, calculos: calculos, total: n, puntos: puntos, minutos: minutos };
  }

  /* ---------------- Dibujo de las hojas ---------------- */
  function enunciado(p) { return MATE.texto(p.enunciado); }
  function puntosTxt(p) { return p.puntos + (p.puntos === 1 ? " punto" : " puntos"); }
  function nombreModulo(num) { return MODULOS[num - 1].titulo; }

  function cabecera(ex, soluciones) {
    const modulos = ex.cfg.modulos.map(nombreModulo).join(", ");
    const datos = soluciones ? "" :
      '<div class="hoja__datos">' +
      '<div><span class="dato__et">Nombre y apellidos</span><span class="dato__linea"></span></div>' +
      '<div><span class="dato__et">Fecha</span><span class="dato__linea"></span></div>' +
      '<div class="dato--nota"><span class="dato__et">Nota (sobre 10)</span><span class="dato__linea"></span></div></div>';
    return '<header class="hoja__cab">' +
      '<div class="hoja__fila"><span>' + esc(CURSO.marca) + '</span><span class="hoja__codigo">Código ' + esc(ex.codigo) + "</span></div>" +
      '<h2 class="hoja__titulo">' + esc(CURSO.examenTitulo) + (soluciones ? ": soluciones" : "") + "</h2>" +
      '<p class="hoja__modulos">' + esc(modulos) + "</p>" + datos +
      '<ul class="hoja__info"><li>Tiempo recomendado: ' + ex.minutos + " minutos</li><li>Puntuación total: " + ex.puntos +
      " puntos</li><li>" + ex.total + (ex.total === 1 ? " pregunta" : " preguntas") + "</li></ul></header>";
  }

  function hojaExamen(ex) {
    let html = cabecera(ex, false);
    const letraProblemas = ex.tests.length ? "B" : "A";

    html += '<p class="hoja__instr"><b>Instrucciones.</b> Escribe con bolígrafo azul o negro. ' +
      (ex.tests.length ? "En el test, marca con una X una sola respuesta por pregunta; no se resta por error. " : "") +
      (ex.calculos.length ? "En los problemas, escribe el desarrollo completo: se valora el procedimiento, no solo el resultado." : "") + "</p>";

    if (ex.tests.length) {
      html += '<section class="parte"><h3 class="parte__titulo">Parte A: test</h3>' +
        '<p class="parte__nota">Marca con una X la respuesta correcta. Cada pregunta vale ' + PUNTOS_TEST + ' punto.</p>' +
        '<ol class="preguntas" style="--n0:0">' + ex.tests.map(p => {
          const largas = p.opciones.some(o => o.length > 34);
          return '<li class="pregunta"><div class="pregunta__cab"><div class="pregunta__enun">' + enunciado(p) + '</div><span class="pregunta__pts">' + puntosTxt(p) + "</span></div>" +
            '<ul class="opciones' + (largas ? " opciones--largas" : "") + '">' + p.opciones.map((o, i) =>
              '<li><span class="casilla" aria-hidden="true"></span><b>' + LETRAS[i] + ")</b><span>" + MATE.texto(o) + "</span></li>").join("") + "</ul></li>";
        }).join("") + "</ol></section>";
    }
    if (ex.calculos.length) {
      html += '<section class="parte"><h3 class="parte__titulo">Parte ' + letraProblemas + ': problemas</h3>' +
        '<p class="parte__nota">Escribe el desarrollo en el recuadro y el resultado final en la línea de respuesta. Cada problema vale ' + PUNTOS_CALCULO + ' puntos.</p>' +
        '<ol class="preguntas" style="--n0:' + ex.tests.length + '">' + ex.calculos.map(p =>
          '<li class="pregunta"><div class="pregunta__cab"><div class="pregunta__enun">' + enunciado(p) + '</div><span class="pregunta__pts">' + puntosTxt(p) + "</span></div>" +
          '<div class="desarrollo desarrollo--' + (p.espacio || "m") + '" aria-hidden="true"></div>' +
          '<div class="respuesta"><span>Respuesta:</span><i></i></div></li>').join("") + "</ol></section>";
    }
    return html;
  }

  function hojaSoluciones(ex) {
    let html = cabecera(ex, true);

    if (ex.tests.length) {
      html += '<section class="parte"><h3 class="parte__titulo">Respuestas del test</h3><div class="claves">' +
        ex.tests.map(p => '<div class="clave"><b>' + p.numero + "</b><span>" + LETRAS[p.correcta] + "</span></div>").join("") + "</div></section>";
    }

    html += '<section class="parte"><h3 class="parte__titulo">Explicaciones</h3><ul class="soluciones">';
    ex.tests.forEach(p => {
      html += '<li class="sol"><div class="sol__cab"><b>Pregunta ' + p.numero + '</b><span>' + esc(nombreModulo(p.modulo)) + "</span></div>" +
        '<div class="sol__enun">' + enunciado(p) + "</div>" +
        '<p><b>Respuesta correcta:</b> ' + LETRAS[p.correcta] + ') ' + MATE.texto(p.opciones[p.correcta]) + "</p>" +
        (p.explicacion ? "<p>" + MATE.texto(p.explicacion) + "</p>" : "") + "</li>";
    });
    ex.calculos.forEach(p => {
      html += '<li class="sol"><div class="sol__cab"><b>Problema ' + p.numero + '</b><span>' + esc(nombreModulo(p.modulo)) + "</span></div>" +
        '<div class="sol__enun">' + enunciado(p) + "</div>" +
        "<p><b>Resolución</b></p><ol class=\"pasos\">" + (p.solucion || []).map(s => "<li>" + MATE.texto(s) + "</li>").join("") + "</ol>" +
        "<p><b>Respuesta:</b> " + MATE.texto(p.respuesta || "") + "</p></li>";
    });
    html += "</ul></section>";

    html += '<section class="parte"><h3 class="parte__titulo">Criterios de corrección</h3>' +
      "<p>Test: " + PUNTOS_TEST + " punto por respuesta correcta; no se resta por error. Problemas: " + PUNTOS_CALCULO +
      " puntos cada uno (1 punto por el planteamiento y 1 por el resultado correcto). Nota sobre 10 = puntos obtenidos × 10 ÷ " + ex.puntos + ".</p></section>";
    return html;
  }

  /* ---------------- Interfaz ---------------- */
  function mostrarPanel(cual) {
    ["examen", "soluciones"].forEach(id => {
      const activo = id === cual;
      el("panel-" + id).hidden = !activo;
      el("tab-" + id).setAttribute("aria-selected", String(activo));
    });
  }

  function mostrar(ex, aviso) {
    examenActual = ex;
    el("hoja-examen").innerHTML = hojaExamen(ex);
    el("hoja-soluciones").innerHTML = hojaSoluciones(ex);
    el("resumen-examen").textContent = ex.total + (ex.total === 1 ? " pregunta" : " preguntas") + ", " + ex.puntos +
      " puntos, " + ex.minutos + " minutos. Código: " + ex.codigo;
    el("aviso").hidden = !aviso;
    if (aviso) el("aviso-texto").textContent = aviso;
    el("resultado").hidden = false;
    mostrarPanel("examen");
    document.title = "Examen " + ex.codigo;
    try { history.replaceState(null, "", "#" + ex.codigo); } catch (e) {}
    el("resultado").scrollIntoView({ behavior: "smooth", block: "start" });
  }

  function leerFormulario() {
    const modulos = Array.prototype.slice.call(document.querySelectorAll('input[name="modulo"]:checked')).map(i => Number(i.value));
    return { modulos: modulos, n: parseInt(el("n").value, 10), tipo: el("tipo").value };
  }

  function disponiblesPara(modulos, tipo) {
    let total = 0;
    modulos.forEach(num => {
      (PREGUNTAS[num] || []).forEach(p => {
        if (tipo === "M" || (tipo === "T" && p.tipo === "test") || (tipo === "P" && p.tipo === "calculo")) total++;
      });
    });
    return total;
  }

  function actualizarAyuda() {
    const f = leerFormulario();
    const total = disponiblesPara(f.modulos, f.tipo);
    el("n").max = Math.max(total, 1);
    el("n-ayuda").textContent = f.modulos.length === 0
      ? "Elige al menos un tema."
      : "Hay " + total + (total === 1 ? " pregunta disponible" : " preguntas disponibles") + " con esta selección.";
    el("error-modulos").hidden = f.modulos.length > 0;
  }

  function aplicarConfiguracion(cfg) {
    document.querySelectorAll('input[name="modulo"]').forEach(i => { i.checked = cfg.modulos.indexOf(Number(i.value)) !== -1; });
    el("n").value = cfg.n;
    el("tipo").value = cfg.tipo;
    actualizarAyuda();
  }

  function generar(semilla) {
    const f = leerFormulario();
    if (f.modulos.length === 0) {
      el("error-modulos").hidden = false;
      const primero = document.querySelector('input[name="modulo"]');
      if (primero) primero.focus();
      return;
    }
    const total = disponiblesPara(f.modulos, f.tipo);
    if (total === 0) { el("n-ayuda").textContent = "No hay preguntas de este tipo en los temas elegidos."; return; }
    let n = isNaN(f.n) || f.n < 1 ? 10 : f.n;
    n = Math.min(n, total);
    el("n").value = n;
    mostrar(construir({ version: BANCO_VERSION, modulos: f.modulos, n: n, tipo: f.tipo, semilla: semilla || nuevaSemilla() }), "");
  }

  function recuperar(texto) {
    const r = leerCodigo(texto);
    if (r.error) {
      el("codigo-error-texto").textContent = r.error;
      el("codigo-error").hidden = false;
      el("codigo").setAttribute("aria-invalid", "true");
      return false;
    }
    el("codigo-error").hidden = true;
    el("codigo").removeAttribute("aria-invalid");
    aplicarConfiguracion(r.cfg);
    const ex = construir(r.cfg);
    const aviso = r.cfg.version !== BANCO_VERSION
      ? "Este código es de una versión anterior del banco de preguntas, así que el examen puede no ser igual al original."
      : "";
    mostrar(ex, aviso);
    return true;
  }

  function imprimir(cual) {
    if (!examenActual) return;
    mostrarPanel(cual);
    document.title = (cual === "examen" ? "Examen " : "Soluciones ") + examenActual.codigo;
    window.print();
  }

  /* ---------------- Arranque ---------------- */
  el("lista-modulos").innerHTML = disponibles.length === 0
    ? '<p class="ds-small ds-muted">Todavía no hay preguntas en el banco.</p>'
    : disponibles.map(m =>
      '<label class="ds-check"><input type="checkbox" name="modulo" value="' + m.num + '" checked><span>' + esc(m.titulo) +
      ' <span class="ds-caption">(' + m.preguntas.length + (m.preguntas.length === 1 ? " pregunta" : " preguntas") + ")</span></span></label>").join("");

  // Si se llega desde el temario (examen.html?modulo=2), solo se marca ese tema
  const modulo = parseInt(new URLSearchParams(location.search).get("modulo"), 10);
  if (modulo && disponibles.some(d => d.num === modulo)) {
    document.querySelectorAll('input[name="modulo"]').forEach(i => { i.checked = Number(i.value) === modulo; });
  }
  actualizarAyuda();

  document.querySelectorAll('input[name="modulo"]').forEach(i => i.addEventListener("change", actualizarAyuda));
  el("tipo").addEventListener("change", actualizarAyuda);
  formExamen.addEventListener("submit", e => { e.preventDefault(); generar(); });
  formCodigo.addEventListener("submit", e => { e.preventDefault(); recuperar(el("codigo").value); });
  el("btn-imprimir-examen").addEventListener("click", () => imprimir("examen"));
  el("btn-imprimir-soluciones").addEventListener("click", () => imprimir("soluciones"));
  el("btn-otro").addEventListener("click", () => {
    if (!examenActual) return;
    aplicarConfiguracion(examenActual.cfg);
    generar();
  });
  window.addEventListener("afterprint", () => { document.title = examenActual ? "Examen " + examenActual.codigo : tituloBase; });

  // Pestañas Examen / Soluciones
  ["examen", "soluciones"].forEach(id => el("tab-" + id).addEventListener("click", () => mostrarPanel(id)));

  // Si la dirección trae un código (examen.html#1-1.2-10-M-K7Q2F), se recupera ese examen
  function recuperarDeLaDireccion() {
    const enHash = decodeURIComponent(location.hash.replace(/^#/, ""));
    if (REGEX_CODIGO.test(enHash.toUpperCase()) && (!examenActual || examenActual.codigo !== enHash.toUpperCase())) recuperar(enHash);
  }
  window.addEventListener("hashchange", recuperarDeLaDireccion);
  recuperarDeLaDireccion();
})();
