print()

n = 3
names = []
order = ["first", "second","third"]
order.reverse()

while n > 0:
    names.append(input("What's the {} name?: ".format(order[n-1])))
    n -= 1

print()
print("The names are: ")

for i in range(3):
    print("  " + names[i])

print()    
