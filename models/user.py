#!/usr/bin/python3
"""User module: Contains the User class. """
from models.base_model import BaseModel


class User(BaseModel):
    """inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
