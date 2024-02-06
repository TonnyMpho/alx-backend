#!/usr/bin/env python3
""" Get locale from request """
from flask import Flask, render_template
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)


class Config:
    """ Config class """
    LANGUAGES = ["en", "fr"]

    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """ Get locale from request """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def index():
    """
    basic Flask app with a single / route and an index.html template
    """
    title = "Welcome to Holberton"
    header = "Hello world"
    return render_template("1-index.html", title=_(title), header=_(header))


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
