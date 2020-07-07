print()

with open("students/exercise_data/names.txt") as txt_file:
    for count,line in enumerate(txt_file): 
        line = line.strip() 
        print(f"{(count+1)}. {line}")

print()