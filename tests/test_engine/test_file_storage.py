#!/usr/bin/python3
"""Unit tests for FileStorage class"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os
import json


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage"""

    def setUp(self):
        """Set up test environment"""
        pass

    def tearDown(self):
        """Clean up after tests"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_file_storage_instance(self):
        """Test FileStorage instantiation"""
        storage = FileStorage()
        self.assertIsInstance(storage, FileStorage)

    def test_all_returns_dict(self):
        """Test that all() returns a dictionary"""
        storage = FileStorage()
        self.assertIsInstance(storage.all(), dict)

    def test_new_adds_object(self):
        """Test that new() adds object to storage"""
        storage = FileStorage()
        model = BaseModel()
        storage.new(model)
        key = f"BaseModel.{model.id}"
        self.assertIn(key, storage.all())

    def test_save_creates_file(self):
        """Test that save() creates file.json"""
        storage = FileStorage()
        model = BaseModel()
        storage.new(model)
        storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_save_writes_correct_json(self):
        """Test that save() writes correct JSON format"""
        storage = FileStorage()
        model = BaseModel()
        storage.new(model)
        storage.save()

        with open("file.json", "r") as f:
            data = json.load(f)

        key = f"BaseModel.{model.id}"
        self.assertIn(key, data)

    def test_reload_loads_objects(self):
        """Test that reload() loads objects from file"""
        model = BaseModel()
        model.save()

        storage = FileStorage()
        storage.reload()
        key = f"BaseModel.{model.id}"
        self.assertIn(key, storage.all())

    def test_reload_with_no_file(self):
        """Test reload when file doesn't exist"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

        storage = FileStorage()
        storage.reload()  # Should not raise error

    def test_reload_with_all_classes(self):
        """Test reload with all class types"""
        user = User()
        state = State()
        city = City()

        user.save()
        state.save()
        city.save()

        storage = FileStorage()
        storage.reload()

        self.assertIn(f"User.{user.id}", storage.all())
        self.assertIn(f"State.{state.id}", storage.all())
        self.assertIn(f"City.{city.id}", storage.all())


if __name__ == '__main__':
    unittest.main()
