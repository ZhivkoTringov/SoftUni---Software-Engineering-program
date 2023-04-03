function getInfo() {
  const stopIdInput = document.getElementById("stopId");
  const stopNameContainer = document.getElementById("stopName");
  const bussesContainer = document.getElementById("buses");
  const BASE_URL = "http://localhost:3030/jsonstore/bus/businfo/";
  const stopId = stopIdInput.value;

  fetch(`${BASE_URL}${stopId}`)
    .then((res) => res.json())
    .then((busInfo) => {
      const {buses, name} = busInfo;
      stopNameContainer.textContent = name;
      for (const busId in buses) {
        const li = document.createElement('li');
        li.textContent = `Bus ${busId} arrives in ${buses[busId]} minutes`;
        bussesContainer.appendChild(li);
      }
    })
    .catch(() => {
      stopNameContainer.textContent = 'Error';
    });
}
