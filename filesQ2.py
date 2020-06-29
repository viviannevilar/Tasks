import pandas as pd

my_data = pd.read_csv("students/exercise_data/colours_20.csv")
#data_answer = my_data[[' RGB',' HEX',' English']]
data_answer = my_data.iloc[:,[1,2,4]]
print(data_answer.to_string(index=False))

print()
my_data = pd.read_csv("students/exercise_data/colours_213.csv")
data_answer = my_data.iloc[:,[1,2,4]]
print(data_answer.to_string(index=False))
