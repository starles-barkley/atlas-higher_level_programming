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