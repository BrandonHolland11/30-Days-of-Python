# Day 8: 30 Days of Python - Dictionaries

# Exercise 1: Create an empty dictionary called dog
from tokenize import Single


dog = {}
print(dog)
print(type(dog))

# Exercise 2: Add information to the dog dictionary
dog["name"] = "Max"
dog["color"] = "Brown"
dog["breed"] = "Labrador"
dog["legs"] = 4
dog["age"] = 3
print(dog)

# Exercise 3: Create a student dictionary

student = {
    "first_name": "Brandon",
    "last_name": "Holland",
    "gender": "Male",
    "age": 24,
    "marital_status": "Single",
    "skills": ["Python"],
    "country": "United States",
    "city": "Greensboro",
}
print(student)

# Exercise 4: Check the length of the student dictionary
print(len(student))

# Exercise 5: Get the skills value and check its data type
skills = student["skills"]
print(skills)
print(type(skills))

# Exercise 6: Add skills to the student dictionary
student["skills"].append("SQL")
student["skills"].append("JavaScript")
print(student["skills"])

# Exercise 7: Get the student dictionary keys as a list
student_keys = list(student.keys())
print(student_keys)

# Exercise 8: Get the student dictionary values as a list
student_values = list(student.values())
print(student_values)

# Exercise 9: Convert dictionary into a list of tuples
student_items = list(student.items())
print(student_items)

# Exercise 10: Delete an item from the student dictionary
del student["marital_status"]
print(student)

# Exercise 11: Delete one of the dictionaries
del dog