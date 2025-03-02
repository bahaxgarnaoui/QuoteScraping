import json

def save_data_to_json(data, filename):
    with open(filename, 'a') as f:
        json.dump(data, f, indent=4)