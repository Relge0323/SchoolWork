//a list of some cards to give the search some function.
const doomsdayComboDeck = ["Cut Down", "Duress", "Locust Spray", "Anoint with Affliction", "Go for the Throat", "Sheoldred's Edict", "Mazemind Tome", "Stock Up", "Malicious Eclipse",
                        "Jace, the Perfected Mind", "Deadly Cover-Up", "Harvester of Misery", "Doomsday Excruciator", "Swamp", "Darkslick Shores", "Gloomlake Verge", "Restless Reef",
                        "Undercity Sewers", "Underground River", "Crawling Barrens"];



document.getElementById('cardSearch').addEventListener('submit', function(event) {
    event.preventDefault();
    const cardName = document.getElementById('cardName').value;
    const resultElement = document.getElementById('result');

    try {
        if (cardName === "") {
            throw new Error("invalid entry")
        }

        let cardFound = false;
        for (let i = 0; i < doomsdayComboDeck.length; i++) {
            if (doomsdayComboDeck[i].toLowerCase() === cardName.toLowerCase()) {  // forcing all entries to be treated as lower case, to avoid errors
                cardFound = true;
                break;
            }
        }

        if (cardFound) {
            resultElement.innerHTML = cardName + " was found";
        } else {
            resultElement.innerHTML = cardName + " not found";
        }
    } catch (error) {
        resultElement.innerHTML = error.message;
    }
})