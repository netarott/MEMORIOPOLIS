(() => {
  'use strict';
  const CONSENT_KEY = 'memoriopolis_analytics_consent';
  const video = document.getElementById('section11-trailer');
  let playSent = false;
  let completeSent = false;
  function analyticsReady() {
    try { return localStorage.getItem(CONSENT_KEY) === 'granted' && typeof window.gtag === 'function'; }
    catch { return false; }
  }
  function sendEvent(name, parameters) {
    if (analyticsReady()) window.gtag('event', name, parameters);
  }
  video?.addEventListener('play', () => {
    if (playSent) return;
    playSent = true;
    sendEvent('section11_trailer_play', { section_id: 'section11', trailer_id: 'section11_trailer_ja_final' });
  });
  video?.addEventListener('ended', () => {
    if (completeSent) return;
    completeSent = true;
    sendEvent('section11_trailer_complete', { section_id: 'section11', trailer_id: 'section11_trailer_ja_final' });
  });
  document.getElementById('open-emaki')?.addEventListener('click', () => {
    sendEvent('section11_trailer_open_emaki', { section_id: 'section11', source: 'trailer_page' });
  });
  document.querySelector('[data-open-production-notes]')?.addEventListener('click', () => {
    sendEvent('open_production_notes', { section_id: 'section11', source: 'trailer_page' });
  });
})();
