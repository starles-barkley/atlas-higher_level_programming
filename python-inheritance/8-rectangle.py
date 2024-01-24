#!/usr/bin/python3
'''This module contains a class named Rectangle that is inherited'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''This is a class named rectangle that is inherited'''
    def __init__(self, width, height):
        """Instantiation method"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
