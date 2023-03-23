function deleteByEmail() {
    let result = document.getElementById('result');
    let input = document.querySelector('input[name="email"]');
    let evenTds = Array.from(document.querySelectorAll('td:nth-child(even)'));
    let email = input.value;
    let foundEl = evenTds.find((td) => td.textContent === email);
    if (foundEl) {
        foundEl.parentElement.remove();
        result.textContent = 'Deleted.'
    } else {
        result.textContent = 'Not found.'
    }
}