function addEventListenersToRatings(){
    let ratings = document.getElementsByClassName('rating');
    for (let i = 0; i < ratings.length; i++){
        ratings[i].addEventListener('click', increaseRating);
        ratings[i].addEventListener('contextmenu', decreaseRating);
    }
}

function increaseRating(t){
    let rating = parseFloat(t.target.innerHTML);
    rating += 0.1;
    rating = rating.toFixed(1);
    t.target.innerHTML = rating;
}

function decreaseRating(t){
    t.preventDefault();
    let rating = parseFloat(t.target.innerHTML);
    rating -= 0.1;
    rating = rating.toFixed(1);
    t.target.innerHTML = rating;
}

addEventListenersToRatings();