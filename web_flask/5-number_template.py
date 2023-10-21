#!/usr/bin/python3
'''
script that starts Flask web application
'''
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """ returns a string """
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ returns a string """
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def c_with_text(text):
    """ returns C with text formatted """
    return "C {}".format(text.replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """ returns python with text formatted """
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def n_is_number(n):
    """ returns a number is input is integer """
    if isinstance(n, int):
        return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """ returns a html if input is integer """
    if isinstance(n, int):
        return render_template("5-number.html", n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
