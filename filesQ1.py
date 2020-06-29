count = 1
print()
with open("students/exercise_data/names.txt") as txt_file:
    for line in txt_file: 
        line = line.strip() 
        print(f"{count}. {line}")
        count = count + 1


print()