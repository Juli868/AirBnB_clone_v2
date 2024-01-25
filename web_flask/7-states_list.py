#!/usr/bin/python3
from models import storage
from flask import Flask


app = Flask(__name__)


@app.route('/states_list/')
def states_list:
    pass

