function fruits (name, grams, pricePerKilogram) {
    let kilos = (grams / 1000);
    let totalPrice = kilos * pricePerKilogram;

    console.log(`I need $${totalPrice.toFixed(2)} to buy ${kilos.toFixed(2)} kilograms ${name}.`);
}