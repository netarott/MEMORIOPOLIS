(() => {
  'use strict';
  const DATA_URL = 'data/section09.json?v=20260822-5';
  const DEFAULT_LANGUAGE = 'ja';
  const SUPPORTED_LANGUAGES = ['ja', 'en', 'zh-TW', 'ko', 'ru'];
  let sectionData = null;
  let renderSequence = 0;
  let initialized = false;
  let pendingTypeset = null;

  const escapeHtml = (value) => String(value).replaceAll('&', '&amp;').replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;').replaceAll('"', '&quot;').replaceAll("'", '&#039;');

  function isDeltaDisplayBlock(block) {
    return block.startsWith('$$') && block.endsWith('$$') &&
      /\\delta\s*=\s*t_\{\\mathrm\{external\}\}\s*-\s*t_\{\\mathrm\{internal\}\}/.test(block);
  }

  function observationEntryHtml() {
    return '<div id="delta" class="observation-entry">' +
      '<p class="deep-link-kicker">STATE MODEL BELOW</p>' +
      '<p>二つの時計の始点の差を、状態模型から観測する。</p>' +
      '<a id="python-observation-link" class="deep-link-button" href="observation.html">Python観測窓をひらく</a>' +
      '</div>';
  }

  function markdownToHtml(markdown) {
    const normalized = String(markdown).replace(/\r\n?/g, '\n').trim();
    if (!normalized) return '';
    const codeBlocks = [];
    const withoutCode = normalized.replace(/```([^\n]*)\n([\s\S]*?)```/g, (_, language, code) => {
      const token = `@@CODE_BLOCK_${codeBlocks.length}@@`;
      codeBlocks.push(`<pre data-language="${escapeHtml(language.trim())}"><code>${escapeHtml(code.replace(/\n$/, ''))}</code></pre>`);
      return `\n\n${token}\n\n`;
    });
    let deltaEntryAdded = false;
    return withoutCode.split(/\n{2,}/).map((block) => block.trim()).filter(Boolean).map((block) => {
      const codeMatch = block.match(/^@@CODE_BLOCK_(\d+)@@$/);
      if (codeMatch) return codeBlocks[Number(codeMatch[1])];
      const paragraph = `<p>${escapeHtml(block).replaceAll('\n', '<br>')}</p>`;
      if (!deltaEntryAdded && isDeltaDisplayBlock(block)) {
        deltaEntryAdded = true;
        return paragraph + observationEntryHtml();
      }
      return paragraph;
    }).join('\n');
  }

  function languageFromUrl() {
    const requested = new URLSearchParams(window.location.search).get('lang');
    return SUPPORTED_LANGUAGES.includes(requested) ? requested : DEFAULT_LANGUAGE;
  }

  function updateUrl(language) {
    const url = new URL(window.location.href);
    if (language === DEFAULT_LANGUAGE) url.searchParams.delete('lang');
    else url.searchParams.set('lang', language);
    window.history.replaceState({}, '', url);
  }

  function scrollToRequestedAnchor() {
    if (window.location.hash === '#delta') {
      window.requestAnimationFrame(() => document.querySelector('#delta')?.scrollIntoView({ block: 'center' }));
    }
  }

  async function runTypeset(element, sequence) {
    if (!window.MathJax?.startup?.promise || typeof window.MathJax.typesetPromise !== 'function') return false;
    try {
      await window.MathJax.startup.promise;
      if (sequence !== renderSequence) return true;
      if (typeof window.MathJax.typesetClear === 'function') window.MathJax.typesetClear([element]);
      await window.MathJax.typesetPromise([element]);
      scrollToRequestedAnchor();
      return true;
    } catch (error) {
      console.warn('[section09] MathJax typesetting was skipped.', error);
      return false;
    }
  }

  function requestTypeset(element, sequence) {
    pendingTypeset = { element, sequence };
    void runTypeset(element, sequence).then((completed) => {
      if (completed && pendingTypeset?.sequence === sequence) pendingTypeset = null;
    });
  }

  async function renderLanguage(language) {
    if (!sectionData || !SUPPORTED_LANGUAGES.includes(language)) return;
    const title = document.querySelector('#section-title');
    const content = document.querySelector('#section-content');
    const status = document.querySelector('#load-status');
    const notesLink = document.querySelector('#production-notes-link');
    if (!title || !content || !status || !notesLink) throw new Error('Required Section 09 DOM elements are missing.');

    const sequence = ++renderSequence;
    document.documentElement.lang = language;
    title.textContent = sectionData.titles[language];
    content.innerHTML = markdownToHtml(sectionData.content[language]);
    status.textContent = '五言語正本から生成された本文を表示しています。';
    status.classList.remove('error');
    document.querySelectorAll('[data-language]').forEach((button) =>
      button.setAttribute('aria-pressed', String(button.dataset.language === language))
    );
    notesLink.href = `${sectionData.links.production_notes || 'notes.html'}?from=${encodeURIComponent(language)}`;
    const observationLink = document.querySelector('#python-observation-link');
    if (observationLink) observationLink.href = `${sectionData.links.python_model || 'observation.html'}?from=${encodeURIComponent(language)}`;
    updateUrl(language);
    scrollToRequestedAnchor();
    requestTypeset(content, sequence);
  }

  async function loadSection() {
    const title = document.querySelector('#section-title');
    const status = document.querySelector('#load-status');
    try {
      const response = await fetch(DATA_URL, { cache: 'no-store' });
      if (!response.ok) throw new Error(`section09.json HTTP ${response.status}`);
      const data = await response.json();
      const complete = data?.metadata && data?.titles && data?.content && data?.documents?.production_notes && data?.documents?.python_model && data?.links;
      const five = SUPPORTED_LANGUAGES.every((language) => typeof data.titles[language] === 'string' && typeof data.content[language] === 'string');
      if (!complete || !five) throw new Error('section09.json structure is incomplete');
      sectionData = data;
      const state = document.querySelector('#build-state');
      if (state) state.hidden = !data.metadata.localization_ready;
      await renderLanguage(languageFromUrl());
    } catch (error) {
      if (title) title.textContent = '本文を読み込めませんでした';
      if (status) { status.textContent = `読み込みエラー: ${error.message}`; status.classList.add('error'); }
      console.error('[section09] Initial rendering failed.', error);
    }
  }

  function connectAudio() {
    const audio = document.querySelector('#bgm');
    const button = document.querySelector('#sound');
    if (!audio || !button) return;
    button.addEventListener('click', async () => {
      if (audio.paused) {
        try { await audio.play(); button.textContent = 'BGMを閉じる'; button.setAttribute('aria-pressed', 'true'); }
        catch (error) { button.textContent = 'BGMを再生できません'; console.error(error); }
      } else {
        audio.pause(); button.textContent = 'BGMをひらく'; button.setAttribute('aria-pressed', 'false');
      }
    });
  }

  function initialize() {
    if (initialized) return;
    initialized = true;
    document.querySelectorAll('[data-language]').forEach((button) =>
      button.addEventListener('click', () => void renderLanguage(button.dataset.language))
    );
    connectAudio();
    void loadSection();
  }

  window.addEventListener('mathjax-ready', () => {
    if (pendingTypeset) void runTypeset(pendingTypeset.element, pendingTypeset.sequence);
  });
  window.addEventListener('mathjax-failed', () => console.warn('[section09] MathJax CDN failed; text remains available.'));
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initialize, { once: true });
  else initialize();
  window.addEventListener('pageshow', () => { if (!sectionData) void loadSection(); });
})();
