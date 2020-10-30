#!/usr/bin/python3
"""
This module defines a City class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """define state and name"""
    state_id = ""
    name = ""
