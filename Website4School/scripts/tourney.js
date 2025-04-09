
document.getElementById("tournament-form").addEventListener("submit", function(evt) {
    // name validation
    let name = document.getElementById("name").value;

    if (!name) {
        window.alert("Name is required");
        evt.preventDefault();
        return;
    }


    // email validation
    let email = document.getElementById("email").value;
    let emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;  // i used google.com to find an 'email regex for .js' and this is what it gave me

    if (!email || !emailRegex.test(email)) {
        window.alert("Please enter a valid email address");
        evt.preventDefault();
        return;
    }


    // format validation
    let formatType = document.getElementById("format-type").value;

    if (!formatType) {
        window.alert("Please select a format type");
        evt.preventDefault();
        return;
    }


    //rank validation
    let rank = document.querySelector('input[name="rank"]:checked');

    if (!rank) {
        window.alert("Please select your rank");
        evt.preventDefault();
        return;
    }

    // agreement validation
    let terms = document.getElementById("terms").checked;

    if(!terms) {
        window.alert("You must agree to the tournament rules and terms");
        evt.preventDefault();
        return;
    }

    window.alert("Registration successful!");
});