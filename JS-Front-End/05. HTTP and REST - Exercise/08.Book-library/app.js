function attachEvents() {
  const tBody = document.querySelector("tbody");
  const loadBtn = document.getElementById("loadBooks");
  const titleInput = document.querySelector('input[name="title"]');
  const authorInput = document.querySelector('input[name="author"]');
  const submitBtn = document.querySelector("#form > button");
  const formHeader = document.querySelector('#form > h3');
  let editBookId = null;
  const BASE_URL = "http://localhost:3030/jsonstore/collections/books/";

  loadBtn.addEventListener("click", booksLoader);
  submitBtn.addEventListener("click", submitBook);

  async function booksLoader() {
    tBody.innerHTML = "";
    const data = await fetch(BASE_URL);
    let bookData = await data.json();
    for (const bookId in bookData) {
      const {title, author} = bookData[bookId]
      const tableRow = document.createElement("tr");
      const authorColumn = document.createElement("td");
      const titleColumn = document.createElement("td");
      const buttonColumn = document.createElement("td");
      const editBtn = document.createElement("button");
      const deleteBtn = document.createElement("button");
      editBtn.textContent = "Edit";
      deleteBtn.textContent = "Delete";
      deleteBtn.id = bookId;
      

      editBtn.addEventListener('click', () => {
        editBookId = bookId;
        formHeader.textContent = 'Edit FORM';
        submitBtn.textContent = 'Save';
        titleInput.value = title;
        authorInput.value = author;
      })
      deleteBtn.addEventListener('click', deleteBook);

      titleColumn.textContent = title;
      authorColumn.textContent = author;
      buttonColumn.appendChild(editBtn);
      buttonColumn.appendChild(deleteBtn);
      tableRow.appendChild(titleColumn);
      tableRow.appendChild(authorColumn);
      tableRow.appendChild(buttonColumn);
      tBody.appendChild(tableRow);
    }
  }

  function submitBook() {
    const title = titleInput.value;
    const author = authorInput.value;

    let httpHeaders = {
      method: "POST",
      body: JSON.stringify({ title, author }),
    };
    let url = BASE_URL;
    if (formHeader.textContent === 'Edit FORM'){
      httpHeaders.method = 'PUT';
      url += editBookId;


    }

    fetch(url, httpHeaders)
    .then((res) => res.json()
    .then(booksLoader));
    if (formHeader.textContent === 'Edit FORM'){
      formHeader.textContent = 'FORM';
      submitBtn.textContent = 'Submit';
    }

    titleInput.value = '';
    authorInput.value = '';
  }


  async function deleteBook(){
    const id = this.id;
    httpHeaders = {
      method: 'DELETE'
    };

    await fetch(BASE_URL + id, httpHeaders);
    booksLoader();

  }
}

attachEvents();
