#!/usr/bin/python3
"""Test FileStorage save()"""
from models import storage
from models.base_model import BaseModel

obj = BaseModel()
obj.save()
print("OK")
