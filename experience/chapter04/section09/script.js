const DATA_URL = 'data/section09.json';
const DEFAULT_LANGUAGE = 'ja';
const SUPPORTED_LANGUAGES = ['ja', 'en', 'zh-TW', 'ko', 'ru'];

const audio = document.querySelector('#bgm');
const soundButton = document.querySelector('#sound');
const titleElement = document.querySelector('#section-title');
const contentElement = document.querySelector('#section-content');
const statusElement = document.querySelector('#load-status');
const buildStateElement = document.querySelector('#build-state');
const languageButtons = [...document.querySelectorAll('[data-language]')];

let sectionData = null;
let renderSequence = 0;

function escapeHtml(value) {
  return value
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;')
    .replaceAll("'", '&#039;');
}

function markdownToHtml(markdown) {
  const normalized = markdown.replace(/\r\n?/g, '\n').trim();
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

      // Escape prose as HTML while preserving TeX delimiters and commands.
      // MathJax processes $...$ and $$...$$ after the HTML is inserted.
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

async function typesetContent(sequence) {
  if (!window.MathJax?.startup?.promise) {
    throw new Error('MathJax failed to load');
  }

  await window.MathJax.startup.promise;
  if (sequence !== renderSequence) return;

  window.MathJax.typesetClear([contentElement]);
  await window.MathJax.typesetPromise([contentElement]);
}

async function renderLanguage(language) {
  if (!sectionData || !SUPPORTED_LANGUAGES.includes(language)) return;

  const sequence = ++renderSequence;
  document.documentElement.lang = language;
  titleElement.textContent = sectionData.titles[language];
  contentElement.innerHTML = markdownToHtml(sectionData.content[language]);
  statusElement.textContent = '五言語正本から生成された本文を表示しています。';
  statusElement.classList.remove('error');

  languageButtons.forEach((button) => {
    const selected = button.dataset.language === language;
    button.setAttribute('aria-pressed', String(selected));
  });

  updateUrl(language);

  try {
    await typesetContent(sequence);
  } catch (error) {
    if (sequence !== renderSequence) return;
    statusElement.textContent = '本文は表示されていますが、数式組版を読み込めませんでした。';
    statusElement.classList.add('error');
    console.error(error);
  }
}

async function loadSection() {
  try {
    const response = await fetch(DATA_URL, { cache: 'no-store' });
    if (!response.ok) throw new Error(`HTTP ${response.status}`);

    const data = await response.json();
    const hasRequiredData = data?.metadata && data?.titles && data?.content && data?.links;
    const hasFiveLanguages = SUPPORTED_LANGUAGES.every(
      (language) => typeof data.titles[language] === 'string' && typeof data.content[language] === 'string'
    );
    if (!hasRequiredData || !hasFiveLanguages) {
      throw new Error('section09.json structure is incomplete');
    }

    sectionData = data;
    buildStateElement.hidden = !data.metadata.localization_ready;
    await renderLanguage(languageFromUrl());
  } catch (error) {
    titleElement.textContent = '本文を読み込めませんでした';
    statusElement.textContent = 'data/section09.json、ローカルサーバー、MathJaxの接続を確認してください。';
    statusElement.classList.add('error');
    console.error(error);
  }
}

languageButtons.forEach((button) => {
  button.addEventListener('click', () => {
    void renderLanguage(button.dataset.language);
  });
});

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

void loadSection();
