#!/usr/bin/env python3
""" 0. Basic Flask app """
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    """
    basic Flask app with a single / route and an index.html template
    """
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
