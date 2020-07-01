import pandas as pd

files = {"colours_20","colours_213"}

for x in files:
    my_data = pd.read_csv(f"students/exercise_data/{x}.csv")
    data_answer = my_data.iloc[:,[1,2,4]]
    print(data_answer.to_string(index=False))
    print()

#data_answer = my_data[[' RGB',' HEX',' English']]