function fadeOutEffect(t) {
    let fadeTarget = t.target;
    let fadeEffect = setInterval(function () {
        if (!fadeTarget.style.opacity) {
            fadeTarget.style.opacity = 1;
        }
        if (fadeTarget.style.opacity > 0) {
            fadeTarget.style.opacity -= 0.1;
        } else {
            clearInterval(fadeEffect);
        }
    }, 200);
}


function addEventListeners() {
    let medals = document.getElementsByClassName('fa-medal')
    console.log(medals);
    for (let i = 0; i < medals.length; i++) {
        console.log(medals[i]);
        medals[i].addEventListener('click', fadeOutEffect);
    }
}

addEventListeners();