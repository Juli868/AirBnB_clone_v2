#!/usr/bin/python3
"""Flask initialisation."""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def index():
    """Definition of the job."""
    return ("Hello world!")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
