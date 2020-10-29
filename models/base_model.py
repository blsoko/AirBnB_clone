#!/usr/bin/python3
"""
This module defines a BaseModel class
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel():
    """
    Defines a BaseModel
    """
    def __init__(self):
        """
        Initializes a BaseModel
        """
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = self.created_at

    def __str__(self):
        """
        Returns a string representation of the BaseModel
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the public attribute updated_at
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__ of the
        instance
        """
        dic_ = self.__dict__.copy()
        if "created_at" in dic_:
            dic_["created_at"] = self.created_at.isoformat("T")
        if "updated_at" in dic_:
            dic_["updated_at"] = self.updated_at.isoformat("T")
        dic_["__class__"] = self.__class__.__name__
        return dic_
