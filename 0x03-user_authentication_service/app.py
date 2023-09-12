#!/usr/bin/env python3
"""Flask app"""


from flask import Flask, jsonify
from auth import Auth

AUTH = Auth()
app = Flask(__name__)


@app.route("/")
def welcome():
    """welcome :) """
    return jsonify({"message": "Bienvenue"})


@app.route("/user/", strict_slashes=False, POST)
def users(email, password):
    





if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
