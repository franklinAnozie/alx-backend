#!/usr/bin/env python3
""" APP.py Entrypoint """


from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def get_route():
    """ returns index page """
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run()
