print()
print("-----------------------------------------")
print("    Program to multiply two numbers")
print("-----------------------------------------")


n = [None,None]
for i,g in enumerate(["first","second"]):
    x = 1
    while x == 1:
        answer = input(f"What's the {g} number? ")
        try:
            n[i] = int(answer)
            x = 0
        except ValueError:
            try:
                n[i] = float(answer)
                x = 0
            except ValueError:
                print("This is not a number, try again")


print(f"{n[0]} * {n[1]} = {n[0]*n[1]}")
print("-----------------------------------------")
print()