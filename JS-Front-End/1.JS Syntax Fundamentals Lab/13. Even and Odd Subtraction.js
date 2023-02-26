function solve (arr) {
    for (let i = 0; i < arr.length; i++) {
        arr[i] =Number(arr[i])        
    }
    let evenSum = 0;
    let oddSum = 0;

    for (let i = 0; i< arr.length; i++) {
      if (arr[i] % 2 === 0){
      evenSum += arr[i]
      } else if (arr[i] % 2 !==0){
        oddSum += arr[i]
      }
    }
    let diff = evenSum - oddSum;
    console.log(diff);
}


solve([2,4,6,8,10])