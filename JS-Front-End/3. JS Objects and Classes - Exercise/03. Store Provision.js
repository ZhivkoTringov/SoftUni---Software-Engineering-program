function store(stock, ordered){
    let products = {}

    for (let i = 0; i < stock.length; i+=2) {
        products[stock[i]] = Number(stock[i + 1]);
    }


    for (let j = 0; j < ordered.length; j+=2) {
        if (products.hasOwnProperty(ordered[j])) {
            products[ordered[j]] += Number(ordered[j + 1]);
        } else {
            products[ordered[j]] = Number(ordered[j + 1]);
        }
    } 

    for (const key in products) {
        console.log(`${key} -> ${products[key]}`);
    }
}
