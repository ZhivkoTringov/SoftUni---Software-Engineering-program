function solve(arr, num) {
    secondArr = [];
    for (let i = 0; i < arr.length; i+=num) {
        secondArr.push(arr[i])
    }
    return secondArr;
}