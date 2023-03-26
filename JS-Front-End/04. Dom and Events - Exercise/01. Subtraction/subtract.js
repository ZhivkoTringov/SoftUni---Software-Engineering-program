function subtract() {
    const firstNum = Number(document.getElementById('firstNumber').value);
    const secondNum = Number(document. getElementById('secondNumber').value);
    let subtract = firstNum - secondNum;
    const result = document.getElementById('result');
    result.textContent = subtract;
}