function cityInfo (city) {
    let keys = Object.keys(city);
    for (const key of keys) {
        console.log(`${key} -> ${city[key]}`);
    }
}