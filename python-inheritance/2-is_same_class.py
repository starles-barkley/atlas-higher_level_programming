#!/usr/bin/python3
''' This module outlines a function that returns whether two classes are the same'''


def is_same_class(obj, a_class):
    '''This function returns whether an object came from a specified class'''
    return (type(obj)) is a_class