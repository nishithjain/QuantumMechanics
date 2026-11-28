/** Fit parent iframe height to full document (Markdown preview, same-origin). */
(() => {
  if (window.self === window.top) return;
  document.documentElement.classList.add('qm-embed');

  const PAD = 16;
  const WIDE = 620;
  let t = null;

  function getFrame() {
    if (window.frameElement) return window.frameElement;
    try {
      const parent = window.parent;
      if (!parent || parent === window) return null;
      for (const f of parent.document.getElementsByTagName('iframe')) {
        if (f.contentWindow === window) return f;
      }
    } catch (_) { /* cross-origin */ }
    return null;
  }

  function contentRoot() {
    return document.querySelector('main') || document.querySelector('.container');
  }

  function measureHeight() {
    const root = contentRoot();
    if (root) {
      const bodyRect = document.body.getBoundingClientRect();
      const rootRect = root.getBoundingClientRect();
      let bottom = rootRect.bottom - bodyRect.top;
      const scrollBottom = root.offsetTop + root.scrollHeight;
      bottom = Math.max(bottom, scrollBottom);
      document.querySelectorAll('body > :not(script):not(link)').forEach(el => {
        const r = el.getBoundingClientRect();
        if (r.height > 0) bottom = Math.max(bottom, r.bottom - bodyRect.top);
      });
      bottom += parseFloat(getComputedStyle(document.body).paddingBottom) || 0;
      return Math.ceil(bottom) + PAD;
    }
    return Math.ceil(
      Math.max(
        document.documentElement.scrollHeight,
        document.body.scrollHeight,
        document.documentElement.offsetHeight
      )
    ) + PAD;
  }

  function fit() {
    const fe = getFrame();
    const w = document.documentElement.clientWidth;
    document.documentElement.classList.toggle('qm-embed-wide', w >= WIDE);

    if (fe) {
      fe.style.height = '4000px';
      fe.style.overflow = 'hidden';
      fe.setAttribute('scrolling', 'no');
    }

    const h = measureHeight();

    if (fe) {
      fe.style.height = h + 'px';
    }
    try {
      window.parent.postMessage({ type: 'qm-embed-height', height: h }, '*');
    } catch (_) { /* blocked */ }
  }

  const schedule = () => {
    if (t) cancelAnimationFrame(t);
    t = requestAnimationFrame(fit);
  };

  window.qmEmbedNotify = schedule;

  function start() {
    schedule();
    window.addEventListener('load', () => {
      schedule();
      [80, 200, 500, 1200, 2500, 4000].forEach(ms => setTimeout(schedule, ms));
    });
    window.addEventListener('resize', schedule);
    if (typeof ResizeObserver !== 'undefined') {
      const ro = new ResizeObserver(schedule);
      ro.observe(document.body);
      const root = contentRoot();
      if (root) {
        ro.observe(root);
        root.querySelectorAll('section, .panel, .card, svg').forEach((el) => ro.observe(el));
      }
    }
    document.addEventListener('click', e => {
      if (e.target.closest('button')) {
        setTimeout(schedule, 80);
        setTimeout(schedule, 300);
      }
    });
    document.addEventListener('input', e => {
      if (e.target.matches('input[type=range], input[type=number]')) schedule();
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', start);
  } else {
    start();
  }
})();