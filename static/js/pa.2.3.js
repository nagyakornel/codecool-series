function addEventListeners(){
    let rows = document.getElementsByTagName('tr');
    for (let i = 0; i < rows.length; i++){
        for (let j = 0; j < rows[i].children.length; j++){
            rows[i].children[j].addEventListener('mouseover', fillBackground);
            rows[i].children[j].addEventListener('mouseleave', emptyBackground);
        }

    }
}

function fillBackground(t){
    let show_id = t.target.parentNode.getAttribute('data-show');
    console.log(show_id);
    let rows = document.querySelectorAll("[data-show='" + show_id + "']");
    for (let row = 0; row < rows.length; row++){
        rows[row].setAttribute('style', "background-color: #4c97ca")
    }
}

function emptyBackground(t) {
    let show_id = t.target.parentNode.getAttribute('data-show');
    let rows = document.querySelectorAll("[data-show='" + show_id + "']");
    console.log(rows);
    for (let row = 0; row < rows.length; row++){
        rows[row].removeAttribute('style')
    }
}

addEventListeners();