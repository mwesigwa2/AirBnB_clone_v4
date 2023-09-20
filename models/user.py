#!/usr/bin/python3
<<<<<<< HEAD
"""user class"""
from models.base_model import BaseModel, Base, Column, String
=======
"""This module defines a class User"""
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import String
>>>>>>> 9e372b3d1dae5e46453c59c505ef829750846485
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
<<<<<<< HEAD
    """This is the class for user
    Attributes:
        email: email
        password: passwordn
        first_name: first name
        last_name: last name
    """
=======
    """This class defines a user by various attributes"""
>>>>>>> 9e372b3d1dae5e46453c59c505ef829750846485
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", backref="user")
    reviews = relationship("Review", backref="user")
