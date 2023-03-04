function addAndSubtract(numOne, NumTwo, numThree) {
  const sum = (a, b) => a + b;
  const subtract = (sums, c) => sums - c;

  return subtract(sum(numOne, NumTwo), numThree)
}
