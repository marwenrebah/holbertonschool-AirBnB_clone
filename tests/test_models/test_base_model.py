#!/usr/bin/python3

import unittest
from datetime import datetime
from models.base_model import BaseModel
import time

class TestBaseModel(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        """Initialize test class"""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel
    
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_constructor_with_kwargs(self):
        data = {
            "id": "some_id",
            "created_at": "2023-01-01T12:00:00.000000",
            "updated_at": "2023-01-02T12:30:00.000000",
            "custom_attr": "some_value"
        }
        obj = BaseModel(**data)

        self.assertEqual(obj.id, data["id"])
        self.assertEqual(obj.created_at, datetime.strptime(data["created_at"], '%Y-%m-%dT%H:%M:%S.%f'))
        self.assertEqual(obj.updated_at, datetime.strptime(data["updated_at"], '%Y-%m-%dT%H:%M:%S.%f'))
        self.assertEqual(obj.custom_attr, data["custom_attr"])

    def test_constructor_without_kwargs(self):
        obj = BaseModel()

        self.assertIsNotNone(obj.id)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_str(self):
        """ Test instance string representation"""
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))


    def test_save_method(self):
        obj = BaseModel()
        previous_updated_at = obj.updated_at
        time.sleep(1)
        obj.save()
        self.assertIsInstance(obj.updated_at, datetime)
        self.assertGreater(obj.updated_at, previous_updated_at)

    def test_to_dict_method(self):
        obj = BaseModel()
        obj_dict = obj.to_dict()

        self.assertIn("__class__", obj_dict)
        self.assertIn("created_at", obj_dict)
        self.assertIn("updated_at", obj_dict)

if __name__ == '__main__':
    unittest.main()
