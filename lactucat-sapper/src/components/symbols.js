
export default function loadOptionsFunction(filterText) {
    
  filterText = filterText ? filterText.replace(' ','_') : '';

  return new Promise((resolve, reject) => {
    const xhr = new XMLHttpRequest();
    //let responseData = [];
    let ApiToken = "";
    xhr.open('GET', `https://finnhub.io/api/v1/search?q=${filterText}&token=${ApiToken}`);
    //xhr.open('GET', `allSymbolsStatic.json`);
    xhr.send();
    
    xhr.onload = () => {
        console.log("symbols.js function")
        const responsData = JSON.parse(xhr.response);
        const responsData2 = responsData.result;
        console.log(responsData); //this works. Returns an array with search results
        console.log(responsData2);

      if (xhr.status >= 200 && xhr.status < 300) {
        setTimeout(resolve(responsData2), 2000);
      } else {
        reject()
      }
    };
  });

}