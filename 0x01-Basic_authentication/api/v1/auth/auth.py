#!/usr/bin/env python3
"""creating class auth"""
from flask import request
from typing import List, TypeVar


class Auth:
    """class auth"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """authentication requirements"""
        return False

    def authorization_header(self, request=request) -> str:
        """auth header"""
        return None

    def current_user(self, request=request) -> TypeVar('User'):
        """current user function/middleware"""
        return None
