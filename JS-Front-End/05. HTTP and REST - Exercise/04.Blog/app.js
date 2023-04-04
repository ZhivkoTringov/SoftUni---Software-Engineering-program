function attachEvents() {
    const loadBtn = document.getElementById('btnLoadPosts');
    const viewBtn = document.getElementById('btnViewPost');
    const selectOptions = document.getElementById('posts');
    const ulList = document.getElementById('post-comments');
    const postTitle = document.getElementById('post-title');
    const postBody = document.getElementById('post-body');
    const POST_URL = 'http://localhost:3030/jsonstore/blog/posts/';
    const VIEW_URL = ' http://localhost:3030/jsonstore/blog/comments';
    let posts = [];
    

    loadBtn.addEventListener('click', loadHandler);
    viewBtn.addEventListener('click', viewHandler);



    async function loadHandler(){
       
        const optionLoader = await fetch(POST_URL);
        let optionData = await optionLoader.json();
        selectOptions.innerHTML = '';
        optionData = Object.values(optionData);
        for (const {body, title, id} of optionData) {
            const optionElement = document.createElement('option');
            optionElement.value = id;
            optionElement.textContent = title;
            selectOptions.appendChild(optionElement);
            posts.push({currentTitle: title, currentBody: body})
            
        }
        
    }

    async function viewHandler(){
        const viewLoader = await fetch(VIEW_URL);
        let viewData = await viewLoader.json();
        ulList.innerHTML = '';
        viewData = Object.values(viewData).filter(el => el.postId === selectOptions.value);
        postTitle.textContent = selectOptions.selectedOptions[0].textContent;
        const mainBody = posts.filter(p => p.currentTitle === selectOptions.selectedOptions[0].textContent);
        postBody.textContent = mainBody[0].currentBody;

        
        
        
        for (const currentData of viewData) {
            const li = document.createElement('li');
            li.textContent = currentData.text;
            ulList.appendChild(li);
            
        }
        
        
            
    
    


            
        

    }
}

attachEvents();