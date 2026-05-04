import json

def load_data(path="data/sample_data.json"):
    with open(path, "r") as file:
        return json.load(file)
