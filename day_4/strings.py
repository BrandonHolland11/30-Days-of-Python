# Day 4: 30 Days of Python - Strings

first_name = "Brandon"
last_name = "Holland"

full_name = first_name + " " + last_name

print(full_name)

# Day 4: String Length

print(len(first_name))
print(len(last_name))
print(len(full_name))

# Day 4: Compare Name Lengths

print(len(first_name) == len(last_name))

# Day 4: String Concatenation

company = "Coding"
school = "For"
subject = "All"
space = " "

company_name = company + space + school + space + subject

print(company_name)

# Day 4: Company Name Length

print(len(company_name))

# Day 4: Uppercase and Lowercase
print(company_name.upper())
print(company_name.lower())

# Day 4: Capitalize, Title, and Swapcase

print(company_name.capitalize())
print(company_name.title())
print(company_name.swapcase())

# Day 4: Remove the First Word

print(company_name[7:])

# Day 4: Find and Index

print(company_name.find("Coding"))
print(company_name.index("Coding"))

# Replacing a Word

print(company_name.replace("Coding", "Python"))

# Day 4: Replace a Word in a Sentence

sentence = "Python for Everyone"
print(sentence.replace("Everyone", "All"))

# Day 4: Split a String

print(company_name.split())

# Day 4: Split a Comma-Separated String

companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(", "))

# Day 4: First Character

print(company_name[0])

# Day 4: Last Character

print(company_name[-1])

# Day 4: Character at Index 10

print(company_name[10])

# Day 4: Acronym for Python for Everyone

phrase = "Python for Everyone"
acronym  = "".join(word[0] for word in phrase.split())
print(acronym)

# Day 4: Acronym for Coding For All

acronym_company = "".join(word[0] for word in company_name.split())
print(acronym_company)

# Day 4: Find the Position of C

print(company_name.index("C"))

# Day 4: Find the Position of F

print(company_name.index("F"))

# Day 4: Find the Last Position of 1

print(company_name.rfind("1"))

# Day 4: Find the First Occurrence of "because"

sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.find("because"))

# Day 4: Find the Last Occurrence of "because"

print(sentence.rfind("because"))

# Day 4: Slice Out "because because because"

print(sentence[31:54])

# Day 4: Check Whether a Sentence Starts with "You"

print(sentence.startswith("You"))

# Day 4: Check Whether a Sentence Ends with "conjunction"

print(sentence.endswith("conjunction"))

# Day 4: Remove Extra Spaces

text = "   Coding For All   "
print(text.strip())

# Day 4: Check Valid Variable Names

print("30DaysOfPython".isidentifier())

print("thirty_days_of_python".isidentifier())

# Day 4: Join Python Libraries

libraries = ["Django", "Flask", "Bottle", "Pyramid", "Falcon"]

print("# ".join(libraries))

# Day 4: New Lines

print("I am enjoying this challenge.\nI just wonder what is next.")

# Day 4: Tabs

print("Name\tAge\tCountry\tCity")

print("Brandon\t24\tUSA\tGreensboro")

# Day 4: String Formatting

radius = 10

area = 3.14 * radius ** 2

print(f"The area of a circle with radius {radius} is {area} meters square.")

# Day 4: Display Calculations

a = 8

b = 6

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")