function focused() {
    const data = Array.from(document.getElementsByTagName('input'));

    for (const input of data) {
        input.addEventListener('focus', focusHandler);
        input.addEventListener('blur', blurHandler)
    }

    function focusHandler(event){
        let currentInput = event.target;
        let div = currentInput.parentElement;
        div.classList.add('focused');
    }

    function blurHandler(event) {
        let currentInput = event.target;
        let div = currentInput.parentElement;

        if (div.classList.contains('focused')){
            div.classList.remove('focused')
        }

    }
}