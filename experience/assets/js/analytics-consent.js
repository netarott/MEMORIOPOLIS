(() => {
  'use strict';

  const MEASUREMENT_ID = 'G-L51VXQ23B6';
  const STORAGE_KEY = 'memoriopolis_analytics_consent';
  const GRANTED = 'granted';
  const DENIED = 'denied';
  let tagLoadingStarted = false;

  function readConsent() {
    try {
      const value = window.localStorage.getItem(STORAGE_KEY);
      return value === GRANTED || value === DENIED ? value : null;
    } catch (error) {
      console.warn('[analytics] Consent preference could not be read.', error);
      return null;
    }
  }

  function writeConsent(value) {
    try {
      window.localStorage.setItem(STORAGE_KEY, value);
    } catch (error) {
      console.warn('[analytics] Consent preference could not be saved.', error);
    }
  }

  function loadGoogleTag() {
    if (tagLoadingStarted || document.querySelector('script[data-memoriopolis-ga4]')) return;
    tagLoadingStarted = true;

    window.dataLayer = window.dataLayer || [];
    window.gtag = window.gtag || function gtag() {
      window.dataLayer.push(arguments);
    };

    window.gtag('js', new Date());
    window.gtag('config', MEASUREMENT_ID, {
      send_page_view: true,
      allow_google_signals: false,
      allow_ad_personalization_signals: false
    });

    const tag = document.createElement('script');
    tag.async = true;
    tag.src = `https://www.googletagmanager.com/gtag/js?id=${encodeURIComponent(MEASUREMENT_ID)}`;
    tag.dataset.memoriopolisGa4 = 'true';
    tag.addEventListener('load', () => {
      document.documentElement.dataset.analytics = GRANTED;
      console.info('[analytics] Google Analytics loaded after consent.');
    }, { once: true });
    tag.addEventListener('error', () => {
      tagLoadingStarted = false;
      document.documentElement.dataset.analytics = 'unavailable';
      console.warn('[analytics] Google Analytics could not be loaded.');
    }, { once: true });
    document.head.appendChild(tag);
  }

  function bannerMarkup() {
    return `
      <aside class="analytics-consent" role="region"
             aria-labelledby="analytics-consent-title"
             aria-describedby="analytics-consent-description">
        <div class="analytics-consent__inner">
          <p class="analytics-consent__eyebrow">CENTRAL STATION / OBSERVATION</p>
          <h2 id="analytics-consent-title">アクセス解析について</h2>
          <p id="analytics-consent-description">
            記憶都市では、作品の改善を目的として、閲覧ページ、利用端末、参照元などを
            Google Analyticsで統計的に観測します。許可するまでGoogleの解析タグは読み込みません。
          </p>
          <p><a href="privacy.html">詳しい説明を読む</a></p>
          <div class="analytics-consent__actions">
            <button type="button" data-analytics-consent="granted">観測を許可する</button>
            <button type="button" data-analytics-consent="denied">許可しない</button>
          </div>
        </div>
      </aside>`;
  }

  function closeBanner(banner, returnFocusTo = null) {
    banner.remove();
    if (returnFocusTo instanceof HTMLElement) returnFocusTo.focus();
  }

  function showBanner(trigger = null) {
    const existing = document.querySelector('.analytics-consent');
    if (existing) {
      existing.querySelector('button')?.focus();
      return;
    }

    document.body.insertAdjacentHTML('beforeend', bannerMarkup());
    const banner = document.querySelector('.analytics-consent');
    const buttons = banner.querySelectorAll('[data-analytics-consent]');

    buttons.forEach((button) => {
      button.addEventListener('click', () => {
        const choice = button.dataset.analyticsConsent;
        writeConsent(choice);
        document.documentElement.dataset.analytics = choice;
        closeBanner(banner, trigger);
        if (choice === GRANTED) loadGoogleTag();
      }, { once: true });
    });

  }

  function connectSettingsButtons() {
    document.querySelectorAll('[data-analytics-consent-open]').forEach((button) => {
      button.addEventListener('click', () => showBanner(button));
    });
  }

  function initialize() {
    connectSettingsButtons();
    const consent = readConsent();
    if (consent === GRANTED) {
      document.documentElement.dataset.analytics = GRANTED;
      loadGoogleTag();
    } else if (consent === DENIED) {
      document.documentElement.dataset.analytics = DENIED;
    } else {
      document.documentElement.dataset.analytics = 'unset';
      showBanner();
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initialize, { once: true });
  } else {
    initialize();
  }
})();
