# Lists

# Lists are collections of values that can be of different data types.
# They are created using square brackets and are ordered.
fruits = ["apple", "banana", "orange"]

# You can access elements in a list using their index.
# Lists are 0-indexed, which means the first element is at index 0.
print(fruits[0])
print(fruits[1])
print(fruits[2])

# Lists are mutable, which means you can modify their elements.
fruits[1] = "grape"
print(fruits)

# You can also add elements to a list using the append function.
fruits.append("mango")
print(fruits)

# You can use the len function to get the length of a list.
print(len(fruits))
