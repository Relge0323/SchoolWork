// upcoming sets with release dates as an array of objects
let upcomingSets = [
    ["Tarkir: Dragonstorm", "2025-04-11"],
    ["Final Fantasy", "2025-06-13"],
    ["Edge of Eternities", "2025-08-01"],
    ["Marvel Spiderman", "TBC"],
    ["Avatar: The Last Airbender", "2025-11-21"]
];

// calculate remaining days
function getDaysUntilRelease(releaseDate) {
    if (releaseDate === "TBC") {
        return "TBA";
    }

    let today = new Date();
    let release = new Date(releaseDate);
    let timeDiff = release - today;
    return Math.ceil(timeDiff / (1000 * 60 * 60 * 24)); // converting milliseconds to days
}

// countdown display
function displayCountdown() {
    let countdownDiv = document.getElementById("countdown");
    let countdownHTML = "";

    for (let i = 0; i < upcomingSets.length; i++) {
        let setName = upcomingSets[i][0];
        let date = upcomingSets[i][1];
        let daysRemaining = getDaysUntilRelease(date);

        let message;
        if (daysRemaining === "TBA") {
            message = setName + ": Release date to be announced.";
        } else if (daysRemaining < 0) {
            message = setName + ": Released!";
        } else if (daysRemaining === 0) {
            message = setName + ": Releases Today!";
        } else {
            message = setName + ": " + daysRemaining + " days until release.";
        }

        countdownHTML += "<p>" + message + "</p>";
    }

    countdownDiv.innerHTML = countdownHTML;
}

displayCountdown();
