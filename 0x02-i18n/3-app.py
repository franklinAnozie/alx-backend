#!/usr/bin/env python3
""" APP.py Entrypoint """


from flask import Flask, render_template, request
from flask_babel import Babel


class Config():
    """ config file """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/", methods=["GET"], strict_slashes=False)
def get_route():
    """ returns index page """
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run()
