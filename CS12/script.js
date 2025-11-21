//Y-4L Final Project - Canape, Cascara, Casipit
//This js file will validate the data given by the user via HTML.

//This function will run once the user presses the submit button.
function submitFormData() {
	let studentNum = document.getElementById('studentNumber').value;
	let firstName = document.getElementById('firstName').value;
	let lastName = document.getElementById('lastName').value;
	let age = document.getElementById('age').value;
	let email = document.getElementById('email').value;

	//Validation - Checks if first and last name field is empty.
	if (!firstName || !lastName) {
		alert("First Name and Last Name must not be empty.");
		return;
	}
	//Checks if the user is an adult; aged 18 or above.
	if (isNaN(age) || age < 18) { //isNan = isNotANumber
		alert("Age must be 18 or above and a number.");
		return;
	}
	//Student number format: XXXX-XXXXX
	let studentNumPattern = /^\d{4}-\d{5}$/; //d{n} = n digits; $ = end of string; / / = regex for patterns
	if (!studentNumPattern.test(studentNum)) {
		alert("Student Number must be in the format XXXX-XXXXX");
		return;
	}
	//Email must contain an @ and at least one dot after the @ (one dot at the domain)
	let emailPattern = /^[^@]+@[^@]+\.[^@]+$/;
	if (!emailPattern.test(email)) {
		alert("Please enter a valid email address.");
		return;
	}

	//Once validated, prepare data to send back to the server.
	let formData = {
		studentNumber: studentNum,
		firstName: firstName,
		lastName: lastName,
		age: age,
		email: email
	};

	//Sends object(the dictionary-like string above) to the python server using POST method
	fetch('http://localhost:8080/formsubmission', { //This will open the stated URL
		method: 'POST', //POST method is for sending data to server
		headers: {
			'Content-Type': 'application/json' //Tells server that we are sending JSON(JavaScript Object Notation)
		},
		body: JSON.stringify(formData)//Converts the "formData" JS object to JSON string
	})
	.then(response => response.text())//Server will send back its "response."
	.then(data => {
		alert(data);//Shows message by python server
	})
	.catch(error => {
		alert("An error occurred: " + error);
	});
}

//View All Data
function viewAllData() {
	fetch('http;//127.0.0.1/viewAllData', {
		method: 'GET' //GET method is for requesting data from a specific source.
	})
	.then(response =. response.text()) //Server to return plain text list of all data
	.then(data => {
		alert(data); //Display everything saved in the file
	})
	.catch(error => {
		alert("An error occurred while retrieving data: " + error);
	});
}
