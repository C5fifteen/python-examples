# Classes

# Classes are templates for objects.
# They are defined using the class keyword and contain attributes and methods.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# You can create an object from a class using the constructor.
john = Person("John", 30)

# You can access the attributes and methods of an object using the dot operator.
print(john.name)
print(john.age)
john.greet()

# You can also define additional methods in a class.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
    
    def increment_age(self):
        self.age += 1
