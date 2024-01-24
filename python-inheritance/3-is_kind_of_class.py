#!/usr/bin/python3
'''This module has a function that checks whether
an object is an instance of a class or inherited'''


def is_kind_of_class(obj, a_class):
    '''This function determines if an object is
    and instance of a class or inherited '''
    return isinstance(obj, a_class)
