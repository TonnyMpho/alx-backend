#!/usr/bin/env python3
""" 3. Parametrize templates """
from flask import Flask, render_template, request
from flask_babel import Babel

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
    locale = request.args.get('locale')

    if locale is not None:
        if locale in app.config['LANGUAGES']:
            return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def index():
    """
    basic Flask app with a single / route and an index.html template
    """
    title = "Welcome to Holberton"
    header = "Hello world!"
    return render_template("3-index.html", title=title, header=header)


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
