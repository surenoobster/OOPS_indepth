class Parent:
    def __init__(self, name):
        print("Parent init called")
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        self.name = name  # Not calling Parent's init
        self.age = age

class GrandChild(Child):
    def __init__(self, name, age, grade):
        super().__init__(name, age)  # Properly calls Parent's init via MRO
        self.grade = grade

# Example 1: Without `super()`
gc1 = GrandChild("Alice", 10, "A")
# Output: No "Parent init called"

# Example 2: With `super()`
class FixedChild(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Calls Parent's init
        self.age = age

class FixedGrandChild(FixedChild):
    def __init__(self, name, age, grade):
        super().__init__(name, age)  # Properly calls Parent's init
        self.grade = grade

gc2 = FixedGrandChild("Alice", 10, "A")
# Output:
# Parent init called
