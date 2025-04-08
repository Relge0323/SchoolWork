"use strict";
/*    JavaScript 7th Edition
      Chapter 6
      Project 06-01

      Project to validate a form used for setting up a new account
      Author: Michael Egler
      Date:   04/03/2025

      Filename: project06-01.js
*/

let submitButton = document.getElementById("submitButton");
let pwd = document.getElementById("pwd");
let pwd2 = document.getElementById("pwd2");

submitButton.addEventListener("click", function(event) {
    // password pattern from the HTML
    let pwdPattern = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/;

    if (!pwdPattern.test(pwd.value)) {
        pwd.setCustomValidity("Your password must be at least 8 characters with at least one letter and one number");
        pwd.reportValidity();
    } else if (pwd.value !== pwd2.value) {
        pwd2.setCustomValidity("Your passwords must match");
        pwd2.reportValidity();
    } else {
        // clear any custom validation messages
        pwd.setCustomValidity("");
        pwd2.setCustomValidity("");
        document.getElementById("signup").submit();
    }

});