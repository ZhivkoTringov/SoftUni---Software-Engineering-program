function meetings(stringArr) {
  let schedule = {};
  for (data of stringArr) {
    let [dayOfWeek, name] = data.split(" ");
    if (schedule.hasOwnProperty(dayOfWeek)) {
        console.log(`Conflict on ${dayOfWeek}!`);
    } else {
        schedule[dayOfWeek] = name;
        console.log(`Scheduled for ${dayOfWeek}`);
    }
  }

  for (const key in schedule) {
    console.log(`${key} -> ${schedule[key]}`);
  }
}

