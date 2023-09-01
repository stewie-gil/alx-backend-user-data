#!/usr/bin/env python3
"""using bycrypt to hash a password"""


import bcrypt


def hash_password(password: str) -> bytes:
    """ Expects one string argument name password
    and returns a salted, hashed password, which is a byte string
    """
    byte_string = str.encode(password, "utf-8")

    hashed = bcrypt.hashpw(byte_string, bcrypt.gensalt())
    return hashed


def is_valid(hashed_password: bytes, password str) -> bool:
    """verifying the password matches the hashed on"""
    if bcrypt.checkpw(password, hashed):
        return True
    else:
        return False
