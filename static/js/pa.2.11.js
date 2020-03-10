function addEventListenerToSearchButton(){
    let button = document.getElementById('search-button');
    button.addEventListener('click', fetchData)
}

function fetchData(){
    let genre = document.getElementById('genres').value;
    fetch('/pa/api/' + genre)
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            displayData(data);
        })
}

function displayData(shows) {
    console.log(shows);
    let card = document.getElementById('search-result');
    let table = document.createElement('table');
    for (let i = 0; i < shows.length; i++){
        let tr = document.createElement('tr');
        let title = document.createElement('td');
        title.innerHTML = shows[i].title;
        let season = document.createElement('td');
        season.innerHTML = shows[i].seasons_count;
        let episode = document.createElement('td');
        episode.innerHTML = shows[i].episodes_count;
        tr.appendChild(title);
        tr.appendChild(season);
        tr.appendChild(episode);
        table.appendChild(tr);
    }
    card.innerHTML = '';
    card.appendChild(table);
}

addEventListenerToSearchButton();