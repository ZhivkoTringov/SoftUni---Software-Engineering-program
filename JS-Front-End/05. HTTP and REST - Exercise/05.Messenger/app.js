function attachEvents() {
  const textArea = document.getElementById("messages");
  const nameInput = document.querySelector('input[name="author"]');
  const messageInput = document.querySelector('input[name="content"]');
  const sendBtn = document.getElementById("submit");
  const refreshBtn = document.getElementById("refresh");
  const BASE_URL = "http://localhost:3030/jsonstore/messenger";

  refreshBtn.addEventListener("click", getAllMsgs);
  sendBtn.addEventListener("click", createMsg);

  async function getAllMsgs() {
    const refreshLoader = await fetch(BASE_URL);
    let refreshData = await refreshLoader.json();
    textArea.innerHTML = "";
    refreshData = Object.values(refreshData)
      .map((entry) => `${entry.author}: ${entry.content}`)
      .join("\n");
    textArea.textContent = refreshData;
  }

  function createMsg() {
    const author = nameInput.value;
    const content = messageInput.value;

    const httpHeaders = {
      method: "POST",
      body: JSON.stringify({ author, content }),
    };
    fetch(BASE_URL, httpHeaders).then((res) => res.json());

    nameInput.value = '';
    messageInput.value = '';
  }
}

attachEvents();
