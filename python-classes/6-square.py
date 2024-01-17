#!/usr/bin/python3

"""This module defines a class named square with a size attribute"""


class Square:
    """A Square class with a private size attribute"""
    def __init__(self, size=0, position=(0, 0)):
        """
        the __init__ method for the Square class

        Args:
            size (int): the size of the Square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter for size private attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for size private attribute

        Args:
            value: the value to set size as
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        getter for position attribute
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        setter for position attribute

        Args:
            value: the value to set position as
        """
        err_msg = "position must be a tuple of 2 positive integers"
        if type(value) is not tuple or len(value) != 2:
            raise TypeError(err_msg)
        for i in value:
            if (type(i) is int and i < 0) or type(i) is not int:
                raise TypeError(err_msg)

        else:
            self.__position = value

    def area(self):
        """
        A method of Square that returns the square area

        Return:
            the square area of the calling instance of Square
        """
        return self.size * self.size

    def my_print(self):
        """
        print the area and position of the square
        """
        if self.size < 1:
            print("")
        else:
            for y in range(self.position[1]):
                print("")
            for i in range(self.size):
                for x in range(self.position[0]):
                    print(" ", end="")
                for j in range(self.size):
                    print("#", end="")
                print("")
