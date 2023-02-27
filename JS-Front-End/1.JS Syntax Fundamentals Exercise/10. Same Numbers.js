function solve(num) {
  let arr = [];
  let theSum = 0;
  let statement =''
  num = String(num);
  for (let i = 0; i < num.length; i++) {
    arr.push(num[i]);
  }
  for (let index = 0; index < arr.length; index++) {
    theSum += Number(arr[index]);
    if (arr[0] == arr[index]){
        statement = 'true'
    } else {
        statement ='false';
    }
  }
  console.log(statement);
  console.log(theSum);
}
