#!/usr/bin/env python3
""" hashing"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """ Generates a slat and hash the password"""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password
