#!/usr/bin/env python3
"""Integration, for various user locations"""
import datetime
import pytz.exceptions
from pytz import timezone
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
    if g.user is None:
        out_time_formatted = datetime.datetime.now(
            pytz.utc).strftime('%b %d, %Y, %I:%M:%S %p')
        return render_template('index.html',
                               user=None, client_time=out_time_formatted)
    client_timezone = get_timezone()
    if client_timezone is None:
        out_time_formatted = datetime.datetime.now(
            pytz.utc).strftime('%b %d, %Y, %I:%M:%S %p')
    else:
        out_time_formatted = datetime.datetime.now(
            timezone(client_timezone)).strftime('%b %d, %Y, %I:%M:%S %p')
    return render_template('index.html', user=g.user['name'],
                           client_time=out_time_formatted)


@babel.localeselector
def get_locale():
    """Get client side location"""
    # if locale is given from url
    if request.args.get('locale'):
        given_lang = request.args.get('locale')
        if given_lang in Config.LANGUAGES:
            return given_lang
    # if locale is in user dictionary
    if g.user is not None:
        if g.user['locale'] is not None:
            if g.user['locale'] in Config.LANGUAGES:
                return g.user['locale']
    # check lang in request header
    in_house_lang: list[str] = Config.LANGUAGES
    return request.accept_languages.best_match(in_house_lang)
    # the default is eng if all fails


def get_user(user_id: int):
    """Login a user"""
    if not user_id:
        return None
    if user_id in users:
        return users[user_id]
    return None


@app.before_request
def before_request():
    """For each request, we have a global user"""
    if request.args.get('login_as'):
        ID: int = int(request.args.get('login_as'))
        g.user = get_user(ID)
    else:
        g.user = None


@babel.timezoneselector
def get_timezone():
    """Get the users time zone"""
    # if timezone parameter is in url
    if request.args.get('timezone'):
        timeZone: str = request.args.get('timezone')
        try:
            return timezone(timeZone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            return None
    # if user is provided and has a known timezone
    if g.user['timezone'] is not None:
        timeZone = g.user['timezone']
        try:
            return timezone(timeZone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            return None


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", 5000)
    app.run(host=host, port=port)
