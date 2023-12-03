#!/usr/bin/python3
"""City module: Contains the City class. """
from models.base_model import BaseModel


class City(BaseModel):
    """inherits from BASEmodel"""
    state_id = ""
    name = ""
