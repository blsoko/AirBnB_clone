#!/usr/bin/python3
"""
This module defines a User class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Defines a User
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
