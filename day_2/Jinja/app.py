from flask import Flask,render_template,url_for
from employees import employees_data

app = Flask(__name__,template_folder="templates")# module
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html",title="Home")

@app.route("/welcome/<name>")

def welcome(name):
    return f"Hi {name.title()} welcome<h1>"
@app.route("/addition/<int:num1>/<int:num2>")
def addition(num1,num2):
    return f"addition is {num1+num2}<h1>"
@app.route("/evaluate/<int:num>")
def evaluate(num):
    return render_template(
        "evaluate.html",
        title="Evaluate",
        number=num
    )
@app.route("/employees")
def employees():
    return render_template(
        "employees.html",
        title="Employees",
        employees=employees_data
    )
    
@app.route("/employees/analyst")
def analyst():
    return render_template(
        "analyst.html",
        title="Analyst",
        emps=employees_data
    )

@app.route("/about")
def about():
    return render_template("about.html",title="About")

if __name__ == "__main__":
    app.run(debug=True)


