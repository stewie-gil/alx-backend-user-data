#!/usr/bin/env python3
"""Flask app"""


from flask import Flask, jsonify, request, abort
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


@app.route('/sessions/', methods=['POST'], strict_slashes=False)
def login() -> str:
    """epects form data with email and password
    if the informatoin is incorrect abort"""
    email = request.form.get('email')
    password = request.form.get('password')
    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        response = jsonify({"email": email, "message": "logged in"})
        response.set_cookie('session_id', session_id)
        return response
    else:
        abort(401)


@app.route('/sessions/', methods=['DELETE'], strict_slashes=False)
def logout() -> None:
    """ Destroys the users session id """
    sessoins_id = request.cookie.get('session_id')
    user = AUTH.get_user_from_session_id(sessions_id)
    if user:
        AUTH.destroy_session(user.id)
        return redirect('/')
    else:
        abort(403)


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile() -> str:
    """checks if a user exists based on  the cookie
    and returns the user if they exist"""
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        return jsonify({"email": user.email}), 200
    else:
        abort(403)


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token() -> str:
    """ resets the password
    """
    email = request.form.get('email')
    try:
        token = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": "<reset token>"}), 200
    except ValueError:
        abort(403)


@app.route('reset_password', methods=['PUT'], strict_slashes=Falses)
def update_password() -> str:
    """ updates the users password """
    try:
        email = request.form.get('email')
        new_password = request.form.get('new_password')
        reset = request.form.get('reset_token')
        AUTH.update_password(token, password)
        return jsonify({"email": email, "message": "Password updated"})
    except ValueError:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
