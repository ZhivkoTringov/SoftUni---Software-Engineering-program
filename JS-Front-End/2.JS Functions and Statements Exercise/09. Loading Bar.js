function loadingBar(num) {
    let loadedBar = [...'..........'];
    let loadedPercent = num / 10;
    for (let i = 0; i < loadedPercent; i++) {
        loadedBar.splice(i, 1, '%')
        
    }
    if (num < 100) {
        return `${num}% [${loadedBar.join('')}]\n Still loading...`;
    }else{
        return `100% Complete! \n [${loadedBar.join('')}]`;
    }
    

}