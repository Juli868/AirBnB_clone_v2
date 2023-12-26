#!/usr/bin/python3
"""Routing definition."""
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello():
    """Route for home."""
    return ("Hello HBNB!")


@app.route("/hbnb")
def hbnb():
    """Hbnb route."""
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
