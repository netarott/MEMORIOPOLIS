const audio = document.querySelector('#bgm');
const button = document.querySelector('#sound');
button.addEventListener('click', async () => {
  if (audio.paused) {
    try {
      await audio.play();
      button.textContent = 'BGMを閉じる';
      button.setAttribute('aria-pressed', 'true');
    } catch (error) {
      button.textContent = 'BGMを再生できません';
      console.error(error);
    }
  } else {
    audio.pause();
    button.textContent = 'BGMをひらく';
    button.setAttribute('aria-pressed', 'false');
  }
});
