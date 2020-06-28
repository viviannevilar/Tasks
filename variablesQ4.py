print()
print("--------------------------------------------------")
print("                Name and height")
print("--------------------------------------------------")

name = input("What's your name? ")
x = 1
while x == 1:
    height = input("What's your height in centimeters? ")
    try:
        n1 = int(height)
        x = 0
    except ValueError:
        print("This is not a valid number, try again")
        # break

print(f"{name} is {n1}cms tall")

print("--------------------------------------------------")
print()