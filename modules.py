# Modules

# Modules are Python files that contain functions, classes, and variables.
# You can import a module using the import keyword.
import math

# You can access the functions and variables in a module using the dot operator.
result = math.sqrt(25)
print(result)

# You can also import specific functions or variables from a module using the from keyword.
from math import sqrt
result = sqrt(25)
print(result)

# You can use the as keyword to give a module or function an alias.
from math import sqrt as square_root
result = square_root(25)
print(result)
