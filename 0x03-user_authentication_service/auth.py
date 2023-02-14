#!/usr/bin/env python3
"""authentication"""
import bcrypt
from db import DB
from user import Base, User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> str:
    """hashed password"""
    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    return hashed


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """intializing auth class"""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """registering method"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            hashed_pwd = _hash_password(password)
            usr = self._db.add_user(email, hashed_pwd)
            return usr
        raise ValueError(f"User {email} already exists")
