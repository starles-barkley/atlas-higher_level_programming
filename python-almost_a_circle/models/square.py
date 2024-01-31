#!/usr/bin/python3
"""This module defines a class named Square that inherits from Rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """This is a class named Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """This is the class constructor for Square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size attribute with validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value <= 0:
            raise ValueError("size must be > 0")
        else:
            self.width = value
            self.height = value

    def __str__(self):
        """Override __str__ to return a formatted string"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
