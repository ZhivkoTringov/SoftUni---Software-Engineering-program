function passwordValidator (password) {
    const isLengthValid = (pass) => pass.length >= 6 && pass.length <=10;
    const isOnlyLettersAndDigits = (pass) => /^[A-Za-z0-9]+$/g.test(pass)
    const hasAtLeastTwoDigits = (pass) => [...pass.matchAll(/\d/g)].length >= 2;

    let passIsValid = true;

    if (!isLengthValid(password)){
        console.log('Password must be between 6 and 10 characters');
        passIsValid = false;
    }

    if (!isOnlyLettersAndDigits(password)) {
        console.log('Password must consist only of letters and digits');
        passIsValid = false
    }

    if (!hasAtLeastTwoDigits(password)) {
        console.log('Password must have at least 2 digits');
        passIsValid = false
    }

    if (passIsValid) {
        console.log('Password is valid');
    }
}