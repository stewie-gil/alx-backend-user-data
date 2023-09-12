#!/usr/bin/env python3
""" hashing"""
import bcrypt
from db import DB
from user import User

def _hash_password(password: str) -> bytes:
    """ Generates a slat and hash the password"""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        result = self._db._session.find_user_by(email, password)
        if result not None:
            raise ValueError('User {} already exists'.format(email))
        else:
            hashed = _hash_password(password)
            user = self._db.add_user(email, hashed)
            return user
