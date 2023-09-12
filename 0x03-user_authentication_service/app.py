#!/usr/bin/env python3
"""Flask app"""


from flask import Flask, jsonify, request
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def welcome() -> str:
    """welcome :) """
    return jsonify({"message": "Bienvenue"})


@app.route('/users/', methods=['POST'], strict_slashes=False)
def register_users() -> str:
    """register user from data from the request"""
    try:
        email = request.form.get('email')
        password = request.form.get('password')
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})

    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
