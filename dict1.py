groceries = {
"Baby Spinach": 2.78, 
"Hot Chocolate": 3.70, 
"Crackers": 2.10, 
"Bacon": 9.00, 
"Carrots": 0.56, 
"Oranges": 3.08}

quant = []

for keys,values in groceries.items():
    quant.append(int(input(f"How many {keys} did you buy? ")))
    
totals = 0
i = 0

print()
print("====Izzy's Food Emporium====")
for keys, values in groceries.items():
    print(f"{keys:<20} ${values*quant[i]:.2f}")
    totals += values*quant[i]
    i = i + 1

print("============================")
print(f"                    ${totals:.2f}")