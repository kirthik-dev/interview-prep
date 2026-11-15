'use strict';
(() => {
  const cards = [...document.querySelectorAll('.qa')];
  const chapters = [...document.querySelectorAll('.chapter')].filter(s => s.querySelector('.qa'));
  const search = document.querySelector('#search');
  const status = document.querySelector('#results');
  const clear = document.querySelector('#clear-search');
  const empty = document.querySelector('#no-results');
  const corpus = new Map(cards.map(card => [card, (card.closest('.chapter').querySelector('.chapter-heading').textContent + ' ' + card.textContent).toLowerCase()]));
  let searchSnapshot = null;
  let printSnapshot = null;
  let toastTimer;
  function toast(message) {
    const el = document.querySelector('#toast');
    el.textContent = message;
    el.classList.add('show');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => el.classList.remove('show'), 2600);
  }
  function filter() {
    const query = search.value.trim().toLowerCase();
    const terms = query.split(/\s+/).filter(Boolean);
    if (query && !searchSnapshot) searchSnapshot = cards.map(c => c.open);
    let count = 0;
    for (const card of cards) {
      const match = terms.every(term => corpus.get(card).includes(term));
      card.hidden = !match;
      if (query && match) card.open = true;
      if (match) count++;
    }
    if (!query && searchSnapshot) {
      cards.forEach((c, i) => { c.open = searchSnapshot[i]; });
      searchSnapshot = null;
    }
    chapters.forEach(s => { s.hidden = ![...s.querySelectorAll('.qa')].some(c => !c.hidden); });
    empty.hidden = count > 0;
    clear.hidden = !query;
    status.textContent = query ? `${count} matching question${count === 1 ? '' : 's'} · all search words must match` : `${cards.length} questions · choose a chapter or search`;
  }
  search.addEventListener('input', filter);
  clear.addEventListener('click', () => { search.value = ''; filter(); search.focus(); });
  document.querySelector('#expand').addEventListener('click', () => { cards.filter(c => !c.hidden).forEach(c => { c.open = true; }); });
  document.querySelector('#collapse').addEventListener('click', () => { cards.filter(c => !c.hidden).forEach(c => { c.open = false; }); });
  async function copyText(text) {
    if (navigator.clipboard && window.isSecureContext) {
      try { await navigator.clipboard.writeText(text); return true; } catch (_) { /* fallback */ }
    }
    const area = document.createElement('textarea');
    area.value = text;
    area.setAttribute('aria-label', 'Code to copy');
    area.style.cssText = 'position:fixed;top:0;left:-9999px';
    document.body.append(area);
    area.select();
    let ok = false;
    try { ok = document.execCommand('copy'); } catch (_) { /* manual copy */ }
    area.remove();
    return ok;
  }
  document.querySelectorAll('[data-copy]').forEach(button => {
    button.addEventListener('click', async () => {
      const text = document.getElementById(button.dataset.copy).textContent;
      const ok = await copyText(text);
      toast(ok ? 'Code copied.' : 'Copy unavailable. Select the code and copy it manually.');
      button.focus();
    });
  });
  function openHash() {
    let id;
    try { id = decodeURIComponent(location.hash.slice(1)); } catch (_) { return; }
    const target = document.getElementById(id);
    if (!target) return;
    if (target.matches('.qa')) {
      if (search.value) { search.value = ''; filter(); }
      target.open = true;
      requestAnimationFrame(() => target.scrollIntoView({block:'start'}));
    } else if (target.matches('.chapter') && search.value) {
      search.value = ''; filter();
      requestAnimationFrame(() => target.scrollIntoView({block:'start'}));
    }
  }
  window.addEventListener('hashchange', openHash);
  openHash();
  window.addEventListener('beforeprint', () => {
    if (printSnapshot) return;
    printSnapshot = {cards: cards.map(c => ({open:c.open, hidden:c.hidden})), chapters:chapters.map(c => c.hidden)};
    cards.forEach(c => { c.hidden = false; c.open = true; });
    chapters.forEach(c => { c.hidden = false; });
  });
  window.addEventListener('afterprint', () => {
    if (!printSnapshot) return;
    cards.forEach((c,i) => Object.assign(c, printSnapshot.cards[i]));
    chapters.forEach((c,i) => { c.hidden = printSnapshot.chapters[i]; });
    printSnapshot = null;
  });
  document.querySelector('#print').addEventListener('click', () => window.print());
  if ('IntersectionObserver' in window) {
    const links = [...document.querySelectorAll('nav a')];
    const observer = new IntersectionObserver(entries => {
      for (const entry of entries) {
        if (!entry.isIntersecting) continue;
        links.forEach(link => {
          const active = link.hash === '#' + entry.target.id;
          link.classList.toggle('active', active);
          if (active) link.setAttribute('aria-current', 'location'); else link.removeAttribute('aria-current');
        });
      }
    }, {rootMargin:'-100px 0px -60% 0px', threshold:0});
    document.querySelectorAll('.chapter').forEach(s => observer.observe(s));
  }
})();
