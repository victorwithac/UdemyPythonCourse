import json
import os

person = [
    {
        "name": 'Maria',
        "lastname": 'Vieira',
        "age": 25,
        "ative": False,
        "grades": ['A', 'A+'],
        "phones": {
            "residencial": "00 0000-0000",
            "cellphone": "00 0000-0000"
        }
    },
    {
        "name": 'Maria',
                "lastname": 'Vieira',
    "age": 25,
    "ative": False,
    "grades": ['A', 'A+'],
    "phones": {
        "residencial": "00 0000-0000",
        "cellphone": "00 0000-0000"
    }
    },
]

BASE_DIR = os.path.dirname(__file__)
SAVE_TO = os.path.join(BASE_DIR, 'file-python.json')

with open(SAVE_TO, 'w') as file:
    json.dump(person, file, indent=2)