function pascalCaseSplitter (text) {
    let output = '';
    for (let symbol of text) {
        let asciiCode = symbol.charCodeAt(0);
        if (asciiCode >= 65 && asciiCode <= 90) {
            if (output.length > 0) {
                output += ', ';
            }
            output += symbol;
        } else {
            output += symbol;
        }
    }

    console.log(output);
}




pascalCaseSplitter('SplitMeIfYouCanHaHaYouCantOrYouCan')