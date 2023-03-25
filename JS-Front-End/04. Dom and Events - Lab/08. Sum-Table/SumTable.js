function sumTable() {
    const elements = Array.from(document.querySelectorAll('td:nth-child(2)'));
    elements.pop()
    const totalSum = document.getElementById('sum');
    let sum = 0;
    

    for (const el of elements) {
        sum += Number(el.textContent);    
    }

    totalSum.textContent = sum;
}