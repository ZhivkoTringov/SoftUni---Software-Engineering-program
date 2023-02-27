function solve (num, ...params){
    for ( let param of params) {
        if (param === 'chop') {
            num /= 2;
            console.log(num);
        } else if (param === 'dice') {
            num = Math.sqrt(num);
            console.log(num);
        } else if (param === 'spice') {
            num += 1;
            console.log(num);
        } else if (param === 'bake') {
            num *= 3;
            console.log(num);
        } else if (param === 'fillet'){
            num -= num*0.2;
            console.log(num);
        }
    }
}



solve ('9', 'dice', 'spice', 'chop', 'bake', 'fillet')