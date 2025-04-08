/*
Mike Egler
02/09/2025
*/


function calculateBMI() {
    let weight = document.getElementById("weight").value;
    let height = document.getElementById("height").value;


    if (weight > 0 && height > 0) {
        let bmi = (weight / (height * height)) * 703;   // remove the * 703 to convert to kilograms and meters


        if (bmi < 18.5) {
            return window.alert("Underweight");
        } else if (bmi < 24.9) {
            return window.alert("Normal weight");
        } else if (bmi < 29.9) {
            return window.alert("Overweight");
        } else {
            return window.alert("Obese");
        }
    }
}