#!/usr/bin/python3
"""Test FileStorage: __file_path attribute"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
# Test that __file_path is a private attribute
try:
    # Try to access private attribute (should work internally)
    file_path = storage._FileStorage__file_path
    if isinstance(file_path, str):
        print("OK")
    else:
        print("Error: __file_path is not a string")
except Exception as e:
    print(f"Error: {e}")
