#!/usr/bin/python3
""" Review module for the HBNB project """
from models.user import User
from models.place import Place
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review classto store review information """
    __tablename__ = "reviews"
    place_id = Column(String
    user_id = ""
    text = ""
