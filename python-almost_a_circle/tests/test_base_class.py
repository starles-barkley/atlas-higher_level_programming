#!/usr/bin/python3

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

def main():
    # Test Base class
    b1 = Base()
    print("Base instance b1 id:", b1.id)

    b2 = Base()
    print("Base instance b2 id:", b2.id)

    # Test Rectangle class
    r1 = Rectangle(5, 10)
    print("\nRectangle instance r1 id:", r1.id)
    print("Rectangle instance r1:", r1)

    r2 = Rectangle(3, 7, 1, 2)
    print("\nRectangle instance r2 id:", r2.id)
    print("Rectangle instance r2:", r2)

    # Test Square class
    s1 = Square(4)
    print("\nSquare instance s1 id:", s1.id)
    print("Square instance s1:", s1)

    s2 = Square(2, 2, 2)
    print("\nSquare instance s2 id:", s2.id)
    print("Square instance s2:", s2)

    # Test save_to_file and load_from_file methods
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

    print("\nLoaded Rectangle instances:")
    for r in loaded_r_list:
        print(r)

    print("\nLoaded Square instances:")
    for s in loaded_s_list:
        print(s)

if __name__ == "__main__":
    main()