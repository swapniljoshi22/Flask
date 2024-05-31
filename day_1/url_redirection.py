from flask import Flask, redirect, url_for

app= Flask(__name__)

@app.route("/")
def welcome():
    return "<h1> Welcome buddy <h1>"
@app.route("/pass")
def passed():
    return "<h1> Buddy pass ho gaya <h1>"

@app.route("/failed")
def failed():
    return "<h1> Sorry buddy you failed<h1>"
@app.route("/score/<name>/<int:num>")
def score(name,num):
    if num>30:
        #pass
        return redirect(url_for('passed'))
    else:
        #failed
        return redirect(url_for('failed'))


if __name__=="__main__":
    app.run(debug=True)