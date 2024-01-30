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
        """This method returns the JSON representation of a dictionary"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """This method writes the JSON str representation to a file"""
        if list_objs is None:
            list_objs = []
        filename = "{}.json".format(cls.__name__)
        with open(filename, 'w') as file:
            dict_list = [obj.to_dictionary() for obj in list_objs]
            json_string = cls.to_json_string(dict_list)
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """This method returns the list of the JSON string representation"""
        if json_string is None or not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """This method returns a dict with all attributes set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """This method returns a list of instances"""
        filename = cls.__name__ + ".json"