#!/usr/bin/python3
'''This is a module that reads a file'''


def read_file(filename=""):
    """This function reads from a file and prints to stdout"""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
