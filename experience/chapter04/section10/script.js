(() => {
  'use strict';

  const VALID_LANGUAGES = ['ja', 'en', 'zh-TW', 'ko', 'ru'];
  const CONSENT_KEY = 'memoriopolis_analytics_consent';
  let currentLanguage = 'ja';
  let trailerPlaySent = false;

  function analyticsReady() {
    try {
      return localStorage.getItem(CONSENT_KEY) === 'granted' && typeof window.gtag === 'function';
    } catch (error) {
      return false;
    }
  }

  function sendEvent(name, parameters) {
    if (!analyticsReady()) return;
    window.gtag('event', name, parameters);
  }

  function languageFromHash() {
    const value = decodeURIComponent(location.hash.replace(/^#/, ''));
    return VALID_LANGUAGES.includes(value) ? value : 'ja';
  }

  function showLanguage(language, userInitiated = false) {
    if (!VALID_LANGUAGES.includes(language)) return;
    const previous = currentLanguage;
    document.querySelectorAll('[data-language]').forEach((article) => {
      article.hidden = article.dataset.language !== language;
    });
    document.querySelectorAll('[data-language-button]').forEach((button) => {
      button.setAttribute('aria-pressed', String(button.dataset.languageButton === language));
    });
    document.documentElement.lang = language;
    currentLanguage = language;

    if (location.hash !== `#${language}`) history.replaceState(null, '', `#${language}`);
    if (userInitiated && previous !== language) {
      sendEvent('language_switch', {
        section_id: 'section10',
        from_language: previous,
        to_language: language
      });
      document.getElementById('story-start')?.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  }

  function initializeLanguageSwitcher() {
    if (!document.querySelector('[data-language-button]')) return;
    currentLanguage = languageFromHash();
    showLanguage(currentLanguage, false);
    document.querySelectorAll('[data-language-button]').forEach((button) => {
      button.addEventListener('click', () => showLanguage(button.dataset.languageButton, true));
    });
    window.addEventListener('hashchange', () => showLanguage(languageFromHash(), false));
  }

  function initializeNotesLinks() {
    document.querySelectorAll('[data-open-production-notes]').forEach((link) => {
      link.addEventListener('click', () => {
        sendEvent('open_production_notes', {
          section_id: 'section10',
          source: link.dataset.source || 'unknown'
        });
      });
    });
  }

  function initializeTrailer() {
    const video = document.getElementById('section10-trailer');
    if (!video) return;
    video.addEventListener('play', () => {
      if (trailerPlaySent) return;
      trailerPlaySent = true;
      sendEvent('trailer_play', {
        section_id: 'section10',
        trailer_id: 'section10_trailer_final'
      });
    });
  }

  function initialize() {
    initializeLanguageSwitcher();
    initializeNotesLinks();
    initializeTrailer();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initialize, { once: true });
  } else {
    initialize();
  }
})();
