function lockedProfile() {
  const buttons = Array.from(document.getElementsByTagName('button'));
    for (const button of buttons) {
        button.addEventListener('click', toggleInformation)
    }

    function toggleInformation(e) {
        const btn = e.currentTarget;
        const parentDiv = btn.parentElement;
        const children = Array.from(parentDiv.children);
        const showMoreInfo = children[9];
        const radioUnlocked = children[4];


        if (radioUnlocked.checked){
            if (btn.textContent === 'Show more'){
                btn.textContent = 'Hide it';
                showMoreInfo.style.display = 'block';
            } else {
                btn.textContent = 'Show more';
                showMoreInfo.style.display = 'none';
            }
        }
    }
}