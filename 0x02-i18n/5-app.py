#!/usr/bin/env python3
"""Integration, for various user locations"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from os import getenv

app = Flask(__name__)


class Config:
    """Config language"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCAL = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


babel = Babel(app)
app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@app.get('/')
def get_home():
    """Return a basic flask web app"""
    if not request.args.get('login_as'):
        return render_template('5-index.html')
    return render_template('5-index.html', user=g.user['name'])


@babel.localeselector
def get_locale():
    """Get client side location"""
    if request.args:
        given_lang = request.args.get('locale')
        if given_lang in Config.LANGUAGES:
            return given_lang
    in_house_lang: list[str] = Config.LANGUAGES
    return request.accept_languages.best_match(in_house_lang)


def get_user(user_id: int):
    """Login a user"""
    if not user_id:
        return None
    if user_id in users:
        return users[user_id]
    return None


@app.before_request
def before_request():
    if request.args.get('login_as'):
        ID: int = int(request.args.get('login_as'))
        g.user = get_user(ID)
    else:
        g.user = None


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", 5000)
    app.run(host=host, port=port, debug=True)
