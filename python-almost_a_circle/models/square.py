#!/usr/bin/python3
"""This module defines a class named Square that inherits from Rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """This is a class named Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor for Square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size attribute with validation"""
        self.width = value
        self.height = value

    def __str__(self):
        """Override __str__ to return a formatted string"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
