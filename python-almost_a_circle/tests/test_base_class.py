import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestClasses(unittest.TestCase):

    def test_base_class(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_rectangle_class(self):
        r1 = Rectangle(5, 10)
        r2 = Rectangle(3, 7, 1, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)

    def test_square_class(self):
        s1 = Square(4)
        s2 = Square(2, 2, 2)
        self.assertEqual(s1.id, 3)
        self.assertEqual(s2.id, 4)

    def test_save_and_load_from_file(self):
        r3 = Rectangle(8, 16, 4, 8)
        r4 = Rectangle(3, 5, 1, 4)
        s3 = Square(6, 3, 3)
        s4 = Square(2, 1, 1)

        r_list = [r3, r4]
        s_list = [s3, s4]

        Rectangle.save_to_file(r_list)
        Square.save_to_file(s_list)

        loaded_r_list = Rectangle.load_from_file()
        loaded_s_list = Square.load_from_file()

        self.assertEqual(len(loaded_r_list), 2)
        self.assertEqual(len(loaded_s_list), 2)

        for r in loaded_r_list:
            self.assertIsInstance(r, Rectangle)

        for s in loaded_s_list:
            self.assertIsInstance(s, Square)

if __name__ == '__main__':
    unittest.main()