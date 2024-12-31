# Encapsulation: Wrapping data and methods into a single unit (class)
class Animal:
    def __init__(self, name, sound):
        # Private variables
        self.__name = name
        self.__sound = sound
    
    # Public method to access private variables
    def get_name(self):
        return self.__name
    
    def make_sound(self):
        return f"{self.__name} makes a {self.__sound} sound."

# Inheritance: A new class can inherit attributes and methods from an existing class
class Dog(Animal):
    def __init__(self, name, breed):
        # Calling the parent class constructor
        super().__init__(name, "bark")
        self.breed = breed

    def dog_info(self):
        return f"{self.get_name()} is a {self.breed}."

# Polymorphism: The same function behaves differently for different classes
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "meow")
    
    # Overriding the parent method
    def make_sound(self):
        return f"{self.get_name()} makes a soft {self._Animal__sound}."

# Abstraction: Hiding the implementation details and exposing only essential features
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

# Demonstration of OOP Concepts
if __name__ == "__main__":
    # Encapsulation
    animal = Animal("Generic Animal", "sound")
    print(animal.make_sound())

    # Inheritance
    dog = Dog("Buddy", "Golden Retriever")
    print(dog.make_sound())
    print(dog.dog_info())

    # Polymorphism
    cat = Cat("Whiskers")
    print(cat.make_sound())

    # Abstraction
    rectangle = Rectangle(5, 3)
    circle = Circle(7)
    print(f"Rectangle Area: {rectangle.area()}")
    print(f"Circle Area: {circle.area()}")
