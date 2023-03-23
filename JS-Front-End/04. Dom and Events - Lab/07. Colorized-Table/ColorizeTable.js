function colorize() {
  let oddTds = Array.from(document.querySelectorAll("tr:nth-of-type(2n)"));
  oddTds.forEach((td) => td.style.backgroundColor = 'teal');

}
