#!/usr/bin/python3
"""This module defines a class named Square that inherits from Rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """This is a class named Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """This is the class constructor for Square"""
        super().__init__(size, size, x, y, id)
