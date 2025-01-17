#!/usr/bin/python3
"""Add a new route."""
from flask import Flask
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
