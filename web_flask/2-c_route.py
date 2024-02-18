#!/usr/bin/python3


"""
This is a python a script that starts a Flask web application using url strings
"""

from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_txt_input(text):
    newstr = text.replace('_', ' ')
    return f"C {escape(newstr)}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
