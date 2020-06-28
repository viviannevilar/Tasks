print()
print("----------------------------------------------------------------")
print("         Are you tall enough to ride the rollercoaster?         ")
print("----------------------------------------------------------------")


x = 1
while x == 1:
    numb = input("What is your height in cms? ")
    try:
        height= int(numb)
        x = 0
    except ValueError:
        print("This is not an integer, try again")
 
if height >= 120:
     print("Hop on!")
else:
    print("Sorry, not today :(")

print("----------------------------------------------------------------")
print()