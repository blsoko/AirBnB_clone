#!/usr/bin/python3
"""
This module defines a FileStorage class
"""
from models.base_model import BaseModel
import json


class FileStorage():
    """
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
        tojson = {}
        for key in self.__objects.keys():
            tojson[key] = self.__objects[key].to_dict()
        with open(self.__file_path, mode='w', encoding='utf-8') as file_:
            json.dump(tojson, file_)

    def reload(self):
        """
        only if the JSON file (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised
        """
        try:
            path_file = type(self).__file_path
            with open(path_file, mode='r', encoding='utf-8') as myfile:
                dict_obj = json.load(myfile)
            for key, value in dict_obj.items():
                myobject = eval(value['__class__'] + '(**value)')
                type(self).__objects[key] = myobject
        except Exception:
            pass
