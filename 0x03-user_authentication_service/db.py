#!/usr/bin/env python3
"""
DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from typing import TypeVar
from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """add new user"""
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **Kwargs) -> User:
        """find a user by the argument provided"""
        if Kwargs is None:
            raise InvalidRequestError
        user_obj = self._session.query(User).filter_by(**Kwargs).first()
        if user_obj is None:
            raise NoResultFound
        return user_obj

    def update_user(self, user_id: int, **kwargs) -> None:
    """ update a user """
    _id = self.find_user_by(id=user_id)
    for key, value in kwargs.items():
        if not hasattr(_id, key):
            raise ValueError
        setattr(_id, key, value)
    self._session.commit()
