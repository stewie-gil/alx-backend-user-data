#!/usr/bin/env python3
""" hashing"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    """ Generates a slat and hash the password"""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


def _generate_uuid() -> str:
    """returns a string representation of a new UUID"""
    id = str(uuid.uuid4())
    return id


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """checks if user is in the databases and adds them"""
        try:
            result = self._db.find_user_by(email=email)
            if result.email == email:
                raise ValueError('User {} already exists'.format(email))
        except NoResultFound:
            hashed = _hash_password(password)
            user = self._db.add_user(email, hashed)
            return user

    def valid_login(self, email: str, password: str) -> bool:
        """ returns true if password is valid, false if otherwise"""
        try:
            result = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode(), result.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """takes an email string argument
        and returns the session ID as a string."""
        try:
            user = self._db.find_user_by(email=email)
            user_id = _generate_uuid()

            self._db.update_user(user.id, session__id=user_id)
            return user_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """ returns user based on a sessoin id """
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session__id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: str) -> None:
        """destroyes the users sessoin id"""
        try:
            self._db.update_user(user_id, session_id=None)
        except NoResultFound:
            return None

    def get_reset_password_token(self, email: str) -> str:
        """resets reset_token based on a unique uuid"""
        try:
            user = self._db.find_user_by(email=email)
            id = _generate_uuid()
            self._db.update_user(user.id, reset_token=id)
            return id
        except NoResultFound:
            raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """updates  a users password"""
        try:
            user = self._db.find_user_by(rest_token=reset_token)
            hashed_password = _hash_password(password)
            self._db.update_user(user.id, hashed_password=hashed_password,
                                 reset_token=None)
        except NoResultFound:
            raise ValueError
