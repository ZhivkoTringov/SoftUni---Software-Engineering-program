function objects(firstName, lastName, age){
    age = Number(age);
    let person = {firstName, lastName, age}

    return person
}


console.log(objects("Peter", 
"Pan",
"20"));