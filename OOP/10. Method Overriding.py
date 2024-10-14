
##! Example 1:-
class Animal:
    def sound(self):
        return "This animal makes a sound"



class Dog(Animal):
    def sound(self):
        return "The dog barks"



    def eat(self):
        return 'Cake'


class Cat(Animal):
    def sound(self):
        return "The cat meows"



# Create instances
animal = Animal()
dog = Dog()
cat = Cat()

print(dog.sound())    
print(cat.sound())    






##! Example 2:-
import math

# Parent class
class Shape:
    def area(self):
        return "Area is not defined for this shape."



# Subclass for Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2 


# Subclass for Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width



# Subclass for Triangle
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height



# Creating instances of shapes
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 4)

# Call the overridden methods
print(f"Circle area: {circle.area()}")         # Output: Circle area: 78.53981633974483
print(f"Rectangle area: {rectangle.area()}")   # Output: Rectangle area: 24
print(f"Triangle area: {triangle.area()}")     # Output: Triangle area: 6.0





##! Example 3:-

import math

# Parent class
class Shape:
    def area(self):
        return "Area is not defined for this shape."

# Subclass for Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        # Call the parent class's area method using super()
        parent_area = super().area()
        return f"{parent_area} But for a circle, the area is {math.pi * self.radius ** 2}"

# Subclass for Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        # Call the parent class's area method using super()
        parent_area = super().area()
        return f"{parent_area} But for a rectangle, the area is {self.length * self.width}"

# Creating instances of shapes
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Call the overridden methods
print(circle.area())       # Output: Area is not defined for this shape. But for a circle, the area is 78.53981633974483
print(rectangle.area())    # Output: Area is not defined for this shape. But for a rectangle, the area is 24
