#!/usr/bin/python3

'''This is a module that has a class that inherits a list'''


class MyList(list):
    '''This is a class that that inherits from a list'''

    def print_sorted(self):
        ''' This is a function that prints list in ascending order'''
        sorted_list = sorted(self)
        print(sorted_list)
