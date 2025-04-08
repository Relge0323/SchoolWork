/*
    Mike Egler
    hamburger.js
    04/06/2025
*/

function hamburger() {
    let menu = document.getElementById("menu-links");
    let hamburgerIcon = document.querySelector(".menu-icon");

    if (menu.style.display === "block") {
        menu.style.display = "none";
        hamburgerIcon.style.display = "block"; // Make sure the hamburger is visible again
    } else {
        menu.style.display = "block";
        hamburgerIcon.style.display = "none"; // Hide the hamburger when menu is open
    }
}
