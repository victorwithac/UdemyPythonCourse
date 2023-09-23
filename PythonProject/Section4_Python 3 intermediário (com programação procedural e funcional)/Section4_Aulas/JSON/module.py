import json
import os

person =   [
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
    {   "name": 'Joana',
        "lastname": 'Amaral',
        "age": 25,
        "ative": False,
        "grades": ['A', 'A+'],
        "phones": {
            "residencial": "00 0000-0000",
            "cellphone": "00 0000-0000"
        }
        },
    ]
    # {
    #     "name": 'Joana',
    #             "lastname": 'Vieira',
    # "age": 25,
    # "numbers": (2, 4, 6, 8, 10),
    # "ative": False,
    # "grades": ['A', 'A+'],
    # "phones": {
    #     "residencial": "00 0000-0000",
    #     "cellphone": "00 0000-0000"
    # }
    # }

FILE_NAME = os.path.basename(__file__) #return only the name of the file
BASE_DIR = os.path.dirname(__file__) #return only the path of the file
SAVE_TO = os.path.join(BASE_DIR, 'file-python.json')


# print(BASE_DIR) #return only the path of the file
# print(__file__)#return the path and the name of the file
# print(FILE_NAME) #return only the name of the file
# print(SAVE_TO)


# with open(SAVE_TO, 'w+', encoding='utf8') as file:
#     json.dump(person, file, indent=2)
# print(json.dumps(person, indent=2))
#
# # print()

with open(SAVE_TO, 'r') as file:
    person_2 = json.load(file)
    # print(person)
    # print()
    # print(person_2)
    # print()
    # print(person_2['name'])
    # print(person_2['grades'])

    for persons in person_2:
        print(persons)




