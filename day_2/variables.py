# Day 2: Variables and Built-in Functions

first_name = "Brandon"
last_name = "Holland"
full_name = first_name + " " + last_name
country = "United States"
city = "Greensboro"
age = 24
year = 2026
is_married = False
is_true = True
is_light_on = True

print(first_name)
print(last_name)
print(full_name)
print(country)
print(city)
print(age)
print(year)
print(is_married)
print(is_true)
print(is_light_on)

# Day 2: Checking Variable Lengths

print(len(first_name))

first_name_length = len(first_name)
last_name_length = len(last_name)
print(first_name_length)
print(last_name_length)
print(first_name_length == last_name_length)

# Day 2: Compare first and last name lengths
print(first_name_length > last_name_length)

# Day 2: Arithmetic With Variables

num_one = 5
num_two = 4
total = num_one + num_two
print(total)

diff = num_one - num_two
print(diff)

product = num_one * num_two
print(product)

division = num_one / num_two
print(division)

remainder = num_two % num_one
print(remainder)

exponent = num_one ** num_two
print(exponent)

floor_division = num_one // num_two
print(floor_division)

# Day 2: Area of a Circle

radius = 30
area_of_circle = 3.14 * radius ** 2
print(area_of_circle)

# Day 2: Circumference of a Circle

circum_of_circle = 2 * 3.14 * radius
print(circum_of_circle)

# Day 2: Area of a Circle Using User Input

radius_input = input("Enter the radius: ")
radius_input = float(radius_input)

area_input = 3.14 * radius_input ** 2
print(area_input)

# Day 2: User Information

first_name_input = input("Enter your first name: ")
last_name_input = input("Enter your last name: ")
country_input = input("Enter your country: ")
age_input = input("Enter your age: ")

# Day 2: Python Keywords

help("keywords")

# Day 2: Multiple Variables on One Line

first_name, last_name, country, age = "Brandon", "Holland", "United States", 24

print(first_name)
print(last_name)
print(country)
print(age)

# Day 2: Check Data Types

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

# Day 2: Complex Number

complex_number = 1 + 2j
print(type(complex_number))

# Day 2: Euclidean Distance

x1 = 2
y1 = 3
x2 = 10
y2 = 8

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print(distance)

age = 24

age_as_string = str(age)

print(type(age_as_string))

# Day 2: Area of a Triangle

base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

area_of_triangle = 0.5 * base * height

print(area_of_triangle)

# Day 2: Perimeter of a Triangle

side_a = float(input("Enter the length of side a: "))
side_b = float(input("Enter the length of side b: "))
side_c = float(input("Enter the length of side c: "))

perimeter = side_a + side_b + side_c

print(perimeter)

# Day 2: Rectangle Area and Perimeter

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

area_of_rectangle = length * width
perimeter_of_rectangle = 2 * (length + width)

print(area_of_rectangle)
print(perimeter_of_rectangle)

# Day 2: Circle Using User Input

radius = float(input("Enter the radius: "))

area_of_circle = 3.14 * radius ** 2
circumference_of_circle = 2 * 3.14 * radius

print(area_of_circle)
print(circumference_of_circle)

# Day 2: Slope

slope = 2
x_intercept = 1
y_intercept = -2

print(slope)
print(x_intercept)
print(y_intercept)

# Day 2: Slope Between Two Points

x1 = 2
y1 = 2
x2 = 6
y2 = 10

slope_two = (y2 - y1) / (x2 - x1)
print(slope_two)

# Day 2: Compare Slopes

print(slope == slope_two)

# Day 2: Quadratic Equation

x = -3
y = x ** 2 + 6 * x + 9

print(y)

# Day 2: Compare String Lengths

python_length = len("python")
dragon_length = len("dragon")

print(python_length == dragon_length)

# Day 2: Check Words With "in"

print("on" in "python" and "on" in "dragon")

# Day 2: Check "jargon" in Sentence

sentence = "I hope this course is not full of jargon."
print("jargon" in sentence)

# Day 2: Check "on" With not

print("on" not in "python" and "on" not in "dragon")

# Day 2: Python Length Conversion

python_length = len("python")
python_length_float = float(python_length)
python_length_string = str(python_length_float)

print(python_length)
print(python_length_float)
print(python_length_string)

# Day 2: Even Number Check

number = 4
print(number % 2 == 0)

# Day 2: Floor Division Comparison

print(7 // 3 == int(2.7))

# Day 2: Type Conversion

print(type("10") == type(10))

# Day 2: Convert 9.8 to Integer and Compare

print(int(9.8) == 10)