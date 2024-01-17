#!/usr/bin/python3
"""This module contains a class defined as Rectangle"""


class Rectangle:
    """This is a class that defines a Rectangle"""
    def __init__(self, width=0, height=0):
        """This method initializes its properties"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

