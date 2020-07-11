import math

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calc_area(self):
        area = self.width*self.height
        return area

    def calc_perimeter(self):
        perimeter = self.width*2 + self.height*2
        return perimeter

    def calc_diag(self):
        diag = math.sqrt(self.width**2 + self.height**2)
        return diag

    def is_square(self):
        if self.width == self.height:
            return True
        else:
            return False


rectangle_1 = Rectangle(2,4)
area = rectangle_1.calc_area()

print(f"Area: {area}")

perimeter = rectangle_1.calc_perimeter()

print(f"Perimeter: {perimeter}")

diag = rectangle_1.calc_diag()

print(f"Diagonal: {diag}")

if rectangle_1.is_square():
    print("This is a square")
else:
    print("This is a rectangle, not a square")