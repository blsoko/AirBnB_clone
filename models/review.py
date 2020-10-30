#!/usr/bin/python3
"""
This module defines a Review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """define place_id, user_id and text"""
    place_id = ""
    user_id = ""
    text = ""
