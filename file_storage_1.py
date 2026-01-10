#!/usr/bin/python3
"""Test FileStorage: __objects attribute"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
# Test that __objects is a private attribute
try:
    # Try to access private attribute
    objects = storage._FileStorage__objects
    if isinstance(objects, dict):
        print("OK")
    else:
        print("Error: __objects is not a dict")
except Exception as e:
    print(f"Error: {e}")
