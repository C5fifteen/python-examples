# Tuples

# Tuples are similar to lists, but they are immutable, which means their elements cannot be modified.
# They are created using parentheses and are also ordered.
colors = ("red", "green", "blue")

# You can access elements in a tuple using their index.
print(colors[0])
print(colors[1])
print(colors[2])

# You cannot modify elements in a tuple.
# The following line will generate a TypeError.
# colors[1] = "yellow"

# You can use the len function to get the length of a tuple.
print(len(colors))
