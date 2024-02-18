#!/usr/bin/python3


"""
This is a python a script that starts a Flask web application and run templates
"""

from flask import Flask, render_template
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


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """display “Python ”, concate with text value"""
    return 'Python ' + text.replace('_', ' ')


@app.route("/number/<int:n>", strict_slashes=False)
def n_is_integer(n):
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def n_template(n):
    """display a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def even_or_odd(n):
    """display a HTML page only if n is integer
       even or odd
    """
    if (n % 2) == 0:
        status = 'even'
    else:
        status = 'odd'
    return render_template('6-number_odd_or_even.html', n=n, status=status)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
