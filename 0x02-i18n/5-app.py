#!/usr/bin/env python3
""" 5. Mock logging in """
from flask import Flask, render_template, request, g
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

    if locale:
        if locale in app.config['LANGUAGES']:
            return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """
    function that returns a user dictionary or None if the ID cannot
    be found or if login_as was not passed.
    """
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id))


@app.before_request
def before_request():
    """
    function that uses the app.before_request decorator to make it be
    executed before all other functions. uses get_user to find a user
    if any, and sets it as a global on flask.g.user
    """
    g.user = get_user()


@app.route("/")
def index():
    """
    basic Flask app with a single / route and an index.html template
    """
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
