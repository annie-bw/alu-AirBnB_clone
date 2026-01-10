#!/usr/bin/python3
"""Test FileStorage: all() method"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

storage = FileStorage()
all_objs = storage.all()

if isinstance(all_objs, dict):
    print("OK")
else:
    print("Error: all() does not return a dict")
