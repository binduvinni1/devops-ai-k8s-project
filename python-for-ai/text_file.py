import os
import pandas as pd


list_class = [
    {"name": "Grace", "age": 30, "city": "New York"},
    {"name": "John", "age": 25, "city": "Los Angeles"},
    {"name": "Jane", "age": 28, "city": "Chicago"},
]

os.makedirs("data", exist_ok=True)

with open("data/class_data.csv", "w") as file:
    file.write("name,age,city\n")
    for student in list_class:
        file.write(f"{student['name']},{student['age']},{student['city']}\n")
    

pd.DataFrame(list_class).to_csv("data/class_data_pandas.csv", index=False)