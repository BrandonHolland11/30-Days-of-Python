# Day 3: 30 Days of Python - Operators

integer_variable = 24
float_variable = 187.96
complex_variable = 6 + 7j

# Day 3: Area of a Triangle

input_base = float(input("Enter the base of the triangle: "))
input_height = float(input("Enter the height of the triangle: "))
area_of_triangle = 0.5 * input_base * input_height
print("Area of the triangle:", area_of_triangle)

# Day 3: Perimeter of a Triangle
input_side_a = float(input("Enter the length of side a: "))
input_side_b = float(input("Enter the length of side b: "))
input_side_c = float(input("Enter the length of side c: "))
perimeter_of_triangle = input_side_a + input_side_b + input_side_c
print("Perimeter of the triangle:", perimeter_of_triangle)

# Day 3: Rectangle Area and Perimeter
input_length = float(input("Enter the length of the rectangle: "))
input_width = float(input("Enter the width of the rectangle: "))
area_of_rectangle = input_length * input_width
perimeter_of_rectangle = 2 * (input_length + input_width)
print("Area of the rectangle:", area_of_rectangle)
print("Perimeter of the rectangle:", perimeter_of_rectangle)

# Day 3: Circle Area and Circumference
input_radius = float(input("Enter the radius of the circle: "))
area_of_circle = 3.14 * input_radius ** 2
circumference_of_circle = 2 * 3.14 * input_radius
print("Area of the circle:", area_of_circle)
print("Circumference of the circle:", circumference_of_circle)

# Day 3: Slope & Intercepts
slope = 2
x_intercept = 1
y_intercept = -2
print("Slope:", slope)
print("X-intercept:", x_intercept)
print("Y-intercept:", y_intercept)

# Day 3: Slope Between Two Points

x1 = 2
y1 = 2
x2 = 6
y2 = 10
slope_between_points = (y2 - y1) / (x2 - x1)
print("Slope between points (2, 2) and (6, 10):", slope_between_points)

# Day 3: Compare Slopes

print(slope == slope_between_points)

# Day 3: Quadratic Equation

x = -3
y = x ** 2 + 6 * x + 9
print("Value of y:", y)

# Day 3: Compare Quadratic Values

x = -3
y = x ** 2 + 6 * x + 9
print(y == 0)

# Day 3: Compare String Lengths

python_length = len("python")
dragon_length = len("dragon")
print(python_length == dragon_length)

# Day 3: Check "on" in Python and Dragon

print("on" in "python" and "on" in "dragon")

# Day 3: Check for Jargon

sentence = "I hope this course is not full of jargon."
print("jargon" in sentence)

# Day 3: Check "on" With Not

print("on" not in "python" and "on" not in "dragon")

# Day 3: Python Length Conversion

python_length = len("python")
python_length_float = float(python_length)
python_length_string = str(python_length_float)

print(python_length_float)
print(python_length_string)

# Day 3: Even Number Check

number = 4
print(number % 2 == 0)

# Day 3: Floor Division Comparison

print(7 // 3 == int(2.7))

# Day 3: Type Comparison

print(type("10") == type(10))

# Day 3: Convert 9.8 and Compare

print(int(9.8) == 10)

# Day 3: Python and Dragon Length Comparison

print(len("python") != len("dragon"))

# Day 3: Calculate Pay

hours = float(input("Enter hours: "))
rate_per_hour = float(input("Enter rate per hour: "))

weekly_earning = hours * rate_per_hour

print("Your weekly earning is:", weekly_earning)

# Day 3:  Calculate Seconds Lived

years = int(input("Enter number of years you have lived: "))
seconds_lived = years * 365 * 24 * 60 * 60

print("You have lived for", seconds_lived, "seconds.")

# Day 3: Number Table

print(1, 1, 1, 1, 1)
print(2, 1, 2, 4, 8)
print(3, 1, 3, 9, 27)
print(4, 1, 4, 16, 64)
print(5, 1, 5, 25, 125)