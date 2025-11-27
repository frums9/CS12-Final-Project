import cherrypy
import os

class FormSubmission(object):
    
    @cherrypy.expose
    def index(self):
        raise cherrypy.HTTPRedirect("/formsubmission")

    @cherrypy.expose
    def formsubmission(self, studentno=None, firstname=None, lastname=None, age=None, email=None):
        
        # 1. HANDLE DATA SUBMISSION
        if cherrypy.request.method == 'POST':
            data_entry = f"{studentno}|{firstname}|{lastname}|{age}|{email}\n"
            
            with open("database.txt", "a") as f:
                f.write(data_entry)
            
            # CRITICAL CHANGE: 
            # Your group's JS expects the server to simply say "OK"
            # We do NOT return HTML here anymore.
            return "OK"
        
        # 2. RENDER THE FORM (GET REQUEST)
        return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Form Submission</title>
    <link rel="stylesheet" href="/public/formsubmission.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Libre+Baskerville:wght@400..700&display=swap" rel="stylesheet">
</head>
<body>
    <form class="form" onsubmit="submitFormData(event)">
        <fieldset>
            <legend id="header">
                Database Submission Form
            </legend>
            <div class="main">
                <label for="student_number" class="text">Student Number: </label>
                <input type="text" id="student_number" class="input_field" placeholder="eg. 2024-12345">

                <label for="first_name" class="text">First name:</label>
                <input type="text" id="first_name" class="input_field" placeholder="eg. Juan">

                <label for="last_name" class="text">Last name:</label>
                <input type="text" id="last_name" class="input_field" placeholder="eg. Dela Cruz">

                <label for="age" class="text">Age:</label>
                <input type="text" id="age" class="input_field" placeholder="eg. 18">

                <label for="email" class="text">Email address:</label>
                <input type="text" id="email" class="input_field" placeholder="eg. abc@def.ghi">
                
                <div class="button-container">
                    <input type="submit" value="Submit" class="submit">
                    <button type="button" class="submit" onclick="viewAllData()">View All Data</button>
                </div>
            </div>
        </fieldset>
    </form>
    <script src="/public/formsubmission.js"></script>
</body>
</html>"""

    @cherrypy.expose
    def viewAllData(self):
        if not os.path.exists("database.txt"):
            return "<h1>No data found yet.</h1><a href='/formsubmission'>Go back</a>"
        
        # 1. Start an empty string to hold our HTML rows
        table_rows = ""

        # 2. Open the file and loop through every line
        with open("database.txt", "r") as f:
            for line in f:
                # Remove invisible newlines at the end
                line = line.strip()
                
                # Skip empty lines if any
                if not line:
                    continue

                # 3. Split the line by the pipe symbol '|' we used in Step 1
                # This turns "2024-1|Juan|Cruz|18|..." into a list ["2024-1", "Juan", "Cruz"...]
                parts = line.split("|")
                
                # Check if the line has all 5 parts (to avoid crashing on bad data)
                if len(parts) == 5:
                    student_no = parts[0]
                    f_name = parts[1]
                    l_name = parts[2]
                    age = parts[3]
                    email = parts[4]

                    # 4. Create the HTML row
                    row_html = f"""
                    <tr>
                        <td>{student_no}</td>
                        <td>{f_name}</td>
                        <td>{l_name}</td>
                        <td>{age}</td>
                        <td>{email}</td>
                    </tr>
                    """
                    # Add this row to our big string
                    table_rows += row_html

        # 5. Inject the 'table_rows' into the HTML string below
        return f"""
        <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Local Student Database</title>
    <link rel="stylesheet" href="/public/data_style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Libre+Baskerville:wght@400..700&display=swap" rel="stylesheet">
</head>
<body>
    <fieldset>
        <legend>Local Student Database</legend>
        <div class="scroll">
            <table style="width: 100%">
                <colgroup>
                    <col span="1" style="width: 20%" >
                    <col span="1" style="width: 20%" >
                    <col span="1" style="width: 20%" >
                    <col span="1" style="width: 10%" >
                    <col span="1" style="width: 30%" >
                </colgroup>
                <thead class="head">
                    <tr>
                        <th>Student No.</th>
                        <th>First Name</th>
                        <th>Last Name</th>
                        <th>Age</th>
                        <th>Email</th>
                    </tr>
                </thead>
                <tbody>
                    {table_rows}
                </tbody>
            </table>
        </div>
        <br>
        <div class="button-container">
            <button onclick="window.location.href='/formsubmission'" style="padding: 10px;">Go Back</button>
        </div>
    </fieldset>

</body>
</html>
        """