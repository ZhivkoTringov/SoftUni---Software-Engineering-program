function extractText() {
    let first = document.querySelectorAll('ul#items li');
    let textArea = document.getElementById('result');
    for (let data of first) {
        textArea.value += data.textContent + '\n';
    }
}