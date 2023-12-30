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


@app.route("/number/<n>")
def number(n):
    """Display only a number."""
    try:
        number = int(n)
        return f"{number} is a number"
    except Exception as e:
        return '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">\n\
                <title>404 Not Found</title>\n\
                <h1>Not Found</h1>\n\
                <p>The requested URL was not found on the server.  \
                If you entered the URL manually please check your \
                spelling and try again.</p>'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
