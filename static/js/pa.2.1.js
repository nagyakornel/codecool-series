function addEventListenersToBars(){
    let stars = document.getElementsByClassName('rating');
    for(let i = 0; i < stars.length; i++){
        for (let j = 0; j < stars[i].children.length; j++){
            stars[i].children[j].addEventListener('mouseover', fillStars);
            stars[i].addEventListener('mouseleave', emptyStars);
        }
    }
}

function fillStars(t){
    let value = parseInt(t.target.dataset['value']);

    for (let i = 0; i < t.target.parentNode.children.length; i++){
        if (parseInt(t.target.parentNode.children[i].dataset['value']) <= value){
            t.target.parentNode.children[i].classList = "fas fa-star";
        }
        else{
            t.target.parentNode.children[i].classList = "far fa-star";
        }
    }
}

function emptyStars(t){
    let value = parseInt(t.target.dataset['original']);
    for (let i = 0; i < t.target.children.length; i++){
        if (i < value){
            t.target.children[i].classList = "fas fa-star";
        }
        else{
            t.target.children[i].classList = "far fa-star";
        }
    }
}

addEventListenersToBars();