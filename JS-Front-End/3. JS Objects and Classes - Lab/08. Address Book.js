function addressBook(stringArr) {
    let bookAddress = {};
    for (const data of stringArr) {
        let [name, address] = data.split(':');
        bookAddress[name] = address;
    }

    let sorted = Object.keys(bookAddress)
    .sort((nameA, nameB) => nameA.localeCompare(nameB));

    for (const key of sorted) {
        console.log(`${key} -> ${bookAddress[key]}`);
    }
}