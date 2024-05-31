from flask import Flask

app = Flask(__name__)

@app.route("/")

def home():
    return "<h1> Welcome<h1>"

@app.route("/welcome/<name>")

def welcome(name):
    return f"<h1> welcome {name.title()}</h1>"

# @app.route("/welcome/vrushabh")

# def welcome_vrushabh():
#     return "<h1> welcome vrushabh</h1>"
    
    
if __name__ == "__main__":
    app.run(debug=True)