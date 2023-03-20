function piccolo(input) {
  let parked = [];
  let parking = {};
  for (const data of input) {
    info = data.split(", ");
    parking[info[1]] = info[0];
  }

  for (const key in parking) {
    if (parking[key] === "IN") {
      parked.push(key);
    }
  }
  let sortedCars = parked.sort((carA, carB) => carA.localeCompare(carB));
  if (parked.length === 0) {
    console.log(`Parking Lot is Empty`);
  } else {
    for (const car of sortedCars) {
      console.log(car);
    }
  }
}
