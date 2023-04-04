async function attachEvents() {
  const tBody = document.querySelector('#results tbody');
  const firstNameInput = document.querySelector('input[name="firstName"]');
  const lastNameInput = document.querySelector('input[name="lastName"]');
  const facultyNumberInput = document.querySelector('input[name="facultyNumber"]');
  const gradeInput = document.querySelector('input[name="grade"]');
  const submitBtn = document.getElementById('submit');
  const BASE_URL = 'http://localhost:3030/jsonstore/collections/students';


  submitBtn.addEventListener('click', addNewStudent)



    const studentsData = await fetch(BASE_URL);
    let studentsInfo = await studentsData.json();
    tBody.innerHTML = ''
    studentsInfo = Object.values(studentsInfo);
    for (const {firstName, lastName, facultyNumber, grade, _id} of studentsInfo) {
      const tableRow = document.createElement('tr');
      const firstNameColumn = document.createElement('td');
      const lastNameColumn = document.createElement('td');
      const facultyNumberColumn = document.createElement('td');
      const gradeColumn = document.createElement('td');
      firstNameColumn.textContent = firstName;
      lastNameColumn.textContent = lastName;
      facultyNumberColumn.textContent = facultyNumber;
      gradeColumn.textContent = grade;
      tableRow.appendChild(firstNameColumn);
      tableRow.appendChild(lastNameColumn);
      tableRow.appendChild(facultyNumberColumn);
      tableRow.appendChild(gradeColumn);
      tBody.appendChild(tableRow);
    }

    async function addNewStudent(event) {
      event.preventDefault();
      const firstName = firstNameInput.value;
      const lastName = lastNameInput.value;
      const facultyNumber = facultyNumberInput.value;
      const grade = gradeInput.value;


      if (!firstName || !lastName || !facultyNumber || !grade){
        return;
      }

      const httpHeaders = {
        method : 'POST',
        body : JSON.stringify({firstName, lastName, facultyNumber, grade})
      }

      await fetch(BASE_URL, httpHeaders)
      .then ((res) => res.json())

    }
  



}

attachEvents();