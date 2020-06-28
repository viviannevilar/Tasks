print()
print("-------------------------------------------------")
print("Program to transform kms to meters and centimeters")
print("-------------------------------------------------")

x = 1
while x == 1:
    number = input("What's the number of kms? ")
    try:
        n1 = int(number)
        x = 0
    except ValueError:
        try:
            n1 = float(number)
            x = 0
        except ValueError:
            print("This is not a number, try again")
            # break

print(f"{n1}km = {int(n1* 1000)}m \n{n1}km = {int(n1* 1000000)}cm")

print("-------------------------------------------------")
print()