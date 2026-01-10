#!/usr/bin/python3
"""Test FileStorage: reload() method"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os

# Create and save an object
obj = BaseModel()
obj.save()

# Create new storage and reload
new_storage = FileStorage()
new_storage.reload()

key = f"BaseModel.{obj.id}"
all_objs = new_storage.all()

if key in all_objs:
    print("OK")
else:
    print("Error: reload() did not load object")

# Cleanup
if os.path.exists("file.json"):
    os.remove("file.json")
