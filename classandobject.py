#object oriented programing
''''class Person:
    def __init__(self,name,age):   #constructor
        self.name = name
        self.age = age
    

    def display(self):
        print(f"name: {self.name}, Age: {self.age}")

#object creation
p1 = Person("Alice",25)
p1.display'''

#object
class Person:
    def __init__(self, name, age):  # constructor
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Object creation
p1 = Person("Alice", 25)
p1.display()