/* Resize the parent iframe to document height (Markdown scrolls, not the embed). */
(function () {
  if (window.__qmEmbedFit) return;
  window.__qmEmbedFit = true;

  function measure() {
    var root = document.documentElement;
    var body = document.body;
    if (!body) return 0;
    var rootEl =
      document.querySelector("#deutsch-demo") ||
      document.querySelector("#dj-oracle-demo") ||
      document.querySelector("main") ||
      document.querySelector(".container") ||
      document.querySelector(".quiz-container") ||
      document.querySelector(".card") ||
      document.querySelector("article.card") ||
      document.querySelector(".target-state") ||
      document.querySelector(".phase-demo") ||
      document.querySelector(".superposition-demo") ||
      document.querySelector(".cnot-minus") ||
      document.querySelector(".signs-explorer") ||
      document.querySelector(".parity-explorer");
    var mainH = 0;
    var bodySt = window.getComputedStyle(body);
    var pad =
      (parseFloat(bodySt.paddingTop) || 0) +
      (parseFloat(bodySt.paddingBottom) || 0);
    if (
      rootEl &&
      ((rootEl.classList && rootEl.classList.contains("quiz-container")) ||
        rootEl.id === "deutsch-demo" ||
        rootEl.id === "dj-oracle-demo")
    ) {
      var qr = rootEl.getBoundingClientRect();
      var qst = window.getComputedStyle(rootEl);
      return Math.ceil(
        qr.height +
        (parseFloat(qst.marginTop) || 0) +
        (parseFloat(qst.marginBottom) || 0) +
        pad
      );
    }
    if (rootEl) {
      var r = rootEl.getBoundingClientRect();
      var st = window.getComputedStyle(rootEl);
      mainH =
        r.height +
        (parseFloat(st.marginTop) || 0) +
        (parseFloat(st.marginBottom) || 0);
    }
    return Math.ceil(
      Math.max(
        root.scrollHeight,
        body.scrollHeight,
        mainH + pad,
        body.getBoundingClientRect().height
      )
    );
  }

  var last = 0;
  function fit() {
    var h = measure();
    if (!h) return;
    if (last && Math.abs(h - last) < 1) return;
    last = h;
    var frame = window.frameElement;
    if (frame) {
      frame.style.height = h + "px";
      frame.setAttribute("height", String(h));
      frame.scrolling = "no";
    }
    try {
      if (window.parent && window.parent !== window) {
        window.parent.postMessage({ type: "qm-embed-height", height: h }, "*");
      }
    } catch (e) {}
  }

  function schedule() {
    window.requestAnimationFrame(fit);
  }
  window.qmEmbedFitSchedule = schedule;

  function start() {
    schedule();
    window.setTimeout(schedule, 50);
    window.setTimeout(schedule, 200);
    window.setTimeout(schedule, 600);
    window.addEventListener("load", schedule);
    window.addEventListener("resize", schedule);
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(schedule);
    document.addEventListener("click", function () {
      window.setTimeout(schedule, 40);
    });
    document.addEventListener("input", schedule);
    document.addEventListener("change", schedule);
    if (window.ResizeObserver) {
      var ro = new ResizeObserver(schedule);
      if (document.body) ro.observe(document.body);
      var rootEl =
        document.querySelector("#deutsch-demo") ||
        document.querySelector("#dj-oracle-demo") ||
        document.querySelector("main") ||
        document.querySelector(".container") ||
        document.querySelector(".quiz-container") ||
        document.querySelector(".card") ||
        document.querySelector("article.card") ||
        document.querySelector(".target-state") ||
        document.querySelector(".phase-demo") ||
        document.querySelector(".superposition-demo") ||
        document.querySelector(".cnot-minus") ||
        document.querySelector(".signs-explorer") ||
        document.querySelector(".parity-explorer");
      if (rootEl) ro.observe(rootEl);
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", start);
  } else {
    start();
  }
})();