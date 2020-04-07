"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"

# Use the 'format' string method to print the same thing

# Finally, print the same thing using an f-string

# printf operator (%)
print("x is %2d, y is %4.2f, z is \"%s\" " % (x, y, z))

# format method ("".format())
print("x is {0:2d}, y is {1:4.2f}, z is \"{2:s}\"".format(x, y, z))

# f-string (f" ")
print(f"x is {x}, y is {y:.2f}, z is \"{z}\"")
