print()
print("----------------------------------------------------------------")
print("Program to determine whether it is time for Roary to catch moths")
print("----------------------------------------------------------------")

moths_in_house = False
mitch_is_home = False

if (moths_in_house & mitch_is_home) == True:
    print("Get the moths!")
elif not all([moths_in_house, mitch_is_home, False]):
    print("No threats detected.")
elif (moths_in_house == True) & (mitch_is_home == False):
    print("Meooooooooooooow! Hissssss!")
else:
    print("Climb on Mitch.")

print("-----------------------------------------------------")
print()

