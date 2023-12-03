#!/usr/bin/python3
"""This is the BaseModel module """
import uuid
from datetime import datetime
import models


class BaseModel:
    """ defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """constructor method"""
        if kwargs:
            for key, value in kwargs.items():
                if key in ("created_at", "updated_at"):
                    if isinstance(value, str):
                        value = datetime.strptime(
                            value, '%Y-%m-%dT%H:%M:%S.%f')
                if "__class__" not in key:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """String representation of the object"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at with
        the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of
        __dict__ of the instance"""
        new = self.__dict__.copy()
        new["__class__"] = self.__class__.__name__
        new["created_at"] = self.created_at.isoformat()
        new["updated_at"] = self.updated_at.isoformat()
        return new
