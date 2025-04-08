function getRandomColor() {
    return `rgb(${Math.floor(Math.random() * 256)}, ${Math.floor(Math.random() * 256)}, ${Math.floor(Math.random() * 256)})`;
}


setInterval(() => {
    document.getElementById("changingText").style.color = getRandomColor();
}, 1000);




// this isnt my code, i took this from the internet