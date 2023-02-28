function reveal(words, template) {
  let arrWords = template.split(" ");
  let newArr = words.split(", ");

  for (let word of newArr) {
    for (const el of arrWords) {
      if (el.includes("*") && el.length === word.length) {
        template = template.replace(el, word);
      }
    }
  }
  console.log(template);
}
