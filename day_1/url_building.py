from flask import Flask, redirect, url_for

app= Flask(__name__)

@app.route("/")
def welcome():
    return "<h1> Welcome buddy <h1>"
@app.route("/pass/failed/<sname>/<int:marks>")
def passed(sname, marks):
    return f"<h1> {sname.title()} pass ho gaya with {marks} marks<h1>"

@app.route("/failed/<sname>/<int:marks>")
def failed(sname,marks):
    return f"<h1> Sorry {sname.title()} you failed because you only scored {marks} marks<h1>"
@app.route("/score/<name>/<int:num>")
def score(name,num):
    if num>30:
        #pass
        return redirect(url_for('passed',sname=name,marks=num))
    else:
        #failed
        return redirect(url_for('failed',sname=name,marks=num))


if __name__=="__main__":
    app.run(debug=True)