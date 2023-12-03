#!/usr/bin/python3
"""objects to a file """

import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    """serializes instances to a JSON file and deserializes JSON
    file to instances """
    __file_path = "file.json"
    __objects = dict()

    def all(self):
        """returns the dictionary objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with a specified key"""
        new_obj = "{}.{}".format(type(obj).__name__,
                                 obj.id)
        FileStorage.__objects[new_obj] = obj

    def save(self):
        """Saves storage dictionary to file"""
        temp = {key: val.to_dict()
                for key, val in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(temp, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, value in temp.items():
                    class_name = value['__class__']
                    del value['__class__']
                    self.new(eval(class_name)(**value))
        except FileNotFoundError:
            pass
