(() => {
  'use strict';
  const DATA_URL = 'data/section09.json?v=20260822-5';
  const SUPPORTED = ['ja', 'en', 'zh-TW', 'ko', 'ru'];
  function language() { const value = new URLSearchParams(location.search).get('from'); return SUPPORTED.includes(value) ? value : 'ja'; }
  function storyTarget(value) { return `index.html${value === 'ja' ? '' : `?lang=${encodeURIComponent(value)}`}#delta`; }
  async function typeset() {
    if (!window.MathJax?.startup?.promise || typeof window.MathJax.typesetPromise !== 'function') return;
    try { await window.MathJax.startup.promise; const math = document.querySelector('#observation-math'); if (math) await window.MathJax.typesetPromise([math]); }
    catch (error) { console.warn('[observation] MathJax skipped.', error); }
  }
  async function load() {
    const title = document.querySelector('#model-title'); const status = document.querySelector('#model-status');
    try {
      const response = await fetch(DATA_URL, { cache: 'no-store' }); if (!response.ok) throw new Error(`section09.json HTTP ${response.status}`);
      const model = (await response.json())?.documents?.python_model; if (!model?.content) throw new Error('Python model data is incomplete');
      title.textContent = model.title; status.textContent = 'Python正本を表示しています。'; document.querySelector('#model-source').textContent = `正本: ${model.source}`; document.querySelector('#python-content').textContent = model.content;
    } catch (error) { title.textContent = 'Python模型を読み込めませんでした'; status.textContent = `読み込みエラー: ${error.message}`; status.classList.add('error'); }
  }
  function navigation() {
    const from = language(); const target = storyTarget(from);
    document.querySelector('#story-return').href = target; document.querySelector('#story-return-bottom').href = target; document.querySelector('#notes-cross-link').href = `notes.html?from=${encodeURIComponent(from)}`;
  }
  function audio() {
    const media = document.querySelector('#bgm'); const button = document.querySelector('#sound');
    button.addEventListener('click', async () => { if (media.paused) { try { await media.play(); button.textContent = 'BGMを閉じる'; } catch { button.textContent = 'BGMを再生できません'; } } else { media.pause(); button.textContent = 'BGMをひらく'; } });
  }
  const initialize = () => { navigation(); audio(); void load(); void typeset(); };
  window.addEventListener('mathjax-ready', () => void typeset());
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initialize, { once: true }); else initialize();
})();
