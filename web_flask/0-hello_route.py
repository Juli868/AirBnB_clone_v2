#!/usr/bin/python3
"""Flask initialisation."""
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def index():
    """Definition of the job."""
    return ("Hello world!")
