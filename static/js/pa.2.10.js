function addEventListenerToRangeInput() {
    let rangeInput = document.getElementById('seasons');
    rangeInput.addEventListener('change', changedValue);
}

function changedValue() {
    let value = this.value;
    fetch('/pa/2/10/api/' + value)
        .then((response) => {
            console.log(response);
            return response.json();
        })
        .then((data) => {
            console.log(data);
            displayShows(data);
        })
}

function displayShows(data) {
    console.log(data);
    let card = document.getElementById('search-result');
    let table = document.createElement('table');
    for (let i=0; i <  data.length; i++) {
        let row = document.createElement('tr');
        let col = document.createElement('td');
        col.innerHTML = data[i].title;
        row.appendChild(col);
        table.appendChild(row);
    }
    card.innerHTML = '';
    card.appendChild(table);
}

addEventListenerToRangeInput();