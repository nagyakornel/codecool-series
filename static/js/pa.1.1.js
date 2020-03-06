function changeBackground(){
    let showEpisodes = document.getElementsByClassName('episodes');
    for (let i = 0; i < showEpisodes.length; i++){
        if (parseInt(showEpisodes[i].innerHTML) % 2 === 0){
            showEpisodes[i].classList.add('even');
        }
        else{
            showEpisodes[i].classList.add('odd');
        }
    }
}

changeBackground();