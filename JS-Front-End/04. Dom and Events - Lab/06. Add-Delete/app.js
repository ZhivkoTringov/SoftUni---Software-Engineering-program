function addItem() {
  const ulContainer = document.getElementById("items");
  const input = document.getElementById("newItemText");
  const li = document.createElement("li");
  const anchor = document.createElement("a");
  li.textContent = input.value;
  anchor.textContent = "[Delete]";
  anchor.setAttribute('href', '#');
  anchor.addEventListener("click", deleteHandler);
  li.appendChild(anchor);
  ulContainer.appendChild(li);
  input.value = "";

  function deleteHandler(e) {
    const liItem = e.currentTarget.parentElement;
    liItem.remove();
  }
}
