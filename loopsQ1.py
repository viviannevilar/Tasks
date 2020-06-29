def get_number():
    x = 1
    y = 1
    while x == 1:
        answer = input("Type a number to add, or RET to get the total: ")
        if answer == "":
            y = 0
            x = 0
            n = 0
        else:
            try:
                n = int(answer)
                x = 0
            except ValueError:
                try:
                    n = float(answer)
                    x = 0
                except ValueError:
                    print("This is not a number, try again")
    return(n,y)



print()

total = 0
y = 1
while y == 1:
    number,y = get_number()
    total = total + number

print()
print(f"Total = {total}")
print()

