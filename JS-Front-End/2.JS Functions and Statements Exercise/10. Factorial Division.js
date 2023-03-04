function factorialDivision(numOne, numTwo) {

    return (factorial(numOne) / factorial(numTwo)).toFixed(2)

    function factorial(num) {
        if (num === 1) {
            return num;
        } else {
            return num * factorial(num - 1);
        }
    }

}