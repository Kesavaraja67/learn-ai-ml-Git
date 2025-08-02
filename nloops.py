for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")  # formatted strings

# Iterables
for x in "python":  # x will iterate to each letter of the string
    print(x)

for x in [1, 2, 3, 4, 5]:  # x will iterate to each list
    print(x)


# While loops
number = 100
while number > 0:
    print(number)
    number //= 2

# command = ""
# while command.lower() != "quit":
#     command = input(">")
#     print("ECHO", command)

# # infinite loops
# while True:
#     command = input(">")
#     print("ECHO", command)
#     if command.lower() == "quit":
#         break

# Exercise(To count and print Even numbers from 1 to 10 )
count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"We have {count} even numbers")
