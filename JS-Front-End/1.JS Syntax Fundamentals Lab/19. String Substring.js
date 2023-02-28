function subString(word, text) {
    let wordLowerCase = word.toLowerCase();
    let arrText = text.split(' ');

    for (const text of arrText) {
        if (text.toLowerCase() === wordLowerCase) {
            return (word)
        }
    }
    return `${word} not found!`
}