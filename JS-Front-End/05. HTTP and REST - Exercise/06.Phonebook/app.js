function attachEvents() {
    const ulList = document.getElementById('phonebook');
    const loadBtn = document.getElementById('btnLoad');
    const personInput = document.getElementById('person');
    const phoneInput = document.getElementById('phone');
    const createBtn = document.getElementById('btnCreate');
    const BASE_URL = 'http://localhost:3030/jsonstore/phonebook/';


    loadBtn.addEventListener('click', phoneBookLoader);
    createBtn.addEventListener('click', createRegister)


    async function phoneBookLoader (){
        try{
        const data = await fetch(BASE_URL);
        let allData = await data.json();
        ulList.innerHTML = '';
        allData = Object.values(allData);
        for (const {person, phone, _id} of allData) {
            const li = document.createElement('li');
            const button = document.createElement('button');
            button.textContent = 'Delete'
            button.id = _id;
            button.addEventListener('click', deletePhoneBook)
            li.innerHTML = `${person}: ${phone}`;
            li.appendChild(button);
            ulList.appendChild(li);
        }
    } catch (err) {
        console.error(err);
    }

    }

    function createRegister(){
        const person = personInput.value;
        const phone = phoneInput.value;
        httpHeaders = {
            method: 'POST',
            body: JSON.stringify({person, phone})
        }

        fetch(BASE_URL, httpHeaders)
        .then((res) => res.json()
        .then(phoneBookLoader))
        .catch((err) => {
            console.error(err);
        })

        personInput.value = '';
        phoneInput.value = '';
    }

    async function deletePhoneBook(){
        const id = this.id;
        const httpHeaders = {
            method : 'DELETE',
        };

        fetch(`${BASE_URL}${id}`, httpHeaders)
        .then((res)=> res.json())
        .then(phoneBookLoader)
        .catch((err)=> {
            console.error(err)
        })
    }

}

attachEvents();