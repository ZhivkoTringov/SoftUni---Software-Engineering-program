function solve() {
  const busContainer = document.querySelector("#info > span");
  const departBtn = document.getElementById("depart");
  const arriveBtn = document.getElementById("arrive");
  const BASE_URL = "http://localhost:3030/jsonstore/bus/schedule/";
  let nextStop = "depot";
  let stopName = null;

  function depart() {
    arriveBtn.disabled = false;
    departBtn.disabled = true;
    fetch(`${BASE_URL}${nextStop}`)
      .then((res) => res.json())
      .then((nextStopInfo) => {
        const {name, next} = nextStopInfo;
        busContainer.textContent = `Next stop ${name}`
        nextStop = next;
        stopName = name;
      })
      .catch(() => {
        busContainer.textContent = "Error";
        arriveBtn.disabled = true;
        departBtn.disabled = true;
      });
  }

  async function arrive() {
    arriveBtn.disabled = true;
    departBtn.disabled = false;
    busContainer.textContent = `Arriving at ${stopName}`;
  }

  return {
    depart,
    arrive,
  };
}

let result = solve();
