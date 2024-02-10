#!/usr/bin/python3
""" create a square """

class Square():
    
    width = 0
    height = 0
    
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def Perimeter_Of_My_Square(self):
        return (self.width * 4)

    def __str__(self):
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":

    s = Square(width=12, height=12)
    print(s)
    print(s.area_of_my_square())
    print(s.Perimeter_Of_My_Square())
