class Shape:
    def area(self):
        return "Undefined"

class Rectangle(Shape):
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def set_length(self, length):
        if length > 0:
            self.__length = length
        else:
            print("Length must be positive")

    def get_length(self):
        return self.__length

    def set_width(self, width):
        if width > 0:
            self.__width = width
        else:
            print("Width must be positive")

    def get_width(self):
        return self.__width

    def area(self):
        return self.__length * self.__width

class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def set_radius(self, radius):
        if radius > 0:
            self.__radius = radius
        else:
            print("Radius must be positive")

    def get_radius(self):
        return self.__radius

    def area(self):
        return 3.14 * self.__radius ** 2

shapes = [Rectangle(2, 3), Circle(5)]


for shape in shapes:
    print(f"Area: {shape.area()}")
    if isinstance(shape, Rectangle):
        shape.set_length(4)
        shape.set_width(5)
    elif isinstance(shape, Circle):
        shape.set_radius(6)
    
    print(f"Updated Area: {shape.area()}")
