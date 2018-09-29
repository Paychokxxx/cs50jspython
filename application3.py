from flask import Flask, render_templates


app = Flask(__name__)

@app.route("/")
def index():
    headline = "Hello world"
    return render_templates("index.html", headline=headline)


@app.route("/bye")
def bye():
    headline = "Bye!"
    return render_templates("index.html", headline=headline)