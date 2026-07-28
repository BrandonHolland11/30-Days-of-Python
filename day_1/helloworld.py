# Day 1: 30 Days of Python
# Brandon Holland
# Learning Python fundamentals

print("Hello, World!")
print("My name is Brandon")
print("I am learning Python")

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(3 ** 4)
print(3 % 4)
print(3 // 4)

print("Brandon")
print("Holland")
print("United States")
print("I am enjoying 30 Days of Python")

# Day 1: Checking data types

print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(["Brandon", "Holland"]))
print(type("Brandon"))
print(type("Holland"))
print(type("United States"))

# Day 1: Different data types

print(type(10)) # Integer
print(type(10.5)) # Float
print(type(1 + 3j)) # Complex
print(type(True)) # Boolean
print(type("Python")) # String
print(type([1, 2, 3])) # List
print(type((1, 2, 3))) # Tuple
print(type({1, 2, 3})) # Set
print(type({"name": "Brandon"})) # Dictionary

# Day 1: Creating different data types
first_name = "Brandon"
last_name = "Holland"
country = "United States"
city = "Greensboro"

age = 24
height = 6.3

is_student = True

skills = ["Python", "Git", "Github"]

person = {
    "first_name": "Brandon",
    "last_name": "Holland",
    "country": "United States",
}

#Day 1: Variables and arithmetic

num_one = 5
num_two = 4

total = num_one + num_two
difference = num_one - num_two
product = num_one * num_two
division = num_one / num_two

print(total)
print(difference)
print(product)
print(division)

remainder = num_one % num_two
floor_division = num_one // num_two

print(remainder)
print(floor_division)

# More artithmetic with variables
exponent = num_one ** num_two

print(exponent)

# Euclidean distance 

x1 = 2
y1 = 3
x2 = 10
y2 = 8

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print(distance)