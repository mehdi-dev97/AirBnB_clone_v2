#!/usr/bin/python3
""" A script that starts a flask web application listening on
0.0.0.0, port 5000
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """ A method to return Hello HBNB! """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def index_hbnb():
    """ A method to return HBNB """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def cTxt(text):
    """ Displaying C and the value of the text variable """
    return "C " + text.replace("_", " ")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)