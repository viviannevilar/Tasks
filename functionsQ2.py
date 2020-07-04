

number = []
new_number_string = input("Type a number to add: ")

while len(new_number_string) > 0:
    new_number = int(new_number_string)
    number.append(new_number)
    new_number_string = input("Type a number to add: ")

mean = sum(number)/len(number)
print("The average of the numbers is {mean}")

