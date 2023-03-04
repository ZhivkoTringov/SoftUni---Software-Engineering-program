function oddAndEvenSum (num) {
    let oddSum = 0;
    let evenSum = 0;
    let numString = num.toString().split('').map(Number);
    for (const i of numString) {
        if (i % 2 === 0){
            evenSum += i;
        } else {
            oddSum += i;
        }
    }
    return `Odd sum = ${oddSum}, Even sum = ${evenSum}`
}
