#!/usr/bin/python3
"""Helper classes and methods"""
from hashlib import sha256
from itsdangerous.url_safe import URLSafeTimedSerializer


class MySerializer(URLSafeTimedSerializer):
    """Custom serializer class that uses sha256 hashing algorithm."""

    def get_signature(self, value):
        """Return the signature for the given value."""
        return sha256(value).digest()
