function employees (input) {
    let emp = {};
    for (const employee of input) {
        let num = employee.length;
        emp[employee] = num;
        console.log(`Name: ${employee} -- Personal Number: ${emp[employee]}`);
    }
}