import math

class Shape:
    def area(self):
        pass
    
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


shape_type = input("Enter shape type (rectangle/circle): ").lower()
if shape_type == "rectangle":
    width = float(input("Enter width: "))
    height = float(input("Enter height: "))
    shape = Rectangle(width, height)
elif shape_type == "circle":
    radius = float(input("Enter radius: "))
    shape = Circle(radius)
else:
    print("Invalid shape type")
    shape = None

if shape:
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
