function solve (nums) {
    let arr = [];
    let theSum = 0;
   nums = String(nums);
   for (let i = 0; i < nums.length; i++) {
    arr.push(nums[i])
   }
   for (let index = 0; index < arr.length; index++) {
    theSum += Number(arr[index]) 
   }
    console.log(theSum);
}