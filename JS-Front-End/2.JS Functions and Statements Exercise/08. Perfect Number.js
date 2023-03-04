function perfectNumber(num) {
    let arr = []

    for (let i = 1; i < num; i++) {
        if ( num % i === 0){
            arr.push(i)
        }
        
    }
    const initialValue = 0
    const sum = arr.reduce((previousValue, currentValue) => previousValue + currentValue, initialValue);

    if (sum === num) {
        console.log('We have a perfect number!');
    } else {
        console.log('It\'s not so perfect.');
    }
}