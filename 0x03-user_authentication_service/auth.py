#!/usr/bin/env python3
""" hashing"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound

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

    
#    def register_user(self, email: str, password: str) -> User:
#        """ Takes mandatory email and password string arguments and returns
#        a User object.
#        """
#        result = self._db.find_user_by(email=email)  
#        try:
#            self._db.find_user_by(email=email)
#            raise ValueError(f"User {email} already exists")
#        except NoResultFound:
#            return self._db.add_user(email, _hash_password(password))


    def register_user(self, email: str, password: str) -> User:
        try:
            result = self._db.find_user_by(email=email)
            if result.email == email:
                raise ValueError('User {} already exists'.format(email))
            else:
                hashed = _hash_password(password)
                user = self._db.add_user(email, hashed)
        except NoResultfound as e:
            return user



    def valid_login(self, email: str, password: str) -> bool:
        
