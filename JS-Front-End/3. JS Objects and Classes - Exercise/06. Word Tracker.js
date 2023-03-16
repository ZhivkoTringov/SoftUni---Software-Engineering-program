function wordTracker(input) {
  words = {};
  searchedWord = input.shift().split(" ");
  for (let i = 0; i < searchedWord.length; i++) {
    words[searchedWord[i]] = 0;
    for (let j = 0; j < input.length; j++) {
      if (input[j] === searchedWord[i]) {
        words[searchedWord[i]] += 1;
      }
    }
  }
  const entries = Object.entries(words);
  let sortedWords = entries.sort(([wordA, valueA], [wordB, valueB]) => valueB - valueA);
  for (const val of sortedWords) {
    console.log(`${val[0]} - ${val[1]}`);
  }
}

wordTracker([
    'is the', 
    'first', 'sentence', 'Here', 'is', 'another', 'the', 'And', 'finally', 'the', 'the', 'sentence']
    );
