function calc(numOne, numTwo, operation) {
  const add = (a, b) => a + b;
  const subtract = (a, b) => a - b;
  const multiply = (a, b) => a * b;
  const divide = (a, b) => a / b;

  switch (operation) {
    case "add":
      return add(numOne, numTwo);
    case "subtract":
      return subtract(numOne, numTwo);
    case "multiply":
      return multiply(numOne, numTwo);
    case "divide":
      return divide(numOne, numTwo);
    default:
      console.log("invalid operation");
  }
}