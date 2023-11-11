'''
Ex.01 Create a class hierarchy for shapes, starting with a base class Shape.
Then, create subclasses like Circle, Rectangle, and Triangle. Implement methods to calculate area and perimeter for each shape.
'''


class Shape:
    existing_id = set()
    def __init__(self, id, colour):
        if id in Shape.existing_id:
            raise ValueError(f"The id {id} is already used.")
        self.id = id
        Shape.existing_id.add(id)
        self.colour = colour

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def set_colour(self,colour):
        self.colour = colour

    def get_colour(self):
        return self.colour

    def area(self):
        raise NotImplementedError("This method should be overridden by subclasses")

    def perimeter(self):
        raise NotImplementedError("This method should be overridden by subclasses")


class Circle(Shape):
    def __init__(self,radius, id, colour):
        super().__init__(id,colour)
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius

    def is_unit_circle(self):
        return self.radius == 1


class Rectangle(Shape):

    def __init__(self,length, width, id, colour):
        super().__init__(id,colour)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2*(self.width + self.length)

    def is_square(self):
        return self.length == self.width


class Triangle(Shape):
    def __init__(self, side1, side2, side3, id, colour):
        super().__init__(id, colour)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        semiperimeter = self.perimeter() / 2
        return (semiperimeter * (semiperimeter - self.side1) * (semiperimeter - self.side2) * (
                    semiperimeter - self.side3)) ** 0.5

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    def is_right_triangle(self):
        return self.side1 ** 2 + self.side2 ** 2 == self.side3 ** 2 or self.side1 ** 2 + self.side3 ** 2 == self.side2 ** 2 or self.side2 ** 2 + self.side3 ** 2 == self.side1 ** 2

    def is_equilateral(self):
        return self.side1 == self.side2 == self.side3

    def is_isosceles(self):
        return self.side1 == self.side2 or self.side1 == self.side3 or self.side2 == self.side3



