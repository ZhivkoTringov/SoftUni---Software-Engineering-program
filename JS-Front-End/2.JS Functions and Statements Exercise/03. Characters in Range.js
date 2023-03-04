function charInRange(firstChar, secondChar) {
  let first = firstChar.charCodeAt(0);
  let second = secondChar.charCodeAt(0);
  let arr = [];
  if (first > second) {
    [first, second] = [second, first];
  }
  for (let i = first + 1; i < second; i++) {
    arr.push(String.fromCharCode(i));
  }

  return arr.join(" ");
}
