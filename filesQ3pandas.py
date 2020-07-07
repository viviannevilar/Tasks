import pandas as pd

files = {"colours_20","colours_213"}
colours = ["red","green","blue"]

print()
for x in sorted(files):
    my_data = pd.read_csv(f"students/exercise_data/{x}.csv")
    print(f"File: {x}")
    for i in colours:
        a = sum(my_data.iloc[:,4].str.count(i))
        print(f"{i.title()}: {a}")
    print()



#red = sum(my_data[' English'].str.count("red"))
#my_data.head()

