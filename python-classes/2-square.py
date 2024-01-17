#!/usr/bin/python3
"""Defines a class called square, with variables"""


class Square:
    """This is a class that defines a square"""
    def __init__(self, size=0):
        """This initializes a simple square"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
