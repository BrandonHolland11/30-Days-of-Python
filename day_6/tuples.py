# Day 6: 30 Days of Python - Tuples

# Exercise 1: Create an empty tuple
empty_tuple = ()
print(empty_tuple)

# Exercise 2: Create tuples of brothers and sisters
brothers = ("James","Michael")
sisters = ("Sarah", "Emily")
print(brothers)
print(sisters)

# Exercise 3: Join brothers and sisters tuples
siblings = brothers + sisters
print(siblings)

# Exercise 4: Count the number of siblings
print(len(siblings))

# Exercise 5: Add parents to the siblings tuple
parents = ("John", "Mary")
family_members = siblings + parents 
print(family_members)

# Exercise 6: Unpack family members
*all_siblings, father, mother = family_members
print("Siblings:", all_siblings)
print("Father:", father)
print("Mother:", mother)

# Exercise 7: Create food tuples
fruits = ("Apple", "Banana", "Orange")
vegetables = ("Carrot", "Broccoli", "Spinach")
animal_products = ("Milk", "Eggs", "Cheese")
print("fruits:", fruits)
print("vegetables:", vegetables)
print("animal products:", animal_products)

# Exercise 8: Combine all food tuples
food_stuff_tp = fruits + vegetables + animal_products
print("All foods:", food_stuff_tp)

# Exercise 9: Convert the food tuple into a list
food_stuff_lt = list(food_stuff_tp)
print("Food list:", food_stuff_lt)
print("Data type:", type(food_stuff_lt))

# Exercise 10: Find the middle food item
middle_index = len(food_stuff_lt) // 2
middle_food = food_stuff_lt[middle_index]
print("Middle food:", middle_food)

# Exercise 11: Find the first three and last three food items
first_three = food_stuff_tp[:3]
last_three = food_stuff_tp[-3:]
print("First three foods:", first_three)
print("Last three foods:", last_three)

# Exercise 12: Delete the food tuple
del food_stuff_tp
print("Food tuple deleted.")

# Exercise 13: Delete tuples
nordic_countries = ("Denmark", "Finland", "Iceland", "Norway", "Sweden")
print("Before deletion:", nordic_countries)
del nordic_countries
print("Nordic countries tuple deleted.")

# Exercise 14: Check countries in a tuple
nordic_countries = ("Denmark", "Finland", "Iceland", "Norway", "Sweden")
print("Is Iceland a nordic country?", "Iceland" in nordic_countries)
print("Is Estonia a nordic country?", "Estonia" in nordic_countries)