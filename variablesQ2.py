print()
print("-------------------------------")
print("Program to multiply two numbers")
print("-------------------------------")

x = 1
while x == 1:
    first_number = input("What's the first number? ")
    try:
        n1 = int(first_number)
        x = 0
    except ValueError:
        try:
            n1 = float(first_number)
            x = 0
        except ValueError:
            print("This is not a number, try again")
            # break


x = 1
while x == 1:
    second_number = input("What's the second number? ")
    try:
        n2 = int(second_number)
        x = 0
    except ValueError:
        try:
            n2 = float(second_number)
            x = 0
        except ValueError:
            print("This is not a number, try again")
            # break

print(f"{n1} * {n2} = {n1*n2}")
print("-------------------------------")
print()