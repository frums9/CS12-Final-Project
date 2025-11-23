//Y-4L Final Project - Canape, Cascara, Casipit
//This js file will validate the data given by the user via HTML.

function submitFormData() {
    // Get values by ID
    let studentNum = document.getElementById('student_number').value;
    let firstName = document.getElementById('first_name').value;
    let lastName = document.getElementById('last_name').value;
    let age = document.getElementById('age').value;
    let email = document.getElementById('email').value;

    // 1. Validate Names
    if (firstName.trim() === "" || lastName.trim() === "") {
        alert("First Name and Last Name must not be empty.");
        return false; // Stop the form from submitting
    }

    // 2. Validate Age
    // Check if empty, not a number, or less than 18
    if (age === "" || isNaN(age) || parseInt(age) < 18) { 
        alert("Age must be a number and 18 or above.");
        return false; 
    }

    // 3. Validate Student Number (XXXX-XXXXX)
    let studentNumPattern = /^\d{4}-\d{5}$/; 
    if (!studentNumPattern.test(studentNum)) {
        alert("Student Number must be in the format XXXX-XXXXX");
        return false;
    }

    // 4. Validate Email
    let emailPattern = /^[^@]+@[^@]+\.[^@]+$/;
    if (!emailPattern.test(email)) {
        alert("Please enter a valid email address.");
        return false;
    }

    // If code reaches here, all data is valid!
    // Return true to allow the form to send data to Python
    return true; 
}