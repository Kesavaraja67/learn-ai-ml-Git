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
