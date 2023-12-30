#!/usr/bin/python3
"""Add a new route."""
from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route("/")
def home():
    """Define home route."""
    return "Hello HBNB"


@app.route("/hbnb")
def HBNB():
    """Define hbnb route."""
    return "HBNB"


@app.route("/c/<text>")
def c_text(text):
    """C followed by a text."""
    return f"C {text.replace('_',' ')}"


@app.route("/python/")
@app.route("/python/<text>")
def python_text(text='is cool'):
    """Define Python route."""
    return f"Python {text.replace('_', ' ')}"


@app.route("/number/<int:n>")
def number(n):
    """Display only a number."""
    return f"{n} is a number"


@app.route('/number_template/<int:n>')
def number_template(n):
    """Display only numbers if int using templates."""
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>')
def odd_or_even(n):
    """Display only numbers if int and its parityusing template."""
    if (n % 2) == 0:
        parity = 'even'
    else:
        parity = 'odd'
    return render_template("5-number.html", n=n, parity = parity)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
