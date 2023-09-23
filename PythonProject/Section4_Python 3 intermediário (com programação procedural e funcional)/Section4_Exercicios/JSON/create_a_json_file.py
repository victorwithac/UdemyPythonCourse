import json
import os


data = {
    "name": "Victor",
    "age": "25",
    "city": "Porto Alegre"
}

BASE_DIR = os.path.dirname(__file__)
SAVE_TO = os.path.join(BASE_DIR, 'create_a_json_file.json')


with open(SAVE_TO, 'w+') as file:
    json.dump(data, file, indent=2)
print(json.dumps(data, indent=2))