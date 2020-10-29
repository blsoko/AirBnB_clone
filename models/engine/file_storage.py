#!/usr/bin/python3
"""
This module defines a FileStorage class
"""
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
        path = type(self).__file_path
        objects = type(self).__objects
        obj_to_dict = {}
        for key, value in objects.items():
            obj_to_dict[key] = value.to_dict()
        with open(path, 'w', encoding='utf-8') as my_file:
            json.dump(obj_to_dict, my_file)
    
    def reload(self):
        from models.base_model import BaseModel
        """
        only if the JSON file (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised
        """
        from models.base_model import BaseModel
        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as myfile:
                dict_obj = json.load(myfile)
            for key, value in dict_obj.items():
                myobject = eval(value['__class__'] + '(**value)')
                type(self).__objects[key] = myobject
        except:
            pass
