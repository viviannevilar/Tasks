import json
with open("data/quiz.json") as json_file:
    json_data = json.load(json_file)
    
quiz = json_data["quiz"] 


for number, item in quiz.items():
    print(f"Question {number}: " + item["question"])
    for options in item["options"]:
        print("      " + options)