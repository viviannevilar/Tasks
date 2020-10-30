import csv

files = {"colours_20","colours_213"}

col = []
for x in sorted(files):
    with open(f"students/exercise_data/{x}.csv") as csv_file:
        reader = csv.reader(csv_file)
        for line in reader:
            print(f"{line[1].strip():<15} {line[2].strip():<15} {line[4].strip()}")
            print()

