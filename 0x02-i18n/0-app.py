#!/usr/bin/env python3
"""Integration, for various user locations"""
from flask import Flask, render_template
from os import getenv

app = Flask(__name__)


@app.get('/')
def get_home():
    """Return a basic flask web app"""
    return render_template('0-index.html')


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", 5000)
    app.run(host=host, port=port)
