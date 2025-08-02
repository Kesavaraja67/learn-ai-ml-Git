for number in range(3):
    print("Attempt", number + 1, (number + 1) * ".")

for number in range(1, 4):
    print("Attempt", number, number * ".")

# step method
for number in range(1, 10, 2):  # start(1), stop(10), step(2)
    # prints every odd number from 1 to 9
    print("Attempt", number, number * ".")


# for.else
successfull = True
for number in range(3):
    print("Attempt")
    if successfull:
        print("successfull")
        break


successfull = False
for number in range(3):
    print("Attempt")
    if successfull:
        print("successfull")
        break
else:
    print("Attempted 3 times and failed")
