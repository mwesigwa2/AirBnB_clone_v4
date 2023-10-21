#!/usr/bin/python3
'''
script that starts Flask web application
'''
from flask import Flask


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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
