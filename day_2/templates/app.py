from flask import Flask,render_template

app = Flask(__name__)# module
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/welcome/<name>")

def welcome(name):
    return f"Hi {name.title()} welcome<h1>"
@app.route("/addition/<int:num1>/<int:num2>")
def addition(num1,num2):
    return f"addition is {num1+num2}<h1>"

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)


