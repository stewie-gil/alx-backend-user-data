#!/usr/bin/env python3
""" this module contains BasicAuth which
inherits from Auth
"""

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ inherits from auth"""

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """
        Extract and return the Base64 part of the
        Authorization header for Basic Authentication.

        Args:
            authorization_header (str): The Authorization header string.

        Returns:
            str: The Base64 part of the
        Authorization header, or None if not valid.
        """
        if authorization_header is None:
            return None
        elif not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None

        base64_credentials = authorization_header[6:]
        return base64_credentials
