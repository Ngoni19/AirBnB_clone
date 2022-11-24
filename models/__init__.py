#!/usr/bin/python3
"""
Intialize the method for the models directory
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
