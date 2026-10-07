/* Visor de PDF página a página (pdf.js): escenario oscuro, flechas, contador, miniaturas, ampliar y descargar.
   Uso: Visor.abrir(elementoContenedor, { archivo, nombre }). La librería está en js/vendor/ (no depende de ningún servicio externo). */
const Visor = (function () {
  const esc = s => String(s).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  const ic = (id) => '<svg class="ds-icon" aria-hidden="true" focusable="false"><use href="#' + id + '"/></svg>';
  if (window.pdfjsLib) pdfjsLib.GlobalWorkerOptions.workerSrc = new URL("vendor/pdf.worker.js", document.currentScript ? document.currentScript.src : location.href).href;

  let doc = null, pagina = 1, tarea = null, observador = null, ampliado = false, sesion = 0;

  function abrir(cont, opciones) {
    const id = ++sesion;
    cont.innerHTML =
      '<div class="vp" role="region" aria-label="Visor de ' + esc(opciones.nombre) + '">' +
      '<div class="vp__stage"><button class="vp__flecha vp__flecha--prev" type="button" aria-label="Página anterior">' + ic("i-chevron-left") + "</button>" +
      '<div class="vp__hoja"><canvas class="vp__canvas" tabindex="0" aria-label="Página actual (clic para ampliar)"></canvas><p class="vp__estado" role="status">Cargando…</p></div>' +
      '<button class="vp__flecha vp__flecha--next" type="button" aria-label="Página siguiente">' + ic("i-chevron-right") + "</button>" +
      '<button class="vp__redondo vp__zoom" type="button" aria-label="Ampliar página">' + ic("i-eye") + "</button>" +
      '<a class="vp__redondo vp__desc" href="' + esc(opciones.archivo) + '" download aria-label="Descargar PDF">' + ic("i-download") + "</a></div>" +
      '<div class="vp__pie"><p class="vp__contador" id="vpContador"></p><div class="vp__tira" role="list"></div></div></div>' +
      '<div class="vp__luz" hidden><button class="vp__cerrar" type="button" aria-label="Cerrar">' + ic("i-close") + '</button><canvas class="vp__luz-canvas"></canvas>' +
      '<p class="vp__pista">Clic para ampliar o reducir · ← → para cambiar de página · Esc para cerrar</p></div>';

    const $ = s => cont.querySelector(s);
    const canvas = $(".vp__canvas"), estado = $(".vp__estado"), tira = $(".vp__tira"), luz = $(".vp__luz"), lc = $(".vp__luz-canvas");
    if (!window.pdfjsLib) { estado.innerHTML = 'No se pudo cargar el visor. <a href="' + esc(opciones.archivo) + '">Abrir el PDF</a>'; return; }
    if (observador) observador.disconnect();
    if (tarea) { try { tarea.cancel(); } catch (e) {} }

    async function pintar(c, pag, ancho, dpr) {
      const base = pag.getViewport({ scale: 1 });
      const escala = ancho / base.width;
      const vp = pag.getViewport({ scale: escala * dpr });
      c.width = Math.round(vp.width); c.height = Math.round(vp.height);
      c.style.width = Math.round(vp.width / dpr) + "px"; c.style.height = Math.round(vp.height / dpr) + "px";
      return pag.render({ canvasContext: c.getContext("2d"), viewport: vp });
    }

    async function ir(n) {
      if (!doc || id !== sesion) return;
      pagina = Math.min(Math.max(n, 1), doc.numPages);
      $(".vp__flecha--prev").disabled = pagina === 1;
      $(".vp__flecha--next").disabled = pagina === doc.numPages;
      $("#vpContador").textContent = pagina + " / " + doc.numPages;
      tira.querySelectorAll(".vp__mini").forEach(b => {
        const act = Number(b.dataset.i) === pagina; b.classList.toggle("is-active", act);
        if (act) b.scrollIntoView({ block: "nearest", inline: "center", behavior: "smooth" });
      });
      if (tarea) { try { tarea.cancel(); } catch (e) {} }
      const pag = await doc.getPage(pagina);
      if (id !== sesion) return;
      const ancho = Math.min($(".vp__hoja").clientWidth || 900, 1280);
      tarea = await pintar(canvas, pag, ancho, Math.min(window.devicePixelRatio || 1, 2));
      try { await tarea.promise; estado.hidden = true; } catch (e) { /* render cancelado */ }
      if (!luz.hidden) ampliar(ampliado);
    }

    async function ampliar(zoom) {
      ampliado = zoom;
      const pag = await doc.getPage(pagina);
      const ancho = zoom ? 2200 : Math.min(window.innerWidth - 48, 1500, (window.innerHeight - 112) * 16 / 9);
      const dpr = zoom ? 1 : Math.min(window.devicePixelRatio || 1, 2);
      lc.classList.toggle("is-zoom", zoom);
      const t = await pintar(lc, pag, ancho, dpr); try { await t.promise; } catch (e) {}
    }
    function abrirLuz() { luz.hidden = false; document.body.style.overflow = "hidden"; ampliar(false); luz.querySelector(".vp__cerrar").focus(); }
    function cerrarLuz() { luz.hidden = true; document.body.style.overflow = ""; canvas.focus(); }

    $(".vp__flecha--prev").onclick = () => ir(pagina - 1);
    $(".vp__flecha--next").onclick = () => ir(pagina + 1);
    canvas.onclick = abrirLuz; $(".vp__zoom").onclick = abrirLuz;
    luz.querySelector(".vp__cerrar").onclick = cerrarLuz;
    lc.onclick = () => ampliar(!ampliado);
    luz.onclick = e => { if (e.target === luz) cerrarLuz(); };
    const teclas = e => {
      if (id !== sesion || !document.body.contains(cont)) return document.removeEventListener("keydown", teclas);
      if (e.key === "ArrowRight" || e.key === "PageDown") { ir(pagina + 1); if (!luz.hidden) e.preventDefault(); }
      else if (e.key === "ArrowLeft" || e.key === "PageUp") { ir(pagina - 1); if (!luz.hidden) e.preventDefault(); }
      else if (e.key === "Escape" && !luz.hidden) cerrarLuz();
    };
    document.addEventListener("keydown", teclas);
    let rt; window.addEventListener("resize", () => { clearTimeout(rt); rt = setTimeout(() => id === sesion && doc && ir(pagina), 200); });

    pdfjsLib.getDocument({ url: opciones.archivo }).promise.then(d => {
      if (id !== sesion) return;
      doc = d;
      for (let i = 1; i <= d.numPages; i++) {
        const b = document.createElement("button");
        b.type = "button"; b.className = "vp__mini"; b.dataset.i = i; b.setAttribute("aria-label", "Ir a la página " + i);
        b.innerHTML = '<canvas></canvas><span>' + i + "</span>";
        b.onclick = () => ir(i); tira.appendChild(b);
      }
      observador = new IntersectionObserver(es => es.forEach(async en => {
        if (!en.isIntersecting) return;
        const b = en.target; observador.unobserve(b);
        const pag = await d.getPage(Number(b.dataset.i)); if (id !== sesion) return;
        const t = await pintar(b.querySelector("canvas"), pag, 176, 1); try { await t.promise; } catch (e) {}
      }), { root: tira, rootMargin: "0px 400px" });
      tira.querySelectorAll(".vp__mini").forEach(b => observador.observe(b));
      ir(1);
    }).catch(() => { estado.innerHTML = 'No se pudo abrir el PDF. <a href="' + esc(opciones.archivo) + '" target="_blank" rel="noopener">Ábrelo en otra pestaña</a>.'; });
  }
  return { abrir };
})();
