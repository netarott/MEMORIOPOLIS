const DATA_URL = 'data/section09.json';
const SUPPORTED_LANGUAGES = ['ja', 'en', 'zh-TW', 'ko', 'ru'];
const audio = document.querySelector('#bgm');
const soundButton = document.querySelector('#sound');
const titleElement = document.querySelector('#notes-title');
const contentElement = document.querySelector('#notes-content');
const statusElement = document.querySelector('#notes-status');
const returnLinks = [document.querySelector('#story-return-top'), document.querySelector('#story-return-bottom')];

function escapeHtml(value) {
  return value.replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;').replaceAll("'", '&#039;');
}

function inlineMarkdown(value) {
  return escapeHtml(value)
    .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
    .replace(/`([^`\n]+)`/g, '<code>$1</code>');
}

function markdownToHtml(markdown) {
  const normalized = markdown.replace(/\r\n?/g, '\n').trim();
  if (!normalized) return '';
  const codeBlocks = [];
  const withoutCode = normalized.replace(/```([^\n]*)\n([\s\S]*?)```/g, (_, language, code) => {
    const token = `@@CODE_BLOCK_${codeBlocks.length}@@`;
    codeBlocks.push(`<pre data-language="${escapeHtml(language.trim())}"><code>${escapeHtml(code.replace(/\n$/, ''))}</code></pre>`);
    return `\n\n${token}\n\n`;
  });

  return withoutCode.split(/\n{2,}/).map((block) => block.trim()).filter(Boolean).map((block) => {
    const codeMatch = block.match(/^@@CODE_BLOCK_(\d+)@@$/);
    if (codeMatch) return codeBlocks[Number(codeMatch[1])];
    const heading = block.match(/^(#{2,6})\s+(.+)$/s);
    if (heading && !heading[2].includes('\n')) {
      const level = Math.min(heading[1].length, 4);
      return `<h${level}>${inlineMarkdown(heading[2])}</h${level}>`;
    }
    if (block.split('\n').every((line) => /^[-*]\s+/.test(line))) {
      return `<ul>${block.split('\n').map((line) => `<li>${inlineMarkdown(line.replace(/^[-*]\s+/, ''))}</li>`).join('')}</ul>`;
    }
    if (block.split('\n').every((line) => /^>\s?/.test(line))) {
      return `<blockquote>${block.split('\n').map((line) => inlineMarkdown(line.replace(/^>\s?/, ''))).join('<br>')}</blockquote>`;
    }
    return `<p>${inlineMarkdown(block).replaceAll('\n', '<br>')}</p>`;
  }).join('\n');
}

function sourceLanguage() {
  const value = new URLSearchParams(window.location.search).get('from');
  return SUPPORTED_LANGUAGES.includes(value) ? value : 'ja';
}

async function loadNotes() {
  try {
    const response = await fetch(DATA_URL, { cache: 'no-store' });
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    const data = await response.json();
    const notes = data?.documents?.production_notes;
    if (!notes || typeof notes.title !== 'string' || typeof notes.content !== 'string') {
      throw new Error('production notes data is incomplete');
    }

    const language = sourceLanguage();
    const returnTarget = `index.html${language === 'ja' ? '' : `?lang=${encodeURIComponent(language)}`}#story-end`;
    returnLinks.forEach((link) => { link.href = returnTarget; });
    titleElement.textContent = notes.title;
    contentElement.innerHTML = markdownToHtml(notes.content);
    statusElement.textContent = `正本: ${notes.source}`;

    if (!window.MathJax?.startup?.promise) throw new Error('MathJax failed to load');
    await window.MathJax.startup.promise;
    window.MathJax.typesetClear([contentElement]);
    await window.MathJax.typesetPromise([contentElement]);
  } catch (error) {
    titleElement.textContent = '制作ノートを読み込めませんでした';
    statusElement.textContent = 'section09.jsonを再Buildし、ローカルサーバーを確認してください。';
    statusElement.classList.add('error');
    console.error(error);
  }
}

soundButton.addEventListener('click', async () => {
  if (audio.paused) {
    try {
      await audio.play();
      soundButton.textContent = 'BGMを閉じる';
      soundButton.setAttribute('aria-pressed', 'true');
    } catch (error) {
      soundButton.textContent = 'BGMを再生できません';
      console.error(error);
    }
  } else {
    audio.pause();
    soundButton.textContent = 'BGMをひらく';
    soundButton.setAttribute('aria-pressed', 'false');
  }
});
void loadNotes();
