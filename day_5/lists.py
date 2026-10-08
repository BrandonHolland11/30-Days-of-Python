# Day 5: 30 Days of Python - Lists

# Exercise 1: Declare an empty list
empty_list = []

# Exercise 2: Declare a list with more than 5 items
fruits = ["apple", "banana", "orange", "mango", "grape", "pineapple"]

# Exercise 3: Find the length of the list
print(len(fruits))

# Exercise 4: First, Middle, and Last Items
print(fruits[0])
print(fruits[3])
print(fruits[-1])

# Excercise 5: Mixed Data Types
mixed_data_types = ["Brandon", 24, 6.3, "Single", "Greensboro"]
print(mixed_data_types)

# Exercise 6: IT Companies
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies)

# Exercise 7: Count the IT Companies
print(len(it_companies))

# Exercise 8: First, Middle, and Last IT Companies
print(it_companies[0])
print(it_companies[3])
print(it_companies[-1])

# Exercise 9: Modify an IT Company
it_companies[1] = "Netflix"
print(it_companies)

# Exercise 10: Add an IT Company
it_companies.append("Tesla")
print(it_companies)

# Exercise 11: Insert an IT Company in the Middle
middle_index = len(it_companies) // 2
it_companies.insert(middle_index, "Nvidia")
print(it_companies)

# Exercise 12: Change a Company to Uppercase
it_companies[0] = it_companies[0].upper()
print(it_companies)

# Exercise 13: Join the IT Companies
print(", ".join(it_companies))

# Exercise 14: Check if an IT Company Exists
print("Netflix" in it_companies)

# Exercise 15: Sort the IT Companies
it_companies.sort()
print(it_companies)

# Exercise 16: Reverse the IT Companies
it_companies.reverse()
print(it_companies)

# Exercise 17: First 3 IT Companies
print(it_companies[:3])

# Exercise 18: Last 3 IT Companies
print(it_companies[-3:])

# Exercise 19: Get the Middle IT Company
middle_index = len(it_companies) // 2
print(it_companies[middle_index])

# Exercise 20: Remove the First IT Company
it_companies.pop(0)
print(it_companies)

# Exercise 21: Remove the Middle IT Company
middle_index = len(it_companies) // 2
it_companies.pop(middle_index)
print(it_companies)

# Exercise 22: Remove the Last IT Company
it_companies.pop()
print(it_companies)

# Exercise 23: Remove All IT Companies
it_companies.clear()
print(it_companies)

# Exercise 24: Delete the IT Companies List
del it_companies

# Exercise 25: Join Front End and Back End Technologies
front_end = ["HTML", "CSS", "JS", "React", "Redux"]
back_end = ["Node", "Express", "MongoDB"]
front_end.extend(back_end)
print(front_end)

# Exercise 26: Copy the Joined List
full_stack = front_end.copy()
print(full_stack)

# Exercise 27: Insert Python & SQL After Redux
redux_index = full_stack.index("Redux")
full_stack.insert(redux_index + 1, "Python")
full_stack.insert(redux_index + 2, "SQL")
print(full_stack)

# Excercise 28: Countries List
countries = ["China", "Russia", "USA", "Finland", "Sweden", "Norway", "Denmark"]

# Excercise 29: Find the Middle Country
middle_index = len(countries) // 2
print(countries[middle_index])

# Excercise 30: Divide Countries Into Two Equal Lists
middle_index = len(countries) // 2
first_half = countries[:middle_index + 1]
second_half = countries[middle_index + 1:]
print(first_half)
print(second_half)

# Excercise 31: Unpack Countries
first, second, third, *scandic_countries = countries
print(first)
print(second)
print(third)
print(scandic_countries)

# Excercise 32: Ages List
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Excercise 33: Sort Ages
ages.sort()
print("Sorted ages:", ages)
print("Min age:", ages[0])
print("Max age:", ages[-1])
print("Median age:", ages[len(ages) // 2])
print("Average age:", sum(ages) / len(ages))
print("Range of ages:", ages[-1] - ages[0])

# Excercise 34: Compare Ages
min_age = min(ages)
max_age = max(ages)
average_age = sum(ages) / len(ages)
print("Min difference:", abs(min_age - average_age))
print("Max difference:", abs(max_age - average_age))

# Excercise 35: Find the Middle Country
middle_country = countries[len(countries) // 2]
print("Middle country:", middle_country)

# Excercise 36: Divide Countries Into Two Lists
middle_index = len(countries) // 2
first_group = countries[:middle_index]
second_group = countries[middle_index + 1:]
print("First group:", first_group)
print("Second group:", second_group)

# Excercise 37: Find the Middle Ages
middle_index = len(ages) // 2
print("Middle ages:", ages[middle_index - 1:middle_index + 1])
