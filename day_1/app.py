from flask import Flask

app = Flask(__name__)# module
@app.route("/")
def home():
    return "<h1>Welcome to HomePage!<h1>"
@app.route("/welcome/<name>")
def welcome(name):
    return f"Hi {name.title()} welcome<h1>"
@app.route("/addition/<int:num1>/<int:num2>")
def addition(num1,num2):
    return f"addition is {num1+num2}<h1>"
@app.route("/about")
def about():
    return "<h1>Welcome to About!<h1>"

if __name__ == "__main__":
    app.run(debug=True)


