function addEventListenerToButton() {
    let button = document.getElementById('search-button');
    button.addEventListener('click', fetchResults)
}

function fetchResults() {
    let searchString = document.getElementById('search-string').value;
    fetch('/search/' + searchString)
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            fillData(data);
        })
}

function fillData(data) {
    let searchResults = document.getElementById('search-result');
    searchResults.innerHTML = '';
    let ol = document.createElement('ol');
    for (let i = 0; i < data.length; i++) {
        let li = document.createElement('li');
        li.innerHTML = data[i].name + ' played ' + data[i]['character_name'] + ' in ' + data[i].title;
        ol.appendChild(li);
    }
    searchResults.appendChild(ol);
}

addEventListenerToButton();