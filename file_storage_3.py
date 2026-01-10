#!/usr/bin/python3
"""Test FileStorage: new() method"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

storage = FileStorage()
obj = BaseModel()
storage.new(obj)

key = f"BaseModel.{obj.id}"
all_objs = storage.all()

if key in all_objs:
    print("OK")
else:
    print("Error: new() did not add object")
