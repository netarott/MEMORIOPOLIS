(() => {
  'use strict';

  const DATA_URL = 'data/section09.json?v=20260822-3';
  const DEFAULT_LANGUAGE = 'ja';
  const SUPPORTED_LANGUAGES = ['ja', 'en', 'zh-TW', 'ko', 'ru'];
  let sectionData = null;
  let renderSequence = 0;
  let initialized = false;

  function escapeHtml(value) {
    return String(value)
      .replaceAll('&', '&amp;')
      .replaceAll('<', '&lt;')
      .replaceAll('>', '&gt;')
      .replaceAll('"', '&quot;')
      .replaceAll("'", '&#039;');
  }

  function markdownToHtml(markdown) {
    const normalized = String(markdown).replace(/\r\n?/g, '\n').trim();
    if (!normalized) return '';

    const codeBlocks = [];
    const withoutCode = normalized.replace(/```([^\n]*)\n([\s\S]*?)```/g, (_, language, code) => {
      const token = `@@CODE_BLOCK_${codeBlocks.length}@@`;
      codeBlocks.push(
        `<pre data-language="${escapeHtml(language.trim())}"><code>${escapeHtml(code.replace(/\n$/, ''))}</code></pre>`
      );
      return `\n\n${token}\n\n`;
    });

    return withoutCode
      .split(/\n{2,}/)
      .map((block) => block.trim())
      .filter(Boolean)
      .map((block) => {
        const codeMatch = block.match(/^@@CODE_BLOCK_(\d+)@@$/);
        if (codeMatch) return codeBlocks[Number(codeMatch[1])];
        return `<p>${escapeHtml(block).replaceAll('\n', '<br>')}</p>`;
      })
      .join('\n');
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

  async function typesetContent(contentElement, sequence) {
    try {
      if (!window.MathJax?.startup?.promise) return;
      await window.MathJax.startup.promise;
      if (sequence !== renderSequence) return;
      if (typeof window.MathJax.typesetClear === 'function') {
        window.MathJax.typesetClear([contentElement]);
      }
      await window.MathJax.typesetPromise([contentElement]);
    } catch (error) {
      console.warn('[section09] MathJax typesetting was skipped.', error);
    }
  }

  async function renderLanguage(language) {
    if (!sectionData || !SUPPORTED_LANGUAGES.includes(language)) return;

    const titleElement = document.querySelector('#section-title');
    const contentElement = document.querySelector('#section-content');
    const statusElement = document.querySelector('#load-status');
    const notesLinkElement = document.querySelector('#production-notes-link');
    const languageButtons = [...document.querySelectorAll('[data-language]')];
    if (!titleElement || !contentElement || !statusElement || !notesLinkElement) {
      throw new Error('Required Section 09 DOM elements are missing.');
    }

    const sequence = ++renderSequence;
    document.documentElement.lang = language;
    titleElement.textContent = sectionData.titles[language];
    contentElement.innerHTML = markdownToHtml(sectionData.content[language]);
    statusElement.textContent = '五言語正本から生成された本文を表示しています。';
    statusElement.classList.remove('error');

    languageButtons.forEach((button) => {
      button.setAttribute('aria-pressed', String(button.dataset.language === language));
    });

    const notesTarget = sectionData.links.production_notes || 'notes.html';
    notesLinkElement.href = `${notesTarget}?from=${encodeURIComponent(language)}`;
    updateUrl(language);
    await typesetContent(contentElement, sequence);
  }

  async function loadSection() {
    const titleElement = document.querySelector('#section-title');
    const statusElement = document.querySelector('#load-status');
    const buildStateElement = document.querySelector('#build-state');

    try {
      console.info('[section09] Loading generated section data.');
      const response = await fetch(DATA_URL, { cache: 'no-store' });
      console.info(`[section09] Data response: ${response.status}`);
      if (!response.ok) throw new Error(`section09.json HTTP ${response.status}`);

      const data = await response.json();
      const complete = data?.metadata && data?.titles && data?.content && data?.documents && data?.links;
      const fiveLanguages = SUPPORTED_LANGUAGES.every(
        (language) => typeof data.titles[language] === 'string' && typeof data.content[language] === 'string'
      );
      if (!complete || !fiveLanguages) {
        throw new Error('section09.json structure is incomplete');
      }

      sectionData = data;
      if (buildStateElement) buildStateElement.hidden = !data.metadata.localization_ready;
      await renderLanguage(languageFromUrl());
      console.info('[section09] Initial rendering completed.');
    } catch (error) {
      if (titleElement) titleElement.textContent = '本文を読み込めませんでした';
      if (statusElement) {
        statusElement.textContent = `読み込みエラー: ${error.message}`;
        statusElement.classList.add('error');
      }
      console.error('[section09] Initial rendering failed.', error);
    }
  }

  function connectControls() {
    const audio = document.querySelector('#bgm');
    const soundButton = document.querySelector('#sound');
    document.querySelectorAll('[data-language]').forEach((button) => {
      button.addEventListener('click', () => void renderLanguage(button.dataset.language));
    });

    if (audio && soundButton) {
      soundButton.addEventListener('click', async () => {
        if (audio.paused) {
          try {
            await audio.play();
            soundButton.textContent = 'BGMを閉じる';
            soundButton.setAttribute('aria-pressed', 'true');
          } catch (error) {
            soundButton.textContent = 'BGMを再生できません';
            console.error('[section09] Audio playback failed.', error);
          }
        } else {
          audio.pause();
          soundButton.textContent = 'BGMをひらく';
          soundButton.setAttribute('aria-pressed', 'false');
        }
      });
    }
  }

  function initialize() {
    if (initialized) return;
    initialized = true;
    console.info('[section09] script.js v20260822-3 initialized.');
    connectControls();
    void loadSection();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initialize, { once: true });
  } else {
    initialize();
  }

  window.addEventListener('pageshow', () => {
    if (!sectionData) void loadSection();
  });
})();
