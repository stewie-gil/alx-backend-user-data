#!/usr/bin/env python3
"""using bycrypt to hash a password"""


import bcrypt
from typing import ByteString


def hash_password(password: str) -> ByteString:
    """ Expects one string argument name password
    and returns a salted, hashed password, which is a byte string
    """
    byte_string = str.encode(password, "utf-8")

    hashed = bcrypt.hashpw(byte_string, bcrypt.gensalt())
    return hashed
