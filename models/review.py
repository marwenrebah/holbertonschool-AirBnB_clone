#!/usr/bin/python3
"""Review module: Contains the Review class. """
from models.base_model import BaseModel


class Review(BaseModel):
    """inherits from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
