function addItem() {
   const select = document.getElementById('menu');
   const newItemTextContent = document.getElementById('newItemText');
   const newItemValueContent = document.getElementById('newItemValue');
   const newItemText = newItemTextContent.value;
   const newItemValue = newItemValueContent.value;
   const option = document.createElement('option');
   option.textContent = newItemText;
   option.value = newItemValue;
   select.appendChild(option);

   newItemTextContent.value = '';
   newItemValueContent.value = '';
}