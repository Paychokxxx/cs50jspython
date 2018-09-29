from flask import Flask, render_template

app = Flask(__name__)

@app.route("/index2")
def index2():
    names = ["Alice", "Bob", "Jack"]
    return render_template("index2.html", names=names)
