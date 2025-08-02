temperature = 15
if temperature > 30:
    print("It's hot")
    print("Drink juice")
elif temperature > 20:
    print("It's perfect")
else:  # else statement is true
    print("It's cold")
print("Done")

temperature = 25
if temperature > 30:
    print("It's hot")
    print("Drink juice")
elif temperature > 20:  # elif statement is true
    print("It's perfect")
else:
    print("It's cold")
print("Done")

temperature = 35
if temperature > 30:  # if statement is true
    print("It's hot")
    print("Drink juice")
elif temperature > 20:
    print("It's perfect")
else:
    print("It's cold")
print("Done")


# normal code
age = 20
if age >= 18:
    message = "Eligible"
else:
    message = "Not Eligible"
print(message)

# ternary operator (Same code with less lines)
age = 17
message = "Eligible" if age >= 18 else "Not Eligible"
print(message)


# chaining comparision operator
age = 22
if age >= 18 and age <= 65:
    print("You are Eligible")

if 18 <= age < 65:  # chaining comparision operator (Code is simple and clean)
    print("You are Eligible")
