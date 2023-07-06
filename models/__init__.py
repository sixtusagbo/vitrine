#!/bin/python3
"""
Instantiate an object of storage
"""
from models.engine.db_storage import DBStorage

storage = DBStorage()

storage.reload()
