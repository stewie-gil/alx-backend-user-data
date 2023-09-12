#!/usr/bin/env python3
""" user model """


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class User(Base):
    """User class represents a user in the system
    Attribtes:
    id (int):  Column(Integer, primary_key=True)
    email (str): Column(String(250), nullable=False)
    hashed_password (str): Column(String(250), nullable=False)
    session__id(str) : Column(String(250), nullable=True)
    reset_token (str): resets token for the user
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session__id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
