#!/usr/bin/python3

import unittest
from models.base import Base
from models.square import Square
from io import StringIO
import sys
from os.path import isfile
from os import remove

class TestSquareAttrs(unittest.TestCase):
    def test_just_size(self):
        s1 = Square(5)
        res = s1.__str__()
        self.assertEqual(res, "[Square] (20) 0/0 - 5")

    def test_all_attrs(self):
        s1 = Square(5, 5, 5, 555)
        res = s1.__str__()
        self.assertEqual(res, "[Square] (555) 5/5 - 5")

    def test_str_size(self):
        with self.assertRaises(TypeError):
            s1 = Square("one")

    def test_neg_size(self):
        with self.assertRaises(ValueError):
            s1 = Square(-5)

    def test_zero_size(self):
        with self.assertRaises(ValueError):
            s1 = Square(0)

    def test_str_x(self):
        with self.assertRaises(TypeError):
            s1 = Square(5, "one")

    def test_neg_x(self):
        with self.assertRaises(ValueError):
            s1 = Square(5, -1)

    def test_str_y(self):
        with self.assertRaises(TypeError):
            s1 = Square(5, 1, "one")

    def test_neg_y(self):
        with self.assertRaises(ValueError):
            s1 = Square(5, 1, -1)

    def test_square_area(self):
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)

    def test_square_dictionary(self):
        s1 = Square(8, 2, 2, 800)
        s1_dict = s1.to_dictionary()
        expected = {'id': 800, 'size': 8, 'x': 2, 'y': 2}
        self.assertEqual(expected, s1_dict)

class TestSquareMethods(unittest.TestCase):
    def test_update_args(self):
        s1 = Square(5, 5, 5, 75)
        test_str = s1.__str__()
        self.assertEqual(test_str, "[Square] (75) 5/5 - 5")
        s1.update(750, 10, 2, 2)
        test_str = s1.__str__()
        self.assertEqual(test_str, "[Square] (750) 2/2 - 10")

    def test_update_kwargs(self):
        s1 = Square(5, 5, 5, 75)
        test_str = s1.__str__()
        self.assertEqual(test_str, "[Square] (75) 5/5 - 5")
        update_dict = {'id': 750, 'size': 10, 'x': 2, 'y': 2}
        s1.update(**update_dict)
        test_str = s1.__str__()
        self.assertEqual(test_str, "[Square] (750) 2/2 - 10")

    def test_create_square(self):
        creation_dict = {'id': 548, 'size': 25, 'x': 0, 'y': 10}
        s1 = Square.create(**creation_dict)
        test_str = s1.__str__()
        self.assertEqual(test_str, "[Square] (548) 0/10 - 25")

    def test_load_nonexistent(self):
        if isfile('Square.json'):
            remove('Square.json')
        res = Square.load_from_file()
        self.assertEqual(res, [])

    def test_none(self):
        Square.save_to_file(None)
        self.assertIs(isfile('Square.json'), True)
        self.assertEqual(Square.load_from_file(), [])

    def test_save_empty(self):
        Square.save_to_file([])
        self.assertIs(isfile('Square.json'), True)
        self.assertEqual(Square.load_from_file(), [])

    def test_save_and_load_not_empty(self):
        s1 = Square(3, 3, 3, 333)
        Square.save_to_file([s1])
        res = Square.load_from_file()
        self.assertEqual(res[0].__str__(), "[Square] (333) 3/3 - 3")