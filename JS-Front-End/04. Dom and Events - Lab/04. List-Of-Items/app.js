function addItem() {
    let data = document.getElementById('newItemText').value;
    let li = document.createElement('li');
    li.appendChild(document.createTextNode(data));
    document.getElementById('items').appendChild(li);
    document.getElementById('newItemText').value = ''


    console.log();
}