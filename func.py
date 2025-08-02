def greet():
    print("Hii")
    print("How are you ?")


greet()

# function using Arguments


def greet1(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome")


greet1("kesavaraja", "M")


def greeting(name):
    return f"Hi {name}"


message = greeting("Kesava")
print(message)


# key word Arguments
def increment(numb, by):
    return numb + by


print(increment(5, by=2))  # by=2 is a keyword arguments


# xargs
def multiplication(*numbers):
    print(numbers)


multiplication(1, 2, 3, 4)


def multiply(*numbers):
    total = 1
    for numbers in numbers:
        total *= numbers
    return total


print(multiply(1, 2, 3, 4, 5, 6))
