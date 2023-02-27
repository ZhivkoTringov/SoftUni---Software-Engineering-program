function solve(start, end) {
    let arr = []
    let theSum = 0;
    for (let i = start; i <= end; i++) {
        theSum += i;
        arr.push(i)
    }
    console.log(...arr);
    console.log(`Sum: ${theSum}`);
}
