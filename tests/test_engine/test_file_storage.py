import unittest
import json
from models import FileStorage, BaseModel


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """Set up a FileStorage instance before each test"""
        self.file_storage = FileStorage()

    def test_all(self):
        """Test the all method"""
        result = self.file_storage.all()
        self.assertIsInstance(result, dict)
        self.assertEqual(result, FileStorage._FileStorage__objects)

    def test_new(self):
        """Test the new method"""
        obj = BaseModel(id='test_id', attribute1='value1', attribute2='value2')
        self.file_storage.new(obj)
        expected_key = 'BaseModel.test_id'
        self.assertIn(expected_key, FileStorage._FileStorage__objects)
        self.assertEqual(FileStorage._FileStorage__objects[expected_key], obj)

    def test_save(self):
        """Test the save method"""
        obj = BaseModel(id='test_id', attribute1='value1', attribute2='value2')
        self.file_storage.new(obj)
        self.file_storage.save()
        with open(FileStorage._FileStorage__file_path, 'r') as f:
            data = json.load(f)
            expected_data = {f'BaseModel.{obj.id}': obj.to_dict()}
            self.assertEqual(data, expected_data)

    def test_reload_file_not_found(self):
        """Test reload when the file does not exist"""
        self.file_storage.reload()
        self.assertEqual(self.file_storage.all(), {})

    def test_reload_file_found(self):
        """Test reload when the file does exist"""
        data = {'BaseModel.test_id': {'id': 'test_id', 'attribute1': 'value1', 'attribute2': 'value2'}}
        with open(FileStorage._FileStorage__file_path, 'w') as f:
            json.dump(data, f)
        self.file_storage.reload()
        expected_obj = BaseModel(id='test_id', attribute1='value1', attribute2='value2')
        self.assertEqual(self.file_storage.all(), {f'BaseModel.{expected_obj.id}': expected_obj})

if __name__ == '__main__':
    unittest.main()
