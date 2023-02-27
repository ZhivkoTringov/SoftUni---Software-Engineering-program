function solve(numberOfPeople, types, dayOfWeek) {
  let price = 0;
  switch (types) {
    case "Students":
      if (dayOfWeek === "Friday") {
        price = 8.45;
      } else if (dayOfWeek === "Saturday") {
        price = 9.8;
      } else if (dayOfWeek === "Sunday") {
        price = 10.46;
      }
      break;
    case "Business":
      if (dayOfWeek === "Friday") {
        price = 10.9;
      } else if (dayOfWeek === "Saturday") {
        price = 15.6;
      } else if (dayOfWeek === "Sunday") {
        price = 16;
      }
      break;
    case "Regular":
      if (dayOfWeek === "Friday") {
        price = 15;
      } else if (dayOfWeek === "Saturday") {
        price = 20;
      } else if (dayOfWeek === "Sunday") {
        price = 22.5;
      }
      break;
  }
  let totalPrice = price * numberOfPeople;
  if (types === "Students" && numberOfPeople >= 30) {
    totalPrice *= 0.85;
  } else if (types === "Business" && numberOfPeople >= 100) {
    totalPrice = price * (numberOfPeople - 10);
  } else if (
    types === "Regular" &&
    numberOfPeople >= 10 &&
    numberOfPeople <= 20
  ) {
    totalPrice *= 0.95;
  }
  console.log(`Total price: ${totalPrice.toFixed(2)}`);
}

solve(40,
    "Regular",
    "Saturday"
    );
