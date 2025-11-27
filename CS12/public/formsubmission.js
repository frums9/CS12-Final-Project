
        function submitFormData(event) {
            event.preventDefault(); // Stop form from reloading the page
            
            // Get values by ID
            let studentNum = document.getElementById('student_number').value;
            let firstName = document.getElementById('first_name').value;
            let lastName = document.getElementById('last_name').value;
            let age = document.getElementById('age').value;
            let email = document.getElementById('email').value;

            // 1. Validate Names
            if (firstName.trim() === "" || lastName.trim() === "") {
                alert("First Name and Last Name must not be empty.");
                return false; 
            }

            // 2. Validate Age
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
            let formData = new FormData();
            // These keys ("studentno", "firstname") MUST match the Python arguments above
            formData.append("studentno", studentNum);
            formData.append("firstname", firstName);
            formData.append("lastname", lastName);
            formData.append("age", age);
            formData.append("email", email);

            fetch("/formsubmission", {
                method: "POST",
                body: formData
            })
            .then(response => response.text())
            .then(result => {
                // This checks the "OK" string we return in Python
                if (result === "OK") {
                    alert("Submission Successful!");

                    // Clear all input fields
                    document.getElementById('student_number').value = "";
                    document.getElementById('first_name').value = "";
                    document.getElementById('last_name').value = "";
                    document.getElementById('age').value = "";
                    document.getElementById('email').value = "";
                } else {
                    alert("Something went wrong on the server.");
                }
            });
            return false;
        }

        function viewAllData() {
            // Note: Your group uses window.open which opens a new tab.
            // If you want it in the same tab, use window.location.href instead.
            window.location.href = "/viewAllData"; 
        }
