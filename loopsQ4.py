groceries = [
["Baby Spinach", 2.78], 
["Hot Chocolate", 3.70], 
["Crackers", 2.10], 
["Bacon", 9.00], 
["Carrots", 0.56], 
["Oranges", 3.08]
]

dim = len(groceries)
print()
q = [0]*dim
total = [0]*dim

for i in range(dim):
    q[i] = int(input(f"How many {groceries[i][0]} did you buy?: "))
    total[i] = q[i]*groceries[i][1]

print()
print("====Izzy's Food Emporium====")
for i in range(dim):
    print("{:<10s} \t ${:>4.2f}".format(groceries[i][0],q[i]*groceries[i][1]))

print("============================")    
print("\t\t ${:4.2f}".format(sum(total)))
print()