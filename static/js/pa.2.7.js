function addEventListenersToCards(){
    let showCards = document.getElementsByClassName('show-card');
    for (let i = 0; i < showCards.length; i++){
        showCards[i].addEventListener('dblclick', changeBackground)
    }
}

function changeBackground(t){
    let count = parseInt(t.target.children[1].innerHTML);
    if (count % 2 === 0){
        t.target.classList.add('even-num')
    }else{
        t.target.classList.add('odd-num')
    }
}

addEventListenersToCards();