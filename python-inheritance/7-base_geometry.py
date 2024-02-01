#!/usr/bin/python3
'''This is a module that defines a class named BaseGeometry'''


class BaseGeometry:
    '''This defines a class named BaseGeometry'''
    def area(self):
        '''Public instance method'''
        raise Exception("area() is not implemented")

     def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
