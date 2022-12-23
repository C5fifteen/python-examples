# Functions

# Functions are blocks of code that can be defined and reused.
# They are defined using the def keyword.
def greet(name):
    print(f"Hello, {name}!")

# You can call a function using its name and passing any required arguments.
greet("John")

# You can also define default values for function arguments.
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("John")
greet("Jane", greeting="Hi")

# You can return a value from a function using the return keyword.
def add(a, b):
    return a + b

result = add(10, 20)
print(result)
