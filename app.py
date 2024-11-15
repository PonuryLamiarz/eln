from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        field1 = request.form.get("field1")
        field2 = request.form.get("field2")
        field3 = request.form.get("field3")
        field4 = request.form.get("field4")
        result = f"Field 1: {field1}, Field 2: {field2}, Field 3: {field3}, Field 4: {field4}"
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)