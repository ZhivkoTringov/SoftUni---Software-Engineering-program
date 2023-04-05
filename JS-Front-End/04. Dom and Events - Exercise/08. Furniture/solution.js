function solve() {
  const [generateTextArea, buyTextArea] = Array.from(document.getElementsByTagName('textarea'));
  const [generateBtn, buyBtn] = Array.from(document.getElementsByTagName('button'));
  const tBody = document.querySelector('.table > tbody')

  generateBtn.addEventListener('click', generateHandler);
  buyBtn.addEventListener('click', buyHandler)

  function generateHandler(){
    const data = JSON.parse(generateTextArea.value);
    for (const {img, name, price, decFactor} of data){
      const tableRow = createElement('tr', tBody);
      const imgColumn = createElement('td', tableRow);
      createElement('img', imgColumn, '', '', '', {src: img});
      const nameColumn = createElement('td', tableRow);
      createElement('p', nameColumn, name);
      const priceColumn = createElement('td', tableRow);
      createElement('p', priceColumn, price);
      const decFactorColumn = createElement('td', tableRow);
      createElement('p', decFactorColumn, decFactor);
      const markColumn = createElement('td', tableRow);
      const checkBox = createElement('input', markColumn, '', '', '', {type: 'checkbox'});
    }
  }

  function buyHandler(){
    const allCheckedItems = Array.from(document.querySelectorAll('tbody tr input:checked'));
    let boughtItems = [];
    let totalPrice = 0;
    let totalDecFactor = 0;

    for (const input of allCheckedItems) {
      const tableRow = input.parentElement.parentElement;
      const [_firstColumn, secondColumn, thirdColumn, fourthColumn] = Array.from(tableRow.children);
      let item = secondColumn.children[0].textContent;
      boughtItems.push(item)
      let currentPrice = Number(thirdColumn.children[0].textContent);
      totalPrice += currentPrice;
      let currentDecFactor = Number(fourthColumn.children[0].textContent);
      totalDecFactor += currentDecFactor;
    }

    buyTextArea.value += `Bought furniture: ${boughtItems.join(', ')}\n`;
    buyTextArea.value += `Total price: ${totalPrice.toFixed(2)}\n`;
    buyTextArea.value += `Average decoration factor: ${totalDecFactor/allCheckedItems.length}`
  }

  function createElement(
    type,
    parentNode,
    content,
    classes,
    id,
    attributes,
    useInnerHtml
  ) {
    const htmlElement = document.createElement(type);

    if (useInnerHtml) {
      htmlElement.innerHtml = content;
    } else {
      if (content && type !== "input") {
        htmlElement.textContent = content;
      }
      if (content && type === "input") {
        htmlElement.value = content;
      }

      if (classes && classes.length > 0) {
        htmlElement.classList.add(...classes);
      }

      if (id) {
        htmlElement.id = id;
      }

      if (attributes){
        for (const key in attributes) {
          htmlElement[key] = attributes[key];
        }
      }

      if (parentNode){
        parentNode.appendChild(htmlElement);
      }

      return htmlElement;
    }
  }
}
