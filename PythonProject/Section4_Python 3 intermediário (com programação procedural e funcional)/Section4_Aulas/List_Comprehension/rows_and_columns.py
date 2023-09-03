import pprint

for  x in range(1, 11):
    for y in range(1, 6):
        print


rows_and_columns = [
    (x, y)
    if y != 2 else (x, y * 1000)
    for x in range(1, 11)
    for y in range(1, 6)
    if x != 2
]


pprint.pprint(rows_and_columns)