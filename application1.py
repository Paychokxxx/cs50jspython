from flask import flask

app = Flask(__name__)

@app.route("/")
def index(): 
    return "Hello, world!"


@app.route("/david")
def david(): 
    return "Hello, David!"

@app.route("/maria")
def maria(): 
    return "Hello, Maria!"


@app.route("/<string:name>")
def hello(name):
    return f"Hello, {name}!"

@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return f"Hello, {name}!"


@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return f"<h1>Hello, {name}!</h1>"

