#!/usr/bin/python3

import unittest
max_integer = __import__("6-max_integer").max_integer

class MaxIntTestCase(unittest.TestCase):
    def test_list_max_end(self):
        res = max_integer([1, 2, 3, 4, 5])
        self.assertEqual(res, 5)


    def test_list_neg_ints(self):
        res = max_integer([-6, -5, -4, -3])
        self.assertEqual(res, -3)


    def test_list_max_start(self):
        res = max_integer([42, 22, 10, 7])
        self.assertEqual(res, 42)


    def test_list_max_mid(self):
        res = max_integer([10, 15, 225, 15, 10])
        self.assertEqual(res, 225)


    def test_list_one_neg(self):
        res = max_integer([1, 2, -3, 4, 5])
        self.assertEqual(res, 5)


    def test_list_one_ele(self):
        res = max_integer([5])
        self.assertEqual(res, 5)


    def test_list_empty(self):
        res = max_integer([])
        self.assertIsNone(res)
