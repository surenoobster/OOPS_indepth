from person import Person

class Employee(Person):
    def __init__(self, name, age, salary, *args, **kwargs):
        super().__init__(name, age, *args, **kwargs)
        self.salary = salary

    def display_info(self):
        super().display_info()
        print(f"Salary: ${self.salary}")