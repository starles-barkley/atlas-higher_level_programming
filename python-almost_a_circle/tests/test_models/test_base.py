#!/usr/bin/python3

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from io import StringIO
import sys


class TestBaseAttributes(unittest.TestCase):
    def test_id_assignment(self):
        self.assertEqual(Base._Base__nb_objects, 0)
        test_obj = Base()
        self.assertEqual(test_obj.id, 1)

    def test_custom_id(self):
        id_obj = Base(89)
        self.assertEqual(id_obj.id, 89)

class TestJSONStringMethod(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_non_dict(self):
        self.assertEqual(Base.to_json_string([1, 2, 3]), "[1, 2, 3]")

    def test_non_list(self):
        self.assertEqual(Base.to_json_string(42), "42")

    def test_success(self):
        rect_1 = Rectangle(4, 5)
        dict_1 = rect_1.to_dictionary()
        expected = '[{"id": 2, "width": 4, "height": 5, "x": 0, "y": 0}]'
        self.assertEqual(Base.to_json_string([dict_1]), expected)

# class TestLoadFileMethod(unittest.TestCase):

class TestFromJSONMethod(unittest.TestCase):
    def test_none_param(self):
        presumably_empty = Base.from_json_string(None)
        self.assertEqual(presumably_empty, [])

    def test_empty_param(self):
        just_empty = Base.from_json_string("[]")
        self.assertEqual(just_empty, [])

    def test_base_dict(self):
        base_dict = {'id': 42}
        dict_list = [base_dict]
        json_list = Base.to_json_string(dict_list)
        self.assertEqual(Base.from_json_string(json_list), [{'id': 42}])

# class TestCreateMethod(unittest.TestCase):