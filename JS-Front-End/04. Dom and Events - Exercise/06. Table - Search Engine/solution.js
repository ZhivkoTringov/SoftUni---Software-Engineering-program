function solve() {
   searchInput = document.getElementById('searchField')
   document.querySelector('#searchBtn').addEventListener('click', onClick);

   function onClick() {
      const searchedWord = searchInput.value;
      const rows = Array.from(document.querySelectorAll('tbody tr'));
      for (const row of rows) {
         let rowText = row.textContent.trim();


         if (row.classList.contains('select')){
            row.classList.remove('select');
         }

         if (rowText.includes(searchedWord)){
            row.classList.add('select');
         }
      }
      searchInput.value = ''
   }
}