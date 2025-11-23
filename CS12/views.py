import cherrypy
import os

class FormSubmission(object):
    
    # 1. The Root Redirect
    @cherrypy.expose
    def index(self):
        # Redirects localhost:8080/ -> localhost:8080/formsubmission
        raise cherrypy.HTTPRedirect("/formsubmission")

    # 2. The Combined Handler (Form + Submit)
    @cherrypy.expose
    def formsubmission(self, studentno=None, firstname=None, lastname=None, age=None, email=None):
        
        # SCENARIO A: The user submitted data (POST)
        if cherrypy.request.method == 'POST':
            
            # 1. Format the data
            data_entry = f"Student No: {studentno} | Name: {firstname} {lastname} | Age: {age} | Email: {email}\n"
            
            # 2. Save to file (Append mode)
            with open("database.txt", "a") as f:
                f.write(data_entry)
            
            # 3. Return Success Page
            return f"""
                <h1>Submission Successful!</h1>
                <p>Student No: {studentno}</p>
                <p>Name: {firstname} {lastname}</p>
                <p>Age: {age}</p>
                <p>Email: {email}</p>
                <br>
                <a href='/formsubmission'>Submit another?</a> <br>
                <a href='/viewAllData'>View All Data</a>
            """
        
        # SCENARIO B: The user is just visiting (GET)
        return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Database</title>
    <link rel="stylesheet" href="/public/formsubmission.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Libre+Baskerville:wght@400..700&display=swap" rel="stylesheet">
</head>
<body>
    <form class="form" action="/formsubmission" method="POST" onsubmit="return submitFormData()">
        <fieldset>
            <legend id="header">Local Student Database</legend>
            <div class="main">
                <label for="student_number" class="text">Student Number: </label>
                <input type="text" id="student_number" name="studentno" class="input_field" placeholder="eg. 2023-12345">

                <label for="first_name" class="text">First name:</label>
                <input type="text" id="first_name" name="firstname" class="input_field" placeholder="eg. Juan">

                <label for="last_name" class="text">Last name:</label>
                <input type="text" id="last_name" name="lastname" class="input_field" placeholder="eg. Dela Cruz">

                <label for="age" class="text">Age:</label>
                <input type="number" id="age" name="age" class="input_field" placeholder="eg. 18">

                <label for="email" class="text">Email address:</label>
                <input type="text" id="email" name="email" class="input_field" placeholder="eg. abc@def.ghi">

                <input type="submit" value="Submit" class="submit">
            </div>
        </fieldset>
    </form>
    <script src="/public/formsubmission.js"></script>
</body>
</html>"""

    # 3. The View Data Handler (Requirement #8)
    @cherrypy.expose
    def viewAllData(self):
        if not os.path.exists("database.txt"):
            return "<h1>No data found yet.</h1><a href='/formsubmission'>Go back</a>"
        
        with open("database.txt", "r") as f:
            content = f.read()
        
        # Convert newlines to HTML line breaks
        html_content = content.replace("\n", "<br>")

        return f"""
        <html>
            <head>
                <title>All Data</title>
                <link rel="stylesheet" href="/public/formsubmission.css"> 
            </head>
            <body>
                <h1>All Registered Students</h1>
                <div class="data-display">
                    {html_content}
                </div>
                <br>
                <a href='/formsubmission'>Back to Form</a>
            </body>
        </html>
        """