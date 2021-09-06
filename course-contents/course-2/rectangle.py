
class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width


    def area(self):
        return self.length * self.width


class Square(Rectangle):

    def __init__(self, length):
        self.length = length
        self.width = length

a = Square(5)
print(a.area())
