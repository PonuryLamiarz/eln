from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        field1 = request.form.get("field1")
        field2 = request.form.get("field2")
        field3 = request.form.get("field3")
        field4 = request.form.get("field4")
        
        # Format the data to save
        result = f"Field 1: {field1}, Field 2: {field2}, Field 3: {field3}, Field 4: {field4}"
        
        # Save data to a file
        with open("data.txt", "a") as file:
            file.write(result + "\n")  # Append each entry on a new line

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
