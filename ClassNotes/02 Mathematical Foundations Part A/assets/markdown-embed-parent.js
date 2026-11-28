/** Resize .demo-frame iframes in Markdown preview (same-origin child documents). */
(() => {
  const PAD = 12;
  const MIN_H = 180;
  const INFLATE = 5000;

  function measureDoc(doc) {
    const body = doc.body;
    if (!body) return null;
    const root = doc.querySelector('main') || doc.querySelector('.container');
    if (root) {
      const bodyRect = body.getBoundingClientRect();
      const rootRect = root.getBoundingClientRect();
      let bottom = rootRect.bottom - bodyRect.top;
      bottom = Math.max(bottom, root.offsetTop + root.scrollHeight);
      body.querySelectorAll(':scope > :not(script):not(link)').forEach((el) => {
        const r = el.getBoundingClientRect();
        if (r.height > 0) bottom = Math.max(bottom, r.bottom - bodyRect.top);
      });
      bottom += parseFloat(getComputedStyle(body).paddingBottom) || 0;
      return Math.ceil(bottom) + PAD;
    }
    const html = doc.documentElement;
    return (
      Math.ceil(
        Math.max(html.scrollHeight, body.scrollHeight, html.offsetHeight, body.offsetHeight)
      ) + PAD
    );
  }

  function measureIframe(iframe) {
    try {
      const doc = iframe.contentDocument;
      if (!doc) return null;
      const saved = iframe.style.height;
      iframe.style.height = INFLATE + 'px';
      const h = measureDoc(doc);
      if (!h) iframe.style.height = saved;
      return h;
    } catch (_) {
      return null;
    }
  }

  function setHeight(iframe, h) {
    const px = Math.max(MIN_H, Math.ceil(h));
    iframe.style.height = px + 'px';
    iframe.setAttribute('height', String(px));
  }

  function fitIframe(iframe) {
    const h = measureIframe(iframe);
    if (h) setHeight(iframe, h);
  }

  function scheduleFits(iframe) {
    fitIframe(iframe);
    [40, 120, 350, 800, 1500, 2500, 4000, 6000].forEach((ms) => setTimeout(() => fitIframe(iframe), ms));
  }

  function attach(iframe) {
    if (iframe.dataset.qmEmbedParent === '1') return;
    iframe.dataset.qmEmbedParent = '1';
    iframe.setAttribute('scrolling', 'no');

    const onReady = () => scheduleFits(iframe);
    if (iframe.contentDocument && iframe.contentDocument.readyState === 'complete') {
      onReady();
    } else {
      iframe.addEventListener('load', onReady, { once: true });
    }
  }

  function init() {
    document.querySelectorAll('.demo-frame iframe').forEach(attach);
  }

  window.addEventListener('message', (e) => {
    const d = e.data;
    if (!d || d.type !== 'qm-embed-height' || typeof d.height !== 'number') return;
    document.querySelectorAll('.demo-frame iframe').forEach((iframe) => {
      if (iframe.contentWindow === e.source) setHeight(iframe, d.height);
    });
  });

  let resizeT = null;
  window.addEventListener('resize', () => {
    if (resizeT) cancelAnimationFrame(resizeT);
    resizeT = requestAnimationFrame(() => {
      document.querySelectorAll('.demo-frame iframe').forEach(fitIframe);
    });
  });

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();