function getOldPeople(){
    let actors = document.getElementsByClassName('actor-card');
    for (let i = 0; i < actors.length; i++){
        if (actors[i].getAttribute('data-older') === 'True'){
            actors[i].classList.add('older')
        }
    }
}

function addEventListenersToCards(){
    let cards = document.getElementsByClassName('actor-card');
    for (let i = 0; i < cards.length; i++){
        cards[i].addEventListener('click', alertData)
    }
}

function alertData(){
    let ageAtRelease = this.getAttribute('data-age-at-release');
    let showAge = this.getAttribute('data-show-age');
    alert('Age at release: ' + ageAtRelease + '\nAge of the show: ' + showAge);
}

getOldPeople();
addEventListenersToCards();