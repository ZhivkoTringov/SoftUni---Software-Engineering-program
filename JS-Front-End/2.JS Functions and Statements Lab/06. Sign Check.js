function signCheck(numOne, numTwo, numThree) {
  let arr = [numOne, numTwo, numThree];
  let counter = 0;
  for (const num of arr) {
    if (num < 0) {
      counter++;
    }
  }
  if (counter % 2 === 0) {
    return "Positive";
  } else {
    return "Negative";
  }
}
