# Dictionaries

# Dictionaries are collections of key-value pairs.
# They are created using curly braces and do not have a specific order.
person = {
    "name": "John",
    "age": 30,
    "city": "New York",
}

# You can access the value of a dictionary using its key.
print(person["name"])
print(person["age"])
print(person["city"])

# Dictionaries are mutable, which means you can modify their values.
person["age"] = 31
print(person)

# You can use the len function to get the length of a dictionary.
print(len(person))
