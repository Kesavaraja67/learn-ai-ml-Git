course = "Python Programming"
print(len(course))
print(course[0])
print(course[-1])
# slicing
print(course[0:3])
print(course[0:])
print(course[:])

# Escape Sequence
name = "Kesava \"raja"  # here \" is used to escape the " symbol
print(name)
name = "Kesava \\raja"  # \\ is used to escape the character
print(name)
name = "Kesava \'raja"  # single quote
print(name)
name = "Kesava \nraja"  # new line
print(name)

# Formatted Strings
first_name = "Kesava"
last_name = "Raja"

# old way of formatting
print(first_name + " " + last_name)

# new way of formatting
full_name = f"{first_name} {last_name}"  # f-string
print(full_name)
full_name = f"{len(first_name)} {3 + 3}"
print(full_name)

# Strings methods
course = "  python programming  "
print(course.upper())  # prints in uppercase
print(course.lower())  # prints in lowercase
print(course.title())  # prints in title case
print(course.lstrip())  # removes leading spaces(left side empty spaces)
print(course.rstrip())  # removes trailing spaces(right side empty spaces)
print(course.find("pro"))
print(course.find("Pro"))
print(course.replace("p", "j"))
print(course.replace("python", "java"))
# checks if the string contains the substring(gives answer in boolean)
print("pro" in course)
print("right" not in course)

# just testing if Git tracks this
