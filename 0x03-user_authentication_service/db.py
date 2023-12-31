#!/usr/bin/env python3
"""DB module"""


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from user import User
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from user import Base


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
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
        """adds  a user to a database"""
        userobj = User(email=email, hashed_password=hashed_password)
        self._session.add(userobj)
        self._session.commit()
        return userobj

    def find_user_by(self, **kwargs) -> User:
        """ takes in arbitrary keyword arguments and
        returns the first row found in the users table"""
        try:
            results = self._session.query(User).filter_by(**kwargs).all()
            if results:
                for result in results:

                    return result

            else:
                raise NoResultFound
        except InvalidRequestError as e:
            self._session.rollback()
            raise e

    def update_user(self, user_id: int, **kwargs) -> None:
        """ update the user’s attributes
        as passed in the method’s arguments"""
        record = self.find_user_by(id=user_id)
        if record:
            for key, value in kwargs.items():
                if not hasattr(record, key):
                    raise ValueError
                else:
                    setattr(record, key, value)
                    self._session.commit()
                self._session.close()
