(() => {
  'use strict';
  const DATA_URL = 'data/section09.json?v=20260822-5';
  const SUPPORTED = ['ja', 'en', 'zh-TW', 'ko', 'ru'];
  const escapeHtml = (value) => String(value).replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;').replaceAll('"', '&quot;').replaceAll("'", '&#039;');
  const inline = (value) => escapeHtml(value).replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>').replace(/`([^`\n]+)`/g, '<code>$1</code>');

  function markdownToHtml(markdown) {
    const normalized = String(markdown).replace(/\r\n?/g, '\n').trim();
    const codeBlocks = [];
    const text = normalized.replace(/```([^\n]*)\n([\s\S]*?)```/g, (_, language, code) => {
      const token = `@@CODE_BLOCK_${codeBlocks.length}@@`;
      codeBlocks.push(`<pre data-language="${escapeHtml(language.trim())}"><code>${escapeHtml(code.replace(/\n$/, ''))}</code></pre>`);
      return `\n\n${token}\n\n`;
    });
    return text.split(/\n{2,}/).map((block) => block.trim()).filter(Boolean).map((block) => {
      const match = block.match(/^@@CODE_BLOCK_(\d+)@@$/);
      if (match) return codeBlocks[Number(match[1])];
      const heading = block.match(/^(#{2,6})\s+(.+)$/s);
      if (heading && !heading[2].includes('\n')) return `<h${Math.min(heading[1].length, 4)}>${inline(heading[2])}</h${Math.min(heading[1].length, 4)}>`;
      if (block.split('\n').every((line) => /^[-*]\s+/.test(line))) return `<ul>${block.split('\n').map((line) => `<li>${inline(line.replace(/^[-*]\s+/, ''))}</li>`).join('')}</ul>`;
      return `<p>${inline(block).replaceAll('\n', '<br>')}</p>`;
    }).join('\n');
  }

  function language() { const value = new URLSearchParams(location.search).get('from'); return SUPPORTED.includes(value) ? value : 'ja'; }
  async function typeset(element) {
    if (!window.MathJax?.startup?.promise || typeof window.MathJax.typesetPromise !== 'function') return;
    try { await window.MathJax.startup.promise; await window.MathJax.typesetPromise([element]); }
    catch (error) { console.warn('[notes] MathJax skipped.', error); }
  }
  async function load() {
    const title = document.querySelector('#notes-title'); const status = document.querySelector('#notes-status'); const content = document.querySelector('#notes-content');
    try {
      const response = await fetch(DATA_URL, { cache: 'no-store' });
      if (!response.ok) throw new Error(`section09.json HTTP ${response.status}`);
      const data = await response.json(); const notes = data?.documents?.production_notes;
      if (!notes) throw new Error('production notes data is incomplete');
      const from = language(); const target = `index.html${from === 'ja' ? '' : `?lang=${encodeURIComponent(from)}`}#story-end`;
      document.querySelector('#story-return-top').href = target; document.querySelector('#story-return-bottom').href = target;
      title.textContent = notes.title; content.innerHTML = markdownToHtml(notes.content); status.textContent = `正本: ${notes.source}`;
      void typeset(content);
    } catch (error) { title.textContent = '制作ノートを読み込めませんでした'; status.textContent = `読み込みエラー: ${error.message}`; status.classList.add('error'); }
  }
  function audio() {
    const media = document.querySelector('#bgm'); const button = document.querySelector('#sound');
    button.addEventListener('click', async () => { if (media.paused) { try { await media.play(); button.textContent = 'BGMを閉じる'; } catch { button.textContent = 'BGMを再生できません'; } } else { media.pause(); button.textContent = 'BGMをひらく'; } });
  }
  const initialize = () => { audio(); void load(); };
  window.addEventListener('mathjax-ready', () => { const content = document.querySelector('#notes-content'); if (content?.children.length) void typeset(content); });
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initialize, { once: true }); else initialize();
})();
