#!/usr/bin/python3
"""Test FileStorage: save() method"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os

# Remove file.json if it exists
if os.path.exists("file.json"):
    os.remove("file.json")

storage = FileStorage()
obj = BaseModel()
storage.new(obj)
storage.save()

if os.path.exists("file.json"):
    print("OK")
else:
    print("Error: save() did not create file.json")
