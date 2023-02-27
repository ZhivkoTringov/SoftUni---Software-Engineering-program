function solve(kmPh, area) {
  let speedLimit;
  let diff = kmPh - speedLimit;
  switch (area) {
    case "motorway":
      speedLimit = 130;
      diff = kmPh - speedLimit;
      break;

      case "city":
      speedLimit = 50;
      diff = kmPh - speedLimit;
      break;

      case "interstate":
      speedLimit = 90;
      diff = kmPh - speedLimit;
      break;

      case "residential":
      speedLimit = 20;
      diff = kmPh - speedLimit;
      break;
  }
  if (kmPh <= speedLimit) {
    console.log(`Driving ${kmPh} km/h in a ${speedLimit} zone`);
  } else if (kmPh > speedLimit && diff <= 20) {
    console.log(
      `The speed is ${diff} km/h faster than the allowed speed of ${speedLimit} - speeding`
    );
  } else if (kmPh > speedLimit && diff <= 40) {
    console.log(
      `The speed is ${diff} km/h faster than the allowed speed of ${speedLimit} - excessive speeding`
    );
  } else if (kmPh > speedLimit && diff > 40) {
    console.log(
      `The speed is ${diff} km/h faster than the allowed speed of ${speedLimit} - reckless driving`
    );
  }
}