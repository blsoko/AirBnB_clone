#!/usr/bin/python3
"""
This module defines a FileStorage class
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


classes = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
}


class FileStorage():
    """
    Defines a FileStorage
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        if obj:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        obj_to_dict = {}
        for key, value in type(self).__objects.items():
            obj_to_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as my_file:
            json.dump(obj_to_dict, my_file, indent=2)

    def reload(self):
        """
        only if the JSON file (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised
        """
        path = type(self).__file_path
        try:
            with open(path, mode='r', encoding='utf-8') as my_file:
                objs = json.load(my_file)
            for key, value in objs.items():
                obj = eval(value['__class__'] + '(**value)')
                type(self).__objects[key] = obj
        except:
            pass
