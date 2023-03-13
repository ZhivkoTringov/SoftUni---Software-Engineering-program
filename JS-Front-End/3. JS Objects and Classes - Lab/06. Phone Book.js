function phoneBookArr(input) {
  let phoneBook = {};
  for (let data of input) {
    let [name, phone] = data.split(" ");
    phoneBook[name] = phone;
  }
    for (const key in phoneBook) {
      console.log(`${key} -> ${phoneBook[key]}`);
    }
  
}