function addEventListeners() {
    let buttons = document.getElementsByClassName('modal-button');
    for (let i = 0; i < buttons.length; i++){
        buttons[i].addEventListener('click', openModal)
    }
}

function openModal(t) {
    let url = t.target.getAttribute('data-link');
    let modals = document.getElementsByClassName('modal-body');
    let iframe = document.createElement('iframe');
    iframe.setAttribute('width', '100%');
    iframe.setAttribute('height', '400px');
    iframe.setAttribute('src', url);
    modals[0].innerHTML = '';
    modals[0].appendChild(iframe);
    $('#myModal').modal('show')
}

addEventListeners();
