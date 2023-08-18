import copy

# copy - retorna uma cópia rasa(shallow copy)
d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1 , 2]
}

# d2 = d1.copy()
# del d1['l1']
# print(d1)
# print(d2)


d2 = copy.deepcopy(d1)
d2['c1'] = 100
d2['l1'][1] = 5
print(d2)
print(d1)


