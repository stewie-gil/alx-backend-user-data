#!/usr/bin/env python3
""" the Authentication module"""


from typing import List, TypeVar
from flask import request
import fnmatch

class Auth:
    """Authentication class for handling user authentication."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
         Check if authentication is required for a given path.

        Args:
            path (str): The requested path.
            excluded_paths (List[str]): List of paths excluded from auth.

        Returns:
            bool: True if authentication is required, False otherwise.
        """
        if path is None or not excluded_paths:
            return True

        # Check if any excluded path is a prefix of the given path
        for excluded_path in excluded_paths:
            if fnmatch.fnmatch(path, excluded_path):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Retrieve the authorization header from the Flask request object.

        Args:
            request: The Flask request object.

        Returns:
            str: The authorization header or None if not present.
        """
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieve info about the current user based on the Flask request object.

        Args:
            request: The Flask request object.

        Returns:
            TypeVar('User'): Info about current user or None if not available.
        """
        return None
