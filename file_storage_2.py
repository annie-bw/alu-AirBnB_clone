#!/usr/bin/python3
"""Test FileStorage all()"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.all()
print("OK")
