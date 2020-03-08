function addEventListenersToCards() {
    let cards = document.getElementsByClassName('format-card')
    for (let i = 0; i < cards.length; i++) {
        cards[i].addEventListener('click', selectCard)
    }
}

function selectCard(t) {
    if (t.target.tagName === 'CARD') {
        let classes = t.target.classList;
        let selected = false;
        for (let i = 0; i < classes.length; i++) {
            if (classes[i] === 'selected') {
                selected = true
            }
        }
        if (selected === true) {
            t.target.classList.remove('selected')
        } else {
            t.target.classList.add('selected')
        }
        displayRating()
    }
}

function displayRating() {
    let rating = document.getElementById('rating');
    let selected = document.getElementsByClassName('selected');
    let sum = 0;
    for (let i = 0; i < selected.length; i++) {
        for (let j = 0; j < selected[i].children.length; j++) {
            if (selected[i].children[j].className === 'avg-rating') {
                sum += parseFloat(selected[i].children[j].innerHTML)
            }
        }
    }
    let avg = sum / selected.length;
    rating.innerHTML = avg;
}

addEventListenersToCards();