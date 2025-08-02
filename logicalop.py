high_income = False
good_credit = True

if high_income and good_credit:
    print("Eligible")  # Eligible only if both are True
else:
    print("Not eligible")


high_income = True
good_credit = True
student = False

if not student:
    print("Eligible")
else:
    print("Not eligible")


high_income = False
good_credit = True
student = False

if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not eligible")
