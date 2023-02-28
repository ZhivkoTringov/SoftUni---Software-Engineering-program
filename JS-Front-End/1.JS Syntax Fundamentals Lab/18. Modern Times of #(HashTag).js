function hashTag(strings) {
  let words = strings.split(" ");
  for (let word of words) {
    if (word.startsWith("#") && word.length > 1){
        let flag = true;
        let searchedWord = word.toLowerCase();
        for (let i = 1; i < searchedWord.length; i++) {
            if (searchedWord.charCodeAt(i) < 97 || searchedWord.charCodeAt(i) > 122) {
                flag = false;
                break;
            }
        }
        if (flag) {
        console.log(word.slice(1));
      }
    }
  }
}
