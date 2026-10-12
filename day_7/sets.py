# Day 7: 30 Days of Python - Sets

# Exercise 1: Find the length of the IT companies set
it_companies = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}
print(len(it_companies))

# Exercise 2: Add Twitter to the IT companies set
it_companies.add("Twitter")
print(it_companies)

# Exercise 3: Add multiple IT companies
it_companies.update(["Netflix", "Tesla", "Spotify"])
print(it_companies)
print("Number of companies:", len(it_companies))

# Exercise 4: Remove Twitter from the IT companies set
it_companies.remove("Twitter")
print(it_companies)
print("Number of companies:", len(it_companies))

# Exercise 5: Remove vs Discard
it_companies.discard("Netflix")
print(it_companies)
it_companies.discard("TikTok")
print(it_companies)
print("Number of companies:", len(it_companies))

# Exercise 6: Clear the IT companies set
it_companies.clear()
print(it_companies)
print(len(it_companies))

# Exercise 7: Delete the IT companies set
del it_companies
print("IT companies set deleted.")

# Exercise 8: Join A and B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
joined_sets = A.union(B)
print(joined_sets)
print("Number of elements:", len(joined_sets))

# Exercise 9: Find the intersection of A and B
common_elements = A.intersection(B)
print("common_elements:", common_elements)
print("Number of common elements:", len(common_elements))

# Exercise 10: Check of A is a subset of B
print("Is A a subset of B?", A.issubset(B))
print("Is B a subset of A?", B.issubset(A))

# Exercise 11: Check if A and B are disjoint
print("Are A and B disjoint?", A.isdisjoint(B))

# Exercise 12: Find the symmetric difference of A and B
symmetric_difference = A.symmetric_difference(B)
print("symmetric_difference:", symmetric_difference)

# Exercise 13: Delete sets A and B
del A
del B
print("Sets A and B deleted.")

# Exercise 14: Convert ages into a set
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages_set = set(ages)
print("Ages list:", ages)
print("Ages set:", ages_set)
print("List length:", len(ages))
print("Set length:", len(ages_set))

# Exercise 15: Compare Data Types
text = "Python"
my_list = [1, 2, 2, 3]
my_tuple = (1, 2, 2, 3)
my_set = {1, 2, 2, 3}

print("String:", text)
print("List:", my_list)
print("Tuple:", my_tuple)
print("Set:", my_set)

print("String length:", len(text))
print("List length:", len(my_list))
print("Tuple length:", len(my_tuple))
print("Set length:", len(my_set))

# Exercise 16: Count unique words
sentence = "I am a teacher and I love to inspire and teach people."
words = sentence.split()
unique_words = set(words)
print("All words:", words)
print("Unique words:", unique_words)
print("Number of unique words:", len(unique_words))