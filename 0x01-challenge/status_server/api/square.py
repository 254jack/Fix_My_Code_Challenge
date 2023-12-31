#!/usr/bin/python3
"""
square model
"""


class Square():
    """square class"""

    width = 0
    height = 0

    def __init__(self, width, height):
        """instantiation method"""
        if width == height:
            self.width, self.height = width, height

    def areaOfMySquare(self):
        """ Area of the square """
        return self.width * self.height

    def PermiterOfMySquare(self):
        """method to square perimeter"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """print method"""
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":
    s = Square(width=12, height=12)
    print(s)
    print(s.areaOfMySquare())
    print(s.PermiterOfMySquare())
