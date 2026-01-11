#!/usr/bin/python3
"""Test FileStorage new()"""
from models import storage
from models.base_model import BaseModel

obj = BaseModel()
storage.new(obj)
print("OK")
