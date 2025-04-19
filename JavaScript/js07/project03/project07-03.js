"use strict";
/*    JavaScript 7th Edition
      Chapter 7
      Project 07-03

      Project to create a New Year's Eve countdown clock
      Author: Michael Egler
      Date: 04/18/2025

      Filename: project07-03.js
*/

let currentTime = document.getElementById("currentTime");
let daysLeftBox = document.getElementById("days");
let hrsLeftBox = document.getElementById("hours");
let minsLeftBox = document.getElementById("minutes");
let secsLeftBox = document.getElementById("seconds");

// Step 3: Run countdown every second
setInterval(countdown, 1000);

// Step 4: Define the countdown function
function countdown() {
  // Step 5: Current date and time
  let now = new Date();

  // Step 6: Show current time
  currentTime.textContent = now.toLocaleString();

  // Step 7: Set initial New Year date
  let newYear = new Date("January 1, 2024");

  // Step 8: Get next year value
  let nextYear = now.getFullYear() + 1;

  // Step 9: Update newYear to nextYear
  newYear.setFullYear(nextYear);

  // Step 10a: Calculate time differences
  let daysLeft = (newYear - now) / (1000 * 60 * 60 * 24);
  let hrsLeft = (daysLeft % 1) * 24;
  let minsLeft = (hrsLeft % 1) * 60;
  let secsLeft = (minsLeft % 1) * 60;

  // Step 11: Display results
  daysLeftBox.textContent = Math.floor(daysLeft);
  hrsLeftBox.textContent = Math.floor(hrsLeft);
  minsLeftBox.textContent = Math.floor(minsLeft);
  secsLeftBox.textContent = Math.floor(secsLeft);
}