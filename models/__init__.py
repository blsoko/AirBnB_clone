#!/usr/bin/python3
"""
Creates a unique FileStorage instance
"""
from models.engine import file_storage

FileStorage = file_storage.FileStorage
storage = FileStorage()
storage.reload()
