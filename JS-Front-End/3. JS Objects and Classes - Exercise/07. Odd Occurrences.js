function oddOccurrences(input) {
    wordsOdd = []
    oddWords = {}
    let words = input.toLowerCase().split(' ');

    for (const word of words) {
        oddWords[word] = 1;
    }

    while (words.length !== 0) {
        let searchedWord = words.shift();
        for (let i = 0; i <= words.length; i++) {
            if (searchedWord === words[i]) {
                oddWords[searchedWord] += 1;
                words.splice(i, 1);
                i = i -1;
            }
        }
    }

    for (const key in oddWords) {
        if (oddWords[key] % 2 !== 0) {
            wordsOdd.push(key)
        }
    }
    console.log(wordsOdd.join(' '));
}