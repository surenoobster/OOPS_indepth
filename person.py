class Person:
    def __init__(self, name, age, *args, **kwargs):
        self.name = name
        self.age = age
        self.additional_info = args
        self.details = kwargs

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
        if self.additional_info:
            print("Additional Info:", ", ".join(map(str, self.additional_info)))
        if self.details:
            print("Details:", self.details)