#!/usr/bin/env python3
"""creating class auth"""
from flask import request
from typing import List, TypeVar


class Auth:
    """class auth"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """authentication requirements"""
        if path is None or excluded_paths is None or not len(excluded_paths):
            return True
        if path[-1] == '/':
            path += "/"
        for i in excluded_paths:
            if i.endswith('*'):
                if path.startswith(i[:1]):
                    return False
        if path in excluded_paths:
            return False
        return False

    def authorization_header(self, request=request) -> str:
        """auth header"""
        return None

    def current_user(self, request=request) -> TypeVar('User'):
        """current user function/middleware"""
        return None
