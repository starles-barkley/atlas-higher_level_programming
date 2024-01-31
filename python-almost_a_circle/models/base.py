#!/usr/bin/python3

"""This module defines a class named base"""

import json


class Base:
    """This is a class named Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """This method is the class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)


    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"