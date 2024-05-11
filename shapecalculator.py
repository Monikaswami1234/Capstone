class shape:
    def area(self):
        pass
    def Perimeter(self):
        pass

class square(shape):
    def __init__(self, side):
        self.side = side 
    def area(self):
        return self.side ** 2 

class rectangle(shape):
    def __init__(self, height, width):
        self.width = width
        self.height = height
    def area(self):
        return self. height * self.width

class circle(shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
    
square = square(5)
rectangle = rectangle(3, 4)
circle = circle(2)

print("Area of Square:", square.area())

print("Area of Rectangle:", rectangle.area())

print("Area of Circle:", circle.area())